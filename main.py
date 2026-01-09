from src.data_handler import load_database, save_database
from src.linguistics import analyze_theophoric_elements

def main():
    print("--- Start der Analyse ---")
    
    file_path = "data/kassite_names_db_analyzed.json"
    db = load_database(file_path)
    
    if not db:
        print("Die Datenbank scheint leer zu sein oder wurde nicht gefunden.")
        return 
    
    print(f"{len(db)} Einträge erfolgreich geladen.")
    
    kassite_gods = [ 
        "Bugaš", "bugašu", "Sugab", "Šugab", 
        "Šuriaš", "suriaš", "shuriash",
        "Maruttaš", "marutash",
        "Buriaš", "buriyaš", "burash",
        "Indaš", "indas",
        "Hala", "Sah", "saḫ",
        "Harbe", "enlil" 
    ]
    
    results = analyze_theophoric_elements(db, kassite_gods)
    for entry in db:
        name = entry.get('transcription')
        match = next((item for item in results if item['name'] == name), None)
        if match:
            entry['detected_gods'] = match['gods']
            entry['god_position'] = match['position']
    
    save_database(db, "data/kassite_names_db_enriched.json")
    print(f"Angereicherte Datenbank mit {len(results)} Götter-Tags gespeichert.")

if __name__ == "__main__":
    main()
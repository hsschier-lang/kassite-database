import json
import os

def load_database(file_path):
    """
    Lädt die Datenbank aus einer JSON-Datei. 
    Gibt eine leere Liste zurück, falls die Datei nicht existiert.
    """
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f" Datenbank geladen! {len(data)} Einträge gefunden.")
        return data
    else:
        print("ℹ Keine Datei gefunden. Eine neue Datenbank wird initialisiert.")
        return []

def save_database(data, file_path):
    """Speichert die aktuelle Liste in die JSON-Datei."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Daten erfolgreich in '{file_path}' gespeichert.")
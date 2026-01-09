def analyze_theophoric_elements(data, gods_list):
    """
    Untersucht eine Liste von Namen auf Götter-Elemente.
    """
    results = []
    
    for entry in data:
        name = entry.get('transcription','').lower()
        search_name = name.replace('š', 's').replace('ḫ', 'h').replace('ṣ', 's')
        
        found_gods = []
        for god in gods_list:
            god_clean = god.lower().replace('š', 's').replace('ḫ', 'h').replace('ṣ', 's')
            
            if god_clean in search_name:
                found_gods.append(god)
        
        if found_gods:
            results.append({
                'name': entry.get('transcription'),
                'gods': list(set(found_gods)), 
                'position': 'Anfang' if search_name.startswith(found_gods[0].lower().replace('š', 's')) else "Ende/Mitte"
            })
    return results
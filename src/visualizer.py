# src/visualizer.py
import matplotlib.pyplot as plt
from collections import Counter

def plot_god_distribution(theophoric_names):
    """
    Erstellt ein Balkendiagramm basierend auf den gefundenen Götternamen.
    """
    all_found_gods = []
    for item in theophoric_names:
        all_found_gods.extend(item['gods']) 

    god_counts = Counter(all_found_gods)
    common_gods = god_counts.most_common()

    names = [x[0] for x in common_gods] 
    counts = [x[1] for x in common_gods]

    plt.figure(figsize=(10, 6))
    plt.bar(names, counts, color='skyblue', edgecolor='navy')
    plt.title('Häufigkeit der Gottheiten in den kassitischen Namen', fontsize=14)
    plt.xlabel('Gottheit', fontsize=12)
    plt.ylabel('Anzahl der Nennungen', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for i, v in enumerate(counts):
        plt.text(i, v + 0.2, str(v), ha='center', fontweight='bold')

    plt.tight_layout()
    # Wichtig: In Skripten brauchen wir plt.show(), damit das Fenster aufpoppt
    plt.show()
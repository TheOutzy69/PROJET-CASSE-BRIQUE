"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025 - 21/10/2025
Objectif : Aquérir, organiser et sauvegarder les scores
"""

import csv
from datetime import datetime

def sauvegarder_score(score, fichier='scores.csv'):
    date_actuelle = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nouveau_score = [date_actuelle, score]

    # Lire les scores existants
    scores = []
    try:
        with open(fichier, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            scores = list(reader)
    except FileNotFoundError:
        pass  # Le fichier n'existe pas encore

    # Ajouter le nouveau score en haut de la pile
    scores.insert(0, nouveau_score)

    # Garder uniquement les 10 premiers
    scores = scores[:10]

    # Réécrire le fichier avec les scores mis à jour
    with open(fichier, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(scores)

    print(f"Score enregistré : {score} points le {date_actuelle}")
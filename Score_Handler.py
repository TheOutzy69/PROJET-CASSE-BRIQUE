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

    # Ajouter le nouveau score à la fin
    scores.append(nouveau_score)

    # Garder uniquement les 10 derniers (en supprimant les plus anciens)
    if len(scores) > 10:
        scores = scores[-10:]

    # Réécrire le fichier avec les scores mis à jour
    with open(fichier, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(scores)

    print(f"Score enregistré : {score} points le {date_actuelle}")


def update_highest(score, file='highest.csv'):
    highest = None

    # Tenter de lire le meilleur score existant
    try:
        with open(file, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ligne = next(reader)
            highest = int(ligne[1])  # colonne 1 = score
    except (FileNotFoundError, StopIteration, ValueError):
        pass  # fichier inexistant, vide ou mal formaté


    # Comparer et mettre à jour si nécessaire
    if highest is None or score > highest:
        date_actuelle = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([date_actuelle, score])
        print(f"🎉 Nouveau meilleur score : {score} points le {date_actuelle}")
    else:
        print(f"Score actuel : {score} points. Meilleur score conservé : {highest} points.")


def Score_exec(score):
    return sauvegarder_score(score),update_highest(score)


def get_highest(file = 'highest.csv'):
    highest = None
    # Tenter de lire le meilleur score existant
    try:
        with open(file, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ligne = next(reader)
            highest = int(ligne[1])  # colonne 1 = score
    except (FileNotFoundError, StopIteration, ValueError):
        pass  # fichier inexistant, vide ou mal formaté
    return highest
    

def get_average(file='scores.csv'):
    scores = []

    try:
        with open(file, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for ligne in reader:
                try:
                    score = int(ligne[1])  # colonne 1 = score
                    scores.append(score)
                except (IndexError, ValueError):
                    continue  # ignore les lignes mal formatées
    except FileNotFoundError:
        print("Fichier introuvable.")
        return None

    if not scores:
        print("Aucun score valide trouvé.")
        return None

    moyenne = sum(scores) / len(scores)
    print(f"Moyenne des {len(scores)} derniers scores : {moyenne:.2f}")
    return moyenne


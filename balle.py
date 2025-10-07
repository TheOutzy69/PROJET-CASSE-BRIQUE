"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer un systéme fonctionnel pour la balle
"""

class Ball:
    
    def __init__(self,witdh,height,color,lifePoints):
        self.witdh = witdh
        self.height = height
        self.color = color
        self.lifePoints = lifePoints
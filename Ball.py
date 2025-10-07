"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer un systéme fonctionnel pour la balle
"""

class Ball:
    
    def __init__(self, witdh, height, color) :
        self.__witdh = witdh
        self.__height = height
        self.__color = color
        self.__lifePoints = 5
    
    def getSize(self) :
        
        return self.__height,self.__witdh
    
    def getColor(self) :
        
        return self.__color
    
    def manageLifePoints(self, sub) :
        if sub :
            self.__lifePoints -= 1
        else :
            self.__lifePoints += 1
    
    def getLifePoints(self) :
        return self.__lifePoints 
    

    
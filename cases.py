"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer les cases du casse brique
"""

class BOX(self):
    def __init__(self, x, y, width, height, color):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color
        self.__visible = True
    
    def getSize(self) :
        
        return self.__height,self.__width
    
    def getColor(self) :
        
        return self.__color
    
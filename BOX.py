"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer les cases du casse brique
"""

class BOX:
    def __init__(self, canvas, x, y):
        self.__canvas = canvas
        self.__x = x
        self.__y = y   

    def création(self):
        self.__rectangle = self.__canvas.create_rectangle(self.__x, self.__y, self.__x + 50, self.__y + 20, fill='red')
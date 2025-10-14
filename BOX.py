"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer les cases du casse brique
"""

class Box:
    def __init__(self, canvas, x, y):
        
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__alive = True
        self.__score = 0
    
    def création(self):
        self.__rectangle = self.__canvas.create_rectangle(self.__x, self.__y, self.__x + 120, self.__y + 50, fill='red', outline='white', width=2)

    def getPos(self):
        return self.__canvas.coords(self.__rectangle)
    
    def destroy(self):
        if self.__alive:
            self.__canvas.delete(self.__rectangle)
            self.__alive = False
        self.__score += 10
    
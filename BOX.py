"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer les cases du casse brique
"""

class BOX:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.__canvas = canvas
        self.__id = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.__alive = True 
    
    def destroy(self):
        if self.__alive:
            self.canvas.delete(self.id)
            self.__alive = False

    def position(self):
        return self.canvas.coords(self.id)
    
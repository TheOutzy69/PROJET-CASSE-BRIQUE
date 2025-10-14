"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer un systéme fonctionnel pour la balle
"""

class Ball:
    
    def __init__(self, canvas, x, y):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
    
    def création(self):
        self.__circle = self.__canvas.create_oval(self.__x, self.__y, self.__x + 30, self.__y + 30, fill='white', outline='blue', width=2)
        
    

    
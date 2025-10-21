"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025 - 21/10/2025
Objectif : Créer les cases du casse brique

Improvements :
    - Créer des sous-classes pour différents types de briques (par exemple, briques résistantes, briques explosives).
"""

class Box:
    
    """
    Permet de créer les briques
    
    Entrées:
        - Canvas : la surface sur laquelle se déroule le jeu
        - X et Y : coordonnées
        - Alive : vie de la brique
    
    """
    
    def __init__(self, canvas, x, y):
        
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__alive = True
        self.__score = 0
    
    def création(self):
        """
        Permet de créer une brique
        """
        self.__rectangle = self.__canvas.create_rectangle(self.__x, self.__y, self.__x + 120, self.__y + 50, fill='red', outline='white', width=2)

    def getPos(self):
        """
        Permet d'avoir la coordonnées de la brique
        """
        return self.__canvas.coords(self.__rectangle)
    
    def destroy(self):
        """
        Permet de détruire la brique
        """
        if self.__alive:
            
            self.__canvas.delete(self.__rectangle)
            self.__alive = False
            
        self.__score += 10
    
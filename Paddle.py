"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025 - 21/10/2025
Objectif : Créer un systéme fonctionnel pour la raquette
"""
class Paddle :
    """
    Classe définissant la raquette.
    Entrées : 
        - canvas : pour définir dans l'espace de jeu.
        - x et y : coordonnées dans l'espace.
        - width et height : taille de la raquette.
        - color : couleur.
        - id : entrée d'identité pour pouvoir réappeller l'objet.
    """
    def __init__(self, canvas, x, y) :
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__width = 100
        self.__height = 20
        self.__color = 'blue'
        self.__id = None
    
    def creation(self) :
        #Fonction pour créer l'objet dans l'environnement
        self.__id = self.__canvas.create_rectangle(self.__x, self.__y, self.__x + self.__width, self.__y + self.__height, fill=self.__color)

    def move_left(self, event) :
        #Fonction de déplacement vers la gauche associée au bind de la flèche gauche
        
        if event.keysym == 'Left' :
            
            if self.__x - self.__width/2 > 0 - self.__width/2 :
                
                self.__canvas.move(self.__id, -20, 0)
                self.__x -= 20
            
    def move_right(self, event) :
        #Fonction de déplacement vers la droite associée au bind de la flèche droite
        if event.keysym == 'Right' :
            
            if self.__x + self.__width/2 < int(self.__canvas['width']) - self.__width/2 :
                
                self.__canvas.move(self.__id, 20, 0)
                self.__x += 20

    def move(self, dx) :
        #Fonction de déplacement associée au mouvement de la souris
        new_x = self.__x + dx
        canvas_width = int(self.__canvas['width'])
        
        if 0 <= new_x <= canvas_width - self.__width:
            
            self.__canvas.move(self.__id, dx, 0)
            self.__x = new_x


    def getPos(self) :
        #Fonction d'obtention des coordonnées de l'objet
        return self.__canvas.coords(self.__id) 
"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer un systéme fonctionnel pour la balle
"""
import math,random

class Ball:
    
    def __init__(self,canvas,rayon,color,width,height,speed) :
        self.__canvas = canvas
        self.__color = color
        self.__rayon = rayon
        self.__width = width
        self.__height = height
        self.__x = self.__width/2
        self.__y = self.__height/2
        self.__speed = speed
        self.__angle = random.uniform(0,2*math.pi)
        self.__dX = speed*math.cos(self.__angle)
        self.__dY = speed*math.cos(self.__angle)
        self.__lifePoints = 5
        self.__id = None
    
    def création(self):
        self.__id = self.__canvas.create_oval(self.__x-self.__rayon,
                                              self.__y-self.__rayon,
                                              self.__x+self.__rayon,
                                              self.__y+self.__rayon,
                                              fill= self.__color)
    
    def move(self):
        
        #Rebond à droite
        if self.__x + self.__rayon + self.__dX > self.__width :
            self.__x = 2*(self.__width-self.__rayon)-self.__x
            self.__dX = -self.__dX
        
        #Rebond à Gauche
        elif self.__x - self.__rayon + self.__dX < 0 :
            self.__x = 2*self.__rayon-self.__x
            self.__dX = -self.__dX
        
        #Rebond en bas
        elif self.__y + self.__rayon + self.__dY > self.__height :
            self.__y = 2*(self.__height-self.__rayon)-self.__y
            self.__dY = -self.__dY
        
        #Rebond en haut
        elif self.__y - self.__rayon + self.__dY < 0 :
            self.__y = 2*self.__rayon-self.__y
            self.__dY = -self.__dY
        
        self.__x += self.__dX
        self.__y += self.__dY
        
        self.__canvas.coords(self.__id,self.__x-self.__rayon,
                                              self.__y-self.__rayon,
                                              self.__x+self.__rayon,
                                              self.__y+self.__rayon)
        
        self.__canvas.after(20,self.move)

    def getPos(self):
        return self.__canvas.coords(self.__id)
    
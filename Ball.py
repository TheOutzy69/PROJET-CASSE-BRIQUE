"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer un systéme fonctionnel pour la balle
"""
import math,random

class Ball:
    
    def __init__(self,canvas,rayon,color,width,height,speed, paddle, brick) :
        self.__canvas = canvas
        self.__color = color
        self.__rayon = rayon
        self.__width = width
        self.__height = height
        self.__x = self.__width/2
        self.__y = self.__height/2
        self.__angle = random.uniform(0,2*math.pi)
        self.__dX = speed*math.cos(self.__angle)
        self.__dY = speed*math.cos(self.__angle)
        self.__id = None
        self.__paddle = paddle
        self.__bricks = brick
        self.__life = 5
        
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
            self.__life -= 1
            self.__x = self.__width/2
            self.__y = self.__height/2
        
        #Rebond en haut
        elif self.__y - self.__rayon + self.__dY < 0 :
            self.__y = 2*self.__rayon-self.__y
            self.__dY = -self.__dY
        
        self.__x += self.__dX
        self.__y += self.__dY
        
        
        #REBOND PADDLE
        paddle_pos = self.__paddle.getPos()
        if paddle_pos:
            rx1, ry1, rx2, ry2 = paddle_pos
            # Bounce on top face of paddle
            if (ry1 <= self.__y + self.__rayon <= ry2) and (rx1 <= self.__x <= rx2) and (self.__dY > 0):
                self.__y = ry1 - self.__rayon
                self.__dY = -self.__dY
            # Bounce on left face of paddle
            elif (rx1 - self.__rayon <= self.__x <= rx1) and (ry1 <= self.__y <= ry2) and (self.__dX > 0):
                self.__x = rx1 - self.__rayon
                self.__dX = -self.__dX
            # Bounce on right face of paddle
            elif (rx2 <= self.__x <= rx2 + self.__rayon) and (ry1 <= self.__y <= ry2) and (self.__dX < 0):
                self.__x = rx2 + self.__rayon
                self.__dX = -self.__dX
            # Bounce on bottom face of paddle
            elif (ry2 <= self.__y <= ry2 + self.__rayon) and (rx1 <= self.__x <= rx2) and (self.__dY < 0):
                self.__y = ry2 + self.__rayon
                self.__dY = -self.__dY
        
        #REBOND BRIQUES
        
        for brick in self.__bricks:
            brickPos = brick.getPos()

            if brickPos:
                bx1, by1, bx2, by2 = brickPos
                # Bounce on top face of brick
                if (by1 <= self.__y + self.__rayon <= by2) and (bx1 <= self.__x <= bx2) and (self.__dY > 0):
                    self.__y = by1 - self.__rayon
                    self.__dY = -self.__dY
                    brick.destroy()
                    
                # Bounce on left face of brick
                elif (bx1 - self.__rayon <= self.__x <= bx1) and (by1 <= self.__y <= by2) and (self.__dX > 0):
                    self.__x = bx1 - self.__rayon
                    self.__dX = -self.__dX
                    brick.destroy()
                    
                # Bounce on right face of brick
                elif (bx2 <= self.__x <= bx2 + self.__rayon) and (by1 <= self.__y <= by2) and (self.__dX < 0):
                    self.__x = bx2 + self.__rayon
                    self.__dX = -self.__dX
                    brick.destroy()
                    
                # Bounce on bottom face of brick
                elif (by2 <= self.__y <= by2 + self.__rayon) and (bx1 <= self.__x <= bx2) and (self.__dY < 0):
                    self.__y = by2 + self.__rayon
                    self.__dY = -self.__dY
                    brick.destroy()

        self.__canvas.coords(self.__id,self.__x-self.__rayon,
                                              self.__y-self.__rayon,
                                              self.__x+self.__rayon,
                                              self.__y+self.__rayon)
        self.__canvas.after(20,self.move)


    def getPos(self):
        return self.__canvas.coords(self.__id)
    
    def getLife(self):
        return self.__life
    
"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025 - 21/10/2025
Objectif : Créer un systéme fonctionnel pour la balle
"""
import math,random
import Score_Handler as sh

class Ball:
    
    """
    Classe qui permet de gérer la balle
    
    Entrées:
    
        - Canvas : la surface sur laquelle se déroule le jeu
        - Rayon : Pour de la balle
        - Color : couleur
        - Width : largeur
        - Height : hauteur
        - Speed : vitesse
        - Paddle : raquette
        - Brick : brique
        - LivesLabel : Texte permettant d'afficher les vies
        - ScoreLabel : Texte permettant d'afficher le score
    
    """
    def __init__(self,canvas,rayon,color,width,height,speed, paddle, brick,livesLabel, scoreLabel) :
        
        #Variable pour créer la balle
        self.__canvas = canvas
        self.__color = color
        self.__rayon = rayon
        self.__width = width
        self.__height = height
        self.__x = self.__width/2
        self.__y = self.__height/2
        
        #Définission de la vitesse de la balle
        self.__angle = random.uniform(0,2*math.pi)
        self.__dX = speed*math.cos(self.__angle)
        self.__dY = speed*math.sin(self.__angle)
        
        self.__id = None
        
        #Variable avec lequelle interagit la balle
        self.__paddle = paddle
        self.__bricks = brick
        self.__life = 5
        self.__score = 0
        
        #Ajout des labels pour les mettre à jour
        self.__livesLabel = livesLabel
        self.__scoreLabel = scoreLabel
        
    def creation(self):
        """
        Permet de créer la balle
        """
        self.__id = self.__canvas.create_oval(self.__x-self.__rayon,
                                              self.__y-self.__rayon,
                                              self.__x+self.__rayon,
                                              self.__y+self.__rayon,
                                              fill= self.__color)
    
    def move(self):
        
        """
        Permet à la balle de se déplacer dans l'interface
        """
        
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
            self.__livesLabel.config(text="Lives : " + str(self.__life))
            
            if self.__life == 0:
                
                self.__canvas.create_text(self.__width/2, self.__height/2, text="Game Over", fill="red", font=("Arial", 50))
                return sh.Score_exec(self.__score)
        
        #Rebond en haut
        elif self.__y - self.__rayon + self.__dY < 0 :
            
            self.__y = 2 * self.__rayon - self.__y
            self.__dY = -self.__dY
        
        self.__x += self.__dX
        self.__y += self.__dY
        
        
        #REBOND PADDLE
        paddle_pos = self.__paddle.getPos()
        
        if paddle_pos :
            
            rx1, ry1, rx2, ry2 = paddle_pos
            
            # Rebond sur la surface supérieure de la raquette
            if (ry1 <= self.__y + self.__rayon <= ry2) and (rx1 <= self.__x <= rx2) and (self.__dY > 0):
                
                self.__y = ry1 - self.__rayon
                self.__dY = -self.__dY
                
            # Rebond sur la surface à gauche de la raquette
            elif (rx1 - self.__rayon <= self.__x <= rx1) and (ry1 <= self.__y <= ry2) and (self.__dX > 0):
                
                self.__x = rx1 - self.__rayon
                self.__dX = -self.__dX
                
            # Rebond sur la surface à droite de la raquette
            elif (rx2 <= self.__x <= rx2 + self.__rayon) and (ry1 <= self.__y <= ry2) and (self.__dX < 0):
                
                self.__x = rx2 + self.__rayon
                self.__dX = -self.__dX
                
            # Rebond sur la surface inférieure de la raquette
            elif (ry2 <= self.__y <= ry2 + self.__rayon) and (rx1 <= self.__x <= rx2) and (self.__dY < 0):
                
                self.__y = ry2 + self.__rayon
                self.__dY = -self.__dY
        
        #REBOND BRIQUES
        
        for brick in self.__bricks :
            
            brickPos = brick.getPos()

            if brickPos :
                
                bx1, by1, bx2, by2 = brickPos
                
                # Rebond sur la surface supérieure de la brique
                if (by1 <= self.__y + self.__rayon <= by2) and (bx1 <= self.__x <= bx2) and (self.__dY > 0):
                    
                    self.__y = by1 - self.__rayon
                    self.__dY = -self.__dY
                    
                    brick.destroy()
                    
                    self.__score += 10
                    self.__scoreLabel.config(text="Score : " + str(self.__score))
                    
                # Rebond sur la surface à gauche de la brique
                elif (bx1 - self.__rayon <= self.__x <= bx1) and (by1 <= self.__y <= by2) and (self.__dX > 0):
                    
                    self.__x = bx1 - self.__rayon
                    self.__dX = -self.__dX
                    
                    brick.destroy()
                    
                    self.__score += 10
                    self.__scoreLabel.config(text="Score : " + str(self.__score))
                    
                # Rebond sur la surface à droite de la brique
                elif (bx2 <= self.__x <= bx2 + self.__rayon) and (by1 <= self.__y <= by2) and (self.__dX < 0):
                    
                    self.__x = bx2 + self.__rayon
                    self.__dX = -self.__dX
                    
                    brick.destroy()
                    
                    self.__score += 10
                    self.__scoreLabel.config(text="Score : " + str(self.__score))
                    
               # Rebond sur la surface inférieure de la brique
                elif (by2 <= self.__y <= by2 + self.__rayon) and (bx1 <= self.__x <= bx2) and (self.__dY < 0):
                    
                    self.__y = by2 + self.__rayon
                    self.__dY = -self.__dY
                    
                    brick.destroy()
                    
                    self.__score += 10
                    self.__scoreLabel.config(text="Score : " + str(self.__score))

        # Récupération des coordonnées
        self.__canvas.coords(self.__id,self.__x - self.__rayon,
                                              self.__y - self.__rayon,
                                              self.__x + self.__rayon,
                                              self.__y + self.__rayon)
        
        # Vérification de la condition de victoire
        if self.__score == len(self.__bricks) * 10 :
            
            self.__canvas.create_text(self.__width/2, self.__height/2, text="You Win!", fill="green", font=("Arial", 50))
            return sh.Score_exec(self.__score)
        
        
        #Permet d'actualiser la fenêtre apres 20ms
        self.__canvas.after(20 , self.move)


    def getPos(self):
        """ 
        Permet de récupérer la coordonnées de la balle
        """
        return self.__canvas.coords(self.__id)
    
    def getLife(self):
        """
        Permet de récupérer les vies
        """
        return self.__life
    
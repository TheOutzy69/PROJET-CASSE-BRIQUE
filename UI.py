"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025 - 21/10/2025
Objectif : Créer un systéme fonctionnel pour l'interface utilisateur
"""

import tkinter as tk
from BOX import Box
from Ball import Ball
from Paddle import Paddle
import Score_Handler as sh
from BoxLife import BoxLife

class App(tk.Tk):
    """
    Classe définissant la fenêtre d'interface qui héberge le jeu.
    """
    
    def __init__(self) :
        
        super().__init__()
        
        """Initialisation de la fenêtre principale"""
        self.title("Casse-brique")
        self.geometry("1200x900+400+0") #au format 1200x900
        
        """Format du cadre de jeu"""
        self.__width = 1200
        self.__height = 800
        
        """Initialisation des variables de jeu"""
        self.__lives = 5
        self.__score = 0
        self.__highest = sh.get_highest()
        self.__average = sh.get_average()
        self.__bricks = []
        self.__bricksLife = 1

        """Création des premiers widgets"""
        self.createWidgets() 
   
    def createWidgets(self) :
        """
        Création des boutons de la fenêtre principale :
        - Bouton "Start Game" pour lancer une nouvelle partie
        - Bouton "Rules" pour afficher les règles du jeu
        - Bouton "Play Again" pour recommencer une partie
        - Bouton "Quit" pour quitter le jeu et terminer le programme.
        """
        


        self.playButton = tk.Button(text="Start Game", command= self.playGame)
        self.playButton.pack()
        
        self.playButton2 = tk.Button(text="Start BoxLife Mode", command= self.playGame2)
        self.playButton2.pack()

        self.BrickLabel = tk.Label(text="Choose the life of the bricks (Max 5) (per default at 1) :")
        self.BrickLabel.pack()

        self.entry = tk.Entry(text='Nombre de vie pour les briques (Max 5)')
        self.entry.pack()
        
        self.buttonChooseLives = tk.Button(text="Confirmer",command=self.read)
        self.buttonChooseLives.pack()

        self.rulesButton = tk.Button(text="Rules", command= self.rules_window)
        self.rulesButton.pack()
        
        self.playagain = tk.Button(text="Play Again", command= self.resetGame)
        self.playagain.config(state=tk.DISABLED)
        
        self.quitButton = tk.Button(text="Quit", command=quit)
        self.quitButton.pack(side='bottom')
        
        self.playagain.pack(side='bottom')
        
    def createLabel(self) :
        """
        Permet d'afficher les valeurs de score et vie en bas de fenêtre
        """
        self.scoreLabel = tk.Label(text="Score : "  + str(self.__score))
        self.scoreLabel.pack(side='left')
        
        self.livesLabel = tk.Label(text="Lives : "  + str(self.__lives))
        self.livesLabel.pack(side='left')

        self.HighestLabel = tk.Label(text="Highest Score: " + "\n"  + str(self.__highest))
        self.HighestLabel.pack(side='right')

        self.AvLabel = tk.Label(text="Average score \n on last 10 rounds: " + "\n" + str(self.__average))
        self.AvLabel.pack(side='right')

    def rules_window(self) :
        
        # Création d'une nouvelle fenêtre Toplevel pour afficher et expliquer les règles
        set_win = tk.Toplevel(self)
        set_win.title("Rules")
        set_win.geometry("400x300+0+0")

        label1 = tk.Label(set_win, text="Here are the rules of the game:")
        label2 = tk.Label(set_win, text="Use the left and right arrow keys to move the paddle.")
        label3 = tk.Label(set_win, text="You can also use the mouse to move the paddle.")
        label4 = tk.Label(set_win, text="Bounce the ball to break all the bricks.")
        label5 = tk.Label(set_win, text="Don't let the ball fall below the paddle.")
        label6 = tk.Label(set_win, text="You have 5 lives. Good luck!")
        
        for lbl in (label1, label2, label3, label4, label5, label6):
            lbl.pack(pady=5)

        closeButton = tk.Button(set_win, text="Close", command=set_win.destroy)
        closeButton.pack()

    def playGame(self) :
        """
        Fonction associée au bouton -Start Game-
        Programme d'affichage et exécution du jeu
        """
        #Supprimer les boutons superflux.
        self.playButton.destroy()
        self.playButton2.destroy()
        self.rulesButton.destroy()
        self.buttonChooseLives.destroy()
        self.entry.destroy()
        self.BrickLabel.destroy()
        #Activation de playgame
        self.playagain.config(state=tk.NORMAL)
        
        #Création de l'espace du jeu
        self.gamespace = tk.Canvas(self, height = self.__height, width = self.__width, bg='black')
        self.gamespace.pack()
        self.createLabel()
        
        #Création et organisation des briques
        #Ici une zone de 5*10 briques de 120*50 pixels
        for j in range(5) :
            for i in range(10) :
                Boite = Box(self.gamespace, 120*i, 50*j)
                Boite.création()
                self.__bricks.append(Boite)
                
        #Création de la raquette
        paddle = Paddle(self.gamespace, 550, 750)
        paddle.creation()
        
        #Création de la balle et lancement des déplacements. 
        ball = Ball(self.gamespace, 10, 'white', self.__width, self.__height, 10, paddle, self.__bricks,self.livesLabel,self.scoreLabel)
        ball.creation()
        ball.move()
        
        #Assignation des touches et mouvements souris.
        self.gamespace.bind_all('<KeyPress-Left>', paddle.move_left)
        self.gamespace.bind_all('<KeyPress-Right>', paddle.move_right)
        self.gamespace.bind('<Motion>', lambda event: paddle.move(event.x - ((paddle.getPos()[0] + paddle.getPos()[2]) / 2)))       
    
    def playGame2(self) :
        """
        Fonction associée au bouton -Start BoxLife Mode-
        Programme d'affichage et exécution du jeu avec les briques à vie
        Il s'agit de la même chose que playGame mais avec des utilisations de classes différentes
        pour les briques.
        Bonnes pratiques peu respéctées pour la redondance du code, mais nous souhaitions cette feature présente avant la deadline.
        """
        #Supprimer les boutons superflux.
        self.playButton.destroy()
        self.playButton2.destroy()
        self.rulesButton.destroy()
        self.buttonChooseLives.destroy()
        self.entry.destroy()
        self.BrickLabel.destroy()
        
        #Création de l'espace du jeu
        self.gamespace = tk.Canvas(self, height = self.__height, width = self.__width, bg='black')
        self.gamespace.pack()
        self.createLabel()
        
        #Création et organisation des briques
        #Ici une zone de 5*10 briques de 120*50 pixels
        
        colors = ['red','orange','yellow','green','blue']
        
        for j in range(5) :
            for i in range(10) :
                Boite = BoxLife(self.gamespace, 120*i, 50*j,self.__bricksLife,colors)
                Boite.création()
                self.__bricks.append(Boite)
                
        #Création de la raquette
        paddle = Paddle(self.gamespace, 550, 750)
        paddle.creation()
        
        #Création de la balle et lancement des déplacements. 
        ball = Ball(self.gamespace, 10, 'white', self.__width, self.__height, 10, paddle,
                    self.__bricks,self.livesLabel,self.scoreLabel)
        ball.creation()
        ball.move()
        
        #Assignation des touches et mouvements souris.
        self.gamespace.bind_all('<KeyPress-Left>', paddle.move_left)
        self.gamespace.bind_all('<KeyPress-Right>', paddle.move_right)
        self.gamespace.bind('<Motion>', lambda event: paddle.move(event.x - ((paddle.getPos()[0] + paddle.getPos()[2]) / 2)))
    
    #Fonction pour relancer le jeu
    def resetGame(self) :
        """
        Fonction associée au bouton -Play Again- 
        Réinitialise les scores et vies pour relancer le programme de jeu
        """
        self.gamespace.destroy()
        self.scoreLabel.destroy()
        self.livesLabel.destroy()
        self.HighestLabel.destroy()
        self.AvLabel.destroy()
        self.__bricks.clear()
        self.__lives = 5
        self.__score = 0
        self.__highest = sh.get_highest()
        self.__average = sh.get_average()
        self.playGame()  
        
        
        
    def read(self):
        
        """
        Cette fonction permet de lire ce qu'il y a dans Entry et d'assigner cette valeur à
        la variable associée à la vie des briques.
        """
        
        value = self.entry.get()
        
        # Convertion de la valeur en Entier
        try :
            value = int(value)
        except :
            pass
        
        # Verification de la transformation
        if isinstance(value,int):
            
            if value > 5 or value == 0:
                
                # Affichage d'un pop-up pour notifier qu'il faut que le nombre soit
                #supérieur à 5 et différent de 0
                popUp = tk.Toplevel(self)
                popUp.geometry("400x300+0+0")
                label = tk.Label(popUp, text="You can't put a number above 5 or 0 !")
                label.pack()

            else :
                
                self.__bricksLife = value
        
        else :
            
            # Affichage d'un pop-up pour notifier qu'il faut l'écrire en chiffre
            popUp = tk.Toplevel(self)
            popUp.geometry("400x300+0+0")
            label = tk.Label(popUp, text="You need to put a number !")
            label.pack()
        


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


class App(tk.Tk):
    
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
        self.__bricks = []
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
        
        self.rulesButton = tk.Button(text="Rules", command= self.rules_window)
        self.rulesButton.pack()
        
        self.playagain = tk.Button(text="Play Again", command= self.resetGame)
        
        self.quitButton = tk.Button(text="Quit", command=quit)
        
        self.quitButton.pack(side='bottom')
        self.playagain.pack(side='bottom')
        
    def createLabel(self):
        """
        Permet d'afficher les valeurs de score et vie en bas de fenêtre
        """
        self.scoreLabel = tk.Label(text="Score : " + str(self.__score))
        self.scoreLabel.pack()
        
        self.livesLabel = tk.Label(text="Lives : " + str(self.__lives))
        self.livesLabel.pack()   

    def rules_window(self):
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

    def playGame(self):
        """
        Programme d'affichage et exécution du jeu
        """
        #On supprime les boutons superflux.
        self.playButton.destroy()
        self.rulesButton.destroy()
        
        self.gamespace = tk.Canvas(self, height = self.__height, width = self.__width, bg='black')
        self.gamespace.pack()
        self.createLabel()
        
        for j in range(5):
            for i in range(10):
                Boite = Box(self.gamespace, 120*i, 50*j)
                Boite.création()
                self.__bricks.append(Boite)
        
        palet = Paddle(self.gamespace, 550, 750)
        palet.creation()
        boule = Ball(self.gamespace, 10, 'white', self.__width, self.__height, 10, palet, self.__bricks,self.livesLabel,self.scoreLabel)
        boule.creation()
        boule.move()
        
        self.gamespace.bind_all('<KeyPress-Left>', palet.move_left)
        self.gamespace.bind_all('<KeyPress-Right>', palet.move_right)
        self.gamespace.bind('<Motion>', lambda event: palet.move(event.x - ((palet.getPos()[0] + palet.getPos()[2]) / 2)))

        
                  
    def resetGame(self):
        self.gamespace.destroy()
        self.scoreLabel.destroy()
        self.livesLabel.destroy()
        self.__bricks.clear()
        self.__lives = 5
        self.__score = 0
        self.playGame()  
        
        
        

        


"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer un systéme fonctionnel pour l'interface utilisateur
"""

import tkinter as tk
from BOX import Box
from Ball import Ball
from Paddle import Paddle


class App(tk.Tk):
    
    def __init__(self) :
        
        super().__init__()
        
        self.title("Casse-brique")
        self.geometry("1200x865+200+0")

        self.__width = 1200
        self.__height = 800

        self.__lives = 5
        self.__score = 0
        self.__bricks = []
        
        self.createWidgets()
        
        
   
    def createWidgets(self) :
        
        self.playButton = tk.Button(text="Start Game", command= self.playGame)
        self.playButton.pack()
        
        self.settingsButton = tk.Button(text="Settings")
        self.settingsButton.pack()
        
        self.quitButton = tk.Button(text="Quit", command=quit)
        self.quitButton.pack(side='bottom')

    def createLabel(self):
        
        self.scoreLabel = tk.Label(text="Score : " + str(self.__score))
        self.scoreLabel.pack()
        
        self.livesLabel = tk.Label(text="Lives : " + str(self.__lives))
        self.livesLabel.pack()
    
    def update(self):
        
        self.scoreLabel.config(text="Score : " + str(self.__score))
        self.livesLabel.config(text="Lives : " + str(self.__lives))
        

    def playGame(self):
        
        self.playButton.destroy()
        self.settingsButton.destroy()
        
        self.gamespace = tk.Canvas(self, height = self.__height, width = self.__width, bg='black')
        self.gamespace.pack()
        self.createLabel()
        
        for j in range(5):
            for i in range(10):
                Boite = Box(self.gamespace, 120*i, 50*j)
                Boite.création()
                self.__bricks.append(Boite)
        
        palet = Paddle(self.gamespace, 550, 750)
        palet.création()
        
        boule2 = Ball(self.gamespace, 10, 'white', self.__width, self.__height, 10, palet, self.__bricks)
        boule2.création()
        boule2.move()

        
        self.gamespace.bind_all('<KeyPress-Left>', palet.move_left)
        self.gamespace.bind_all('<KeyPress-Right>', palet.move_right)
        
        self.gamespace.bind('<Motion>', lambda event: palet.move(event.x - ((palet.getPos()[0] + palet.getPos()[2]) / 2)))
        
        
        
        
        
        

        


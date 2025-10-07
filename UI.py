"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer un systéme fonctionnel pour l'interface utilisateur
"""

import tkinter as tk
import BOX
import Ball

class App(tk.Tk):
    
    def __init__(self) :
        
        super().__init__()
        
        self.title("Casse-brique")
        self.geometry("1200x800")
        
        self.createWidgets()
    
    def createWidgets(self) :
        
        self.playButton = tk.Button(text="Start Game", command= self.playGame)
        self.playButton.pack()
        
        self.settingsButton = tk.Button(text="Settings")
        self.settingsButton.pack()
        
        self.quitButton = tk.Button(text="Quit", command=quit)
        self.quitButton.pack(side='bottom')

    
    
    
    def playGame(self):
        #for element in self.winfo_children():
        #   element.destroy()
        #self.pack_propagate(0)
        self.playButton.destroy()
        self.settingsButton.destroy()

        self.gamespace = tk.Canvas(self, height=800, width=1200, bg='black')
        self.gamespace.pack()
        box = BOX(self.gamespace, 100, 100, 50, 50, 'red')
        box.create()
        
        
        

        


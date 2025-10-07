"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025
Objectif : Créer un systéme fonctionnel pour l'interface utilisateur
"""

import tkinter as tk


class App(tk.Tk):
    
    def __init__(self) :
        
        super().__init__()
        
        self.title("Breakout")
        self.geometry("800x600")
        
        self.createWidgets()
    
    def createWidgets(self) :
        
        self.playButton = tk.Button(text="Start Game")
        self.playButton.pack()
        
        self.settingsButton = tk.Button(text="Settings")
        self.settingsButton.pack()
        
        self.quitButton = tk.Button(text="Quit", command=quit)
        self.quitButton.pack()
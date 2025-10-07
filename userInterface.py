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
        
        self.playButton = tk.Button(text= "Start Game", width = 20, height = 2)
        self.playButton.place(relx=0.5, rely=0.4, anchor="center")
        
        self.settingsButton = tk.Button(text="Settings", width = 20, height = 2)
        self.settingsButton.place(relx=0.5, rely=0.5, anchor="center")
        
        self.quitButton = tk.Button(text="Quit", command=quit, width = 20, height = 2)
        self.quitButton.place(relx=0.5, rely=0.6, anchor="center")
          
    
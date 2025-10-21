"""
Projet : Casse-briques
Auteur : Nallet Hugo et Serveaux Tao
Date : 07/10/2025 - 21/10/2025
Objectif : Aquérir, organiser et sauvegarder les scores
"""

from datetime import datetime
import pandas as pd



class Scores:

    def __init__(self):
        self.__scores = []

    def retrieve_score(self, sent_data):
        now = datetime.now()
        self.__scores.append([now, sent_data])
     



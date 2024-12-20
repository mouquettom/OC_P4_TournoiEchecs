from random import choice
import os
import json

class Joueur:
    def __init__(self, prenom, nom, genre, date_naissance):
        self.prenom = prenom
        self.nom = nom
        self.genre = genre
        self.date_naissance = date_naissance
        self.points = 0.0

    def vainqueur_match(self):
        self.points += 1

    def match_nul(self):
        self.points += 0.5

    def __repr__(self):
        return f"{self.prenom} {self.nom} [{self.points} pts]"


class Match:
    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs

    def jouer_match(self):
        resultats = choice(["gagnant", "égalité"])
        if resultats == "gagnant":
            gagnant = choice(self.joueurs)
            gagnant.vainqueur_match()
        elif resultats == "égalité":
            for joueur in self.joueurs:
                joueur.match_nul()


class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.joueurs = []
        self.matchs = []
        self.joueurs_restants = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def ajouter_match(self, match):
        self.matchs.append(match)

    def match_making(self):
        if len(self.joueurs_restants) < 2:
            raise ValueError("Il n'y a pas assez de joueurs pour organiser un match.")

        self.joueurs_restants.sort(key=lambda joueur: joueur.points, reverse=True)
        j1, j2 = self.joueurs_restants.pop(0), self.joueurs_restants.pop(0)
        return j1, j2

    def enregister_classement(self):
        DIR_NAME = os.path.dirname(os.path.abspath(__file__))
        DIR_FILE = os.path.join(DIR_NAME, f"{self.nom} Classement")

        path = os.path.join(DIR_FILE, f"{self.nom} Classement.json")

        if not os.path.exists(DIR_FILE):
            os.makedirs(DIR_FILE)

        # Extraire les informations des joueurs sous forme de dictionnaire
        classement = sorted(self.joueurs, key=lambda joueur: joueur.points, reverse=True)

        # Convertir les objets Joueur en dictionnaires
        classement_dico = [
            {
                "position": i + 1,
                "nom": joueur.nom,
                "prenom": joueur.prenom,
                "points": joueur.points
            }
            for i, joueur in enumerate(classement)
        ]

        # Enregistrer dans un fichier JSON
        try:
            with open(path, 'w', encoding='utf-8') as file:
                json.dump(classement_dico, file, indent=4, ensure_ascii=False)
            print(f"\nLe classement a été enregistré dans : {path}.")
        except IOError as e:
            print(f"Erreur lors de l'écriture dans le fichier : {e}")
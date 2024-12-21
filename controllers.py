from models import Joueur, Match, Tournoi
from views import TournoiView
from random import shuffle

class TournoiController:
    def __init__(self):
        self.tournoi = None

    def creer_tournoi(self):
        nom, lieu, date_debut, date_fin = TournoiView.demander_info_tournoi()

        self.tournoi = Tournoi(nom, lieu, date_debut, date_fin)
        print(f"Le Tournoi '{self.tournoi.nom}' a bien été créé.")

    def ajouter_joueurs(self):
        while True:
            choix = ""

            while choix not in ["Y", "N"]:
                choix = input("\nSouhaitez-vous ajouter un joueur (Y/N) ? ")
            if choix == "Y":
                prenom, nom, genre, date_naissance = TournoiView.demander_info_joueur()
                confirmation = ""
                while confirmation not in ["Y", "N"]:
                    confirmation = input("\nConfirmez-vous l'ajout de ce nouveau joueur (Y/N) ? ")
                if confirmation == "Y":
                    joueur = Joueur(prenom, nom, genre, date_naissance)
                    self.tournoi.ajouter_joueur(joueur)
                    print(f"\n{joueur.prenom} a bien été ajouté à la liste des joueurs du Tournoi.")
                elif confirmation == "N":
                    print("Saisie annulée.")
                    continue
            else:
                break

    def jouer_tournoi(self):
        shuffle(self.tournoi.joueurs)
        nb_tours = ""
        while not nb_tours.isdigit():
            nb_tours = input("\nVeuillez indiquer le nombre de tours ? ")

        nb_tours = int(nb_tours)
        for _ in range(nb_tours):
            self.tournoi.joueurs_restants = self.tournoi.joueurs.copy()
            while len(self.tournoi.joueurs_restants) >= 2:
                j1, j2 = self.tournoi.match_making()
                TournoiView.afficher_match(j1, j2)
                match = Match(f"Match {len(self.tournoi.matchs) + 1}", [j1, j2])
                match.jouer_match()
                TournoiView.afficher_resultats_match(match.joueurs)
                self.tournoi.ajouter_match(match)

        # Appel de la méthode pour enregistrer le classement à la fin du tournoi
        self.tournoi.enregister_classement()

    def afficher_classement(self):
        self.tournoi.joueurs.sort(key=lambda joueur: joueur.points, reverse=True)
        TournoiView.afficher_classement(self.tournoi.joueurs)

    def rapport_joueurs(self):
        joueurs = self.tournoi.joueurs_par_ordre_alphabetique()
        TournoiView.afficher_joueurs(joueurs)

    def rapport_tournois(self, tournois):
        TournoiView.afficher_tournois(tournois)

    def rapport_details_tournoi(self):
        TournoiView.afficher_details_tournoi(self.tournoi)
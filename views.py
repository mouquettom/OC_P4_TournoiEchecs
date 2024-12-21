from datetime import datetime

class TournoiView:
    @staticmethod
    def afficher_classement(joueurs):
        print("\nClassement final :\n")
        for index, joueur in enumerate(joueurs, start=1):
            print(f"{index}. {joueur}")

    @staticmethod
    def afficher_match(j1, j2):
        print(f"\n{j1} va affronter {j2}.\n")

    @staticmethod
    def afficher_resultats_match(joueurs):
        for joueur in joueurs:
            print(f" - {joueur.prenom} {joueur.nom} [{joueur.points} pts]")

    @staticmethod
    def demander_date_valide(message):
        while True:
            date = input(message)
            try:
                date_obj = datetime.strptime(date, "%d/%m/%Y")
                return date_obj
            except ValueError:
                print("Date invalide. Veuillez entrer une date au format JJ/MM/AAAA.")

    @staticmethod
    def demander_info_tournoi():
        nom = input("\nLe nom du Tournoi : ")
        lieu = input("Le lieu du Tournoi : ")
        date_debut = TournoiView.demander_date_valide("La date de début (JJ/MM/AAAA) : ")
        date_fin = TournoiView.demander_date_valide("La date de fin (JJ/MM/AAAA) : ")
        return nom, lieu, date_debut, date_fin

    @staticmethod
    def demander_info_joueur():
        prenom = input("\nQuel est le prénom du joueur : ")
        nom = input("Quel est le nom de famille du joueur : ")
        genre = input("Quel est le genre du joueur (H/F) : ")
        date_naissance = TournoiView.demander_date_valide("Quelle est la date de naissance du joueur (JJ/MM/AAAA) : ")
        return prenom, nom, genre, date_naissance

    @staticmethod
    def afficher_joueurs(joueurs):
        print("\nListe des joueurs (ordre alphabétique) :")
        for joueur in joueurs:
            print(f"- {joueur.nom} {joueur.prenom}")

    @staticmethod
    def afficher_tournois(tournois):
        print("\nListe des tournois :")
        for tournoi in tournois:
            print(f"- {tournoi.nom}")

    @staticmethod
    def afficher_details_tournoi(tournoi):
        print(f"\nDétails du tournoi : {tournoi.details_tournoi()}")

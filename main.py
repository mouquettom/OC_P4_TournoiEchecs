from controllers import TournoiController

if __name__ == "__main__":
    print("\n*** TOURNOI INTERNATIONAL D'ECHECS ***\n")
    controller = TournoiController()
    controller.creer_tournoi()
    controller.ajouter_joueurs()
    controller.jouer_tournoi()
    controller.afficher_classement()
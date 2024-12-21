from controllers import TournoiController

if __name__ == "__main__":
    print("\n*** TOURNOI INTERNATIONAL D'ECHECS ***")

    def menu_principal():
        controller = TournoiController()
        tournois = []  # Liste pour stocker tous les tournois

        while True:
            print("\nMenu principal :\n")
            print("1. Créer un tournoi")
            print("2. Ajouter des joueurs")
            print("3. Jouer le tournoi")
            print("4. Afficher classement")
            print("5. Voir rapports")
            print("6. Quitter")

            choix = input("\nChoisissez une option : ")

            if choix == "1":
                controller.creer_tournoi()
                tournois.append(controller.tournoi)
            elif choix == "2":
                if controller.tournoi:
                    controller.ajouter_joueurs()
                else:
                    print("\nAucun tournoi n'a été créé. Veuillez d'abord créer un tournoi.")
            elif choix == "3":
                if controller.tournoi:
                    controller.jouer_tournoi()
                else:
                    print("\nAucun tournoi n'a été créé. Veuillez d'abord créer un tournoi.")
            elif choix == "4":
                if controller.tournoi:
                    controller.afficher_classement()
                else:
                    print("\nAucun tournoi n'a été créé. Veuillez d'abord créer un tournoi.")
            elif choix == "5":
                if controller.tournoi:
                    print("\nRapports disponibles :")
                    print("1. Liste de tous les joueurs (ordre alphabétique)")
                    print("2. Liste de tous les tournois")
                    print("3. Détails d'un tournoi")

                    sous_choix = input("Choisissez une option : ")
                    if sous_choix == "1":
                        controller.rapport_joueurs()
                    elif sous_choix == "2":
                        controller.rapport_tournois(tournois)
                    elif sous_choix == "3":
                        controller.rapport_details_tournoi()
                    else:
                        print("Option invalide.")
                else:
                    print("\nAucun tournoi n'a été créé. Veuillez d'abord créer un tournoi.")
            elif choix == "6":
                print("Au revoir !")
                break
            else:
                print("Option invalide, veuillez réessayer.")


    menu_principal()

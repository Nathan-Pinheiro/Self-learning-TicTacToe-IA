import os
import TTTGame.TicTacToe as TTT
import TTTGame.TicTacToePlayer as TTTPlayer

#----------------------------------------
#Affiche le menu numéro 1
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : aucune
#
#Sortie : affichage
#----------------------------------------
def __afficher_menu():

    os.system("cls")
    print("---------------------")
    print("     Bienvenue !     ")
    print("                     ")
    print("  1 - Jouer          ")
    print("  2 - Règles         ")
    print("  3 - Quitter        ")
    print("                     ")
    print("---------------------")


#----------------------------------------
#Affiche le menu numéro 1
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : aucune
#
#Sortie : affichage
#----------------------------------------
def __afficher_menu_bots():

    os.system("cls")
    print("------------------------")
    print("     Bienvenue !        ")
    print("                        ")
    print("  1 - Entrainer IA      ")
    print("  2 - Jouer contre l'IA ")
    print("  3 - Quitter           ")
    print("                        ")
    print("------------------------")


#----------------------------------------
#Affiche les règles d'un jeu
#
#private : variable accessible uniquement dans le script actuel
#
#Entrée : str (le nom du jeu souhaité)
#
#Sortie : affichage
#----------------------------------------
def __afficher_regles():

    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)
    O  = '\033[93m' # yellow
    P  = '\033[95m' # purple
    N  = '\033[90m' # noir

    os.system("cls")
    print("---------------------")
    print(O + "Règles : " + W)
    print("---------------------")
    print("La partie se déroule dans un tableau de 3 x 3")
    print("")
    print(N + "(Le joueur qui démarre est défini aléatoirement)" + W)
    print("")
    print("Le " + B + "joueur 1" + W + " choisit de mettre son " + P + "symbole de couleur" + W + " dans la case qu'il désire")
    print("")
    print("Le " + R + "joueur 2" + W + " choisit de à son tour de mettre son " + P + "symbole de couleur" + W + " dans la case qu'il désire")
    print()
    print("Et ainsi de suite " + P + "jusqu’à obtenir une rangée de 3 symbole de même couleur dans toutes les directions possible" + W)
    print()
    print(P + "Le joueur qui possède les 3 jetons alignés gagne la partie" + W)
    print("---------------------")
    os.system("pause")

if __name__ == "__main__":

    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)

    os.system("cls")

    najarala = TTTPlayer.Najarala()
    
    while True :

        __afficher_menu()

        choice = str(input("Choisissez le jeu : "))

        match choice:

            case "1":
                while True :
                    __afficher_menu_bots()

                    choice = str(input("Choisissez le jeu : "))

                    match choice:

                        case "1":
                            TTT.trainAI(najarala, TTTPlayer.RandomTrainer())

                        case "2":
                            najarala.model.train(TTTPlayer.RandomTrainer(), 10, 500)

                        case "3":
                            break

                        case other:
                            print("Réponse inconnue")
                            os.system("pause")
            case "2":
                __afficher_regles()

            case "3":
                break

            case other:
                print("Réponse inconnue")
                os.system("pause")

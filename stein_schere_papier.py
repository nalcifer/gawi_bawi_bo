#REGLES DU JEU
#L'utilisateur choisis le nombre de manches voulues.
#Le jeu commence : L'utilisateur choisis entre pierre, feuille et ciseaux.
#Il y a égalité lorsque l’utilisateur et l’ordinateur font le même choix.
#la pierre gagne sur les ciseaux et perd contre la feuille
#la feuille gagne sur la pierre et perd contre les ciseaux
#les ciseaux gagnent sur la feuille et perdent contre la pierre

from random import randint
options = ["PIERRE", "PAPIER", "CISEAUX"]


def joueurVSbot ():
    Pointsjoueur1 = 0
    Pointsjoueur2 = 0
    tour = 0
    continuer = True
    while (continuer):
        bot = options[randint(0,2)]
        joueur = input("Pierre, Feuille, Ciseaux? ou tapez Fin pour arrêter le jeu!\n")

        if (joueur.upper() == 'FIN') :
            continuer = False
        elif (joueur.upper() == 'PUIT') :
            print ("On a dit pierre, feuille ou ciseaux. Dommage le bot gagne 1 point")
            Pointsjoueur2 = Pointsjoueur2 + 1
        elif(joueur.upper() == bot):
            print("Joueur et bot ont joué", bot, ".Egalité!")
        elif(joueur.upper() == "PIERRE"):
                if(bot == "PAPIER"):
                    print("Perdu!", bot, "recouvre", joueur)
                    Pointsjoueur2 = Pointsjoueur2 + 1 
                else:
                    print("Gagné!", joueur, "écrase", bot)
                    Pointsjoueur1 = Pointsjoueur1 + 1
        elif(joueur.upper() == "FEUILLE"):
                if(bot == "CISEAUX"):
                    print("Perdu!", bot, "coupe", joueur)
                    Pointsjoueur2 = Pointsjoueur2 + 1 
                else:
                    print("Gagné!", joueur, "recouvre", bot)
                    Pointsjoueur1 = Pointsjoueur1 + 1
        elif(joueur.upper() == "CISEAUX"):
                if(bot == "PIERRE"):
                    print("Perdu!", bot, "écrase", joueur)
                    Pointsjoueur2 = Pointsjoueur2 + 1 
                else:
                    print("Gagné!", joueur, "coupe", bot)
                    Pointsjoueur1 = Pointsjoueur1 + 1
        else:
            print("Votre choix n'est pas correct, vérifiez l'orthographe!")
        tour=tour+1
        print("Tour n°",tour,"fini\n")
    return (Pointsjoueur1, Pointsjoueur2)

def joueurVSjoueur () :
    Pointsjoueur1 = 0
    Pointsjoueur2 = 0
    tour = 0
    continuer = True
    namejoueur1 = input("Entrez nom joueur 1 :")
    namejoueur2 = input("Entrez nom joueur 2 :")
    while (continuer):
        joueur1 = input(namejoueur1 + " choisissez : Pierre, Feuille ou Ciseaux? ou tapez Fin pour arrêter le jeu!\n")
        joueur2 = input(namejoueur2 +" choisissez : Pierre, Feuille ou Ciseaux? ou tapez Fin pour arrêter le jeu!\n")

        if (joueur1.upper()== 'FIN' or joueur2.upper()== 'FIN') :
            continuer = False
        elif (joueur1.upper() == 'PUIT') :
            print ("On a dit pierre, feuille ou ciseaux. 1 point de plus pour",namejoueur2)
            Pointsjoueur2 = Pointsjoueur2 + 1
        elif (joueur2.upper() == 'PUIT') :
            print ("On a dit pierre, feuille ou ciseaux. 1 point de plus pour",namejoueur1)
            Pointsjoueur1 = Pointsjoueur1 + 1
        elif(joueur1.upper() == joueur2.upper()):
            print("Joueur1 et joueur2 ont joué", joueur2, ".Egalité!")
        elif(joueur1.upper() == "PIERRE"):
                if(joueur2.upper() == "PAPIER"):
                    print(namejoueur2,"à gagné", joueur2, "recouvre", joueur1)
                    Pointsjoueur2 = Pointsjoueur2 + 1 
                else:
                    print(namejoueur1,"à gagné!", joueur1, "écrase", joueur2)
                    Pointsjoueur1 = Pointsjoueur1 + 1
        elif(joueur1.upper() == "FEUILLE"):
                if(joueur2.upper() == "CISEAUX"):
                    print(namejoueur2,"à gagné", joueur2, "coupe", joueur1)
                    Pointsjoueur2 = Pointsjoueur2 + 1 
                else:
                    print(namejoueur1,"à gagné!", joueur1, "recouvre", joueur2)
                    Pointsjoueur1 = Pointsjoueur1 + 1
        elif(joueur1.upper() == "CISEAUX"):
                if(joueur2.upper() == "PIERRE"):
                    print(namejoueur2,"à gagné", joueur2, "écrase", joueur1)
                    Pointsjoueur2 = Pointsjoueur2 + 1 
                else:
                    print(namejoueur1,"à gagné!", joueur1, "coupe", joueur2)
                    Pointsjoueur1 = Pointsjoueur1 + 1
        else:
            print("Votre choix n'est pas correct, vérifiez l'orthographe!")
        tour=tour+1
        print("Tour n°",tour,"fini\n")
    return (Pointsjoueur1, Pointsjoueur2, namejoueur1, namejoueur2)



mode = input("Choisissez un mode : 1=joueurVSbot ou 2=joueurVSjoueur. \n")
if mode == "1" :
    Pointsjoueur1, Pointsjoueur2 = joueurVSbot()
    print("Le joueur à obtenue: ", Pointsjoueur1, "points. Le bot à obtenue:", Pointsjoueur2, "points.\n" )
    if Pointsjoueur1 > Pointsjoueur2 :
        print("BRAVO! Le gagnant est le joueur.")
    elif Pointsjoueur1 < Pointsjoueur2 :
        print("PERDU! Le gagnant est le bot.") 
    else :
        print("Il y a égalité, rejouez pour vous départager")
elif mode == "2" :
    Pointsjoueur1, Pointsjoueur2, namejoueur1, namejoueur2 = joueurVSjoueur()
    print(namejoueur1," à obtenue: ", Pointsjoueur1, "points. ",namejoueur2," à obtenue:", Pointsjoueur2, "points.\n" )
    if Pointsjoueur1 > Pointsjoueur2 :
        print("Le gagnant est",namejoueur1,". Bravo!")
    elif Pointsjoueur1 < Pointsjoueur2 :
        print("Le gagnant est",namejoueur2,". Bravo!")
    else :
        print("Il y a égalité, rejouez pour vous départager")

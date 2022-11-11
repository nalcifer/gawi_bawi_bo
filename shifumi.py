#DEBUT

#afficher "REGLES DU JEU"
#L'utilisateur choisis le nombre de manches voulues.
#Le jeu commence : L'utilisateur choisis entre pierre, feuille et ciseaux.
#Il y a égalité lorsque l’utilisateur et l’ordinateur font le même choix.
#la pierre gagne sur les ciseaux et perd contre la feuille
#la feuille gagne sur la pierre et perd contre les ciseaux
#les ciseaux gagnent sur la feuille et perdent contre la pierre

#on admet une fonction input qui permet à un joueur d'entrer une valeur
#importer la fonction randint du module random (qui permet de générer des nombres aléatoires)
from random import randint
#initialiser la liste "options" et lui attribuer les 3 chaines de caractere "PIERRE", "PAPIER" et "CISEAUX"
options = ["PIERRE", "PAPIER", "CISEAUX"]

#attribuer 0 à Pointsjoueur
Pointsjoueur = 0
#attribuer 0 à Pointsordi
Pointsordi = 0

#initialiser tour en lui atribuant la valeur 0
tour = 0
#initialiser continuer comme vrai
continuer = True
#tant que continuer est vrai
while (continuer):
    #assigner à bot la valeur de la liste "options" à l'index retourné aléatoirement par l'execution de la fonction randint avec comme parametres 0 et 2
    bot = options[randint(0,2)]
    #attribuer à joueur le retour de l'execution de la fonction input avec comme texte "Pierre, Feuille, Ciseaux? ou tapez Fin pour arrêter le jeu!" et sauter une ligne
    joueur = input("Pierre, Feuille, Ciseaux? ou tapez Fin pour arrêter le jeu!\n")

    #si la chaine de caractere "joueur" renvoyé en majuscules est égale à "FIN" 
    if (joueur.upper() == 'FIN') :
        #alors attribuer à continuer la valeur False
        continuer = False
    #sinon si la chaine de caractere "joueur" renvoyé en majuscules est égale à "PUIT"
    elif (joueur.upper() == 'PUIT') :
        #alors afficher "On a dit pierre, feuille ou ciseaux. Dommage le bot gagne 1 point"
        print ("On a dit pierre, feuille ou ciseaux. Dommage le bot gagne 1 point")
        #et incrementer Pointsordi de 1 
        Pointsordi = Pointsordi + 1
    #sinon si la chaine de caractere dans joueur renvoyée en majuscules est égale à bot 
    elif(joueur.upper() == bot):
        #alors afficher la concatenation de "Joueur et bot ont joué", le retour de l'execution de la fonction string de bot et ".Egalité!"
        print("Joueur et bot ont joué", bot, ".Egalité!")
    #sinon si la chaine de caractere dans joueur renvoyée en majuscules est égale à "PIERRE"
    elif(joueur.upper() == "PIERRE"):
            #alors si bot à pour valeur "PAPIER"
            if(bot == "PAPIER"):
                #alors afficher la concaténation de "Perdu!", bot, "recouvre", joueur
                print("Perdu!", bot, "recouvre", joueur)
                #et incrementer Pointsordi de 1 
                Pointsordi = Pointsordi + 1 
            #sinon
            else:
                #alors afficher la concaténation de "Gagné!", joueur, "écrase", bot
                print("Gagné!", joueur, "écrase", bot)
                #et incrementer Pointsjoueur de 1 
                Pointsjoueur = Pointsjoueur + 1
    #sinon si la chaine de caractere dans joueur renvoyée en majuscules est égale à "FEUILLE"
    elif(joueur.upper() == "FEUILLE"):
            #alors si bot est égal à "CISEAUX"
            if(bot == "CISEAUX"):
                #alors afficher la concaténation de "Perdu!", bot, "coupe", joueur
                print("Perdu!", bot, "coupe", joueur)
                #et incrementer Pointsordi de 1 
                Pointsordi = Pointsordi + 1 
            #sinon
            else:
                #alors afficher la concaténation de "Gagné!", joueur, "recouvre", bot
                print("Gagné!", joueur, "recouvre", bot)
                #et incrementer Pointsjoueur de 1 
                Pointsjoueur = Pointsjoueur + 1
    #sinon si la chaine de caractere dans joueur renvoyée en majuscules est égale à "CISEAUX"
    elif(joueur.upper() == "CISEAUX"):
            #alors si bot à pour valeur pierre
            if(bot == "PIERRE"):
                #alors afficher la concaténation de "Perdu!", bot, "écrase", joueur
                print("Perdu!", bot, "écrase", joueur)
                #et incrementer Pointsordi de 1 
                Pointsordi = Pointsordi + 1 
            #sinon
            else:
                #alors afficher la concatenation de "Gagné!", joueur, "coupe" et bot
                print("Gagné!", joueur, "coupe", bot)
                #et incrementer Pointsjoueur de 1 
                Pointsjoueur = Pointsjoueur + 1
    #sinon
    else:
        #alors afficher "Votre choix n'est pas correct, vérifiez l'orthographe!"
        print("Votre choix n'est pas correct, vérifiez l'orthographe!")
    #incrémenter tour de 1
    tour=tour+1
    #afficher la concatenation de "Tour n°", tour et "fini" et sauter une ligne
    print("Tour n°",tour,"fini\n")

#afficher la concatenation de "Le joueur à obtenue: ", Pointsjoueur, "points. Le bot à obtenue:", Pointsordi, "points."
#et sauter une ligne
print("Le joueur à obtenue: ", Pointsjoueur, "points. Le bot à obtenue:", Pointsordi, "points.\n" )
#si Pointsjoueur est supérieur à Pointsordi
if Pointsjoueur > Pointsordi :
    #alors afficher "BRAVO! Le gagnant est le joueur."
    print("BRAVO! Le gagnant est le joueur.")
#sinon si Pointsjoueur est inférieur à Pointsordi
elif Pointsjoueur < Pointsordi :
    #alors afficher "PERDU! Le gagnant est le bot."
    print("PERDU! Le gagnant est le bot.") 
#sinon
else :
    #alors afficher "Il y a égalité, rejouez pour vous départager"
    print("Il y a égalité, rejouez pour vous départager")

#FIN

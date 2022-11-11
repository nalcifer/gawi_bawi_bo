#DEBUT

#on admet une fonction input qui permet à un joueur d'entrer une valeur
#importer la fonction randint du module random (qui permet de générer des nombres aléatoires)

#afficher "REGLES DU JEU"
#L'utilisateur choisis le nombre de manches voulues.
#Le jeu commence : L'utilisateur choisis entre pierre, feuille et ciseaux.
#Il y a égalité lorsque l’utilisateur et l’ordinateur font le même choix.
#la pierre gagne sur les ciseaux et perd contre la feuille
#la feuille gagne sur la pierre et perd contre les ciseaux
#les ciseaux gagnent sur la feuille et perdent contre la pierre

#initialiser la liste "options" et lui attribuer les 3 chaines de caractere "PIERRE", "PAPIER" et "CISEAUX"

#attribuer 0 à Pointsjoueur
#attribuer 0 à Pointsordi
#initialiser tour en lui atribuant la valeur 0
#initialiser continuer comme vrai

#tant que continuer est vrai
    #assigner à bot la valeur de la liste "options" à l'index retourné aléatoirement par l'execution de la fonction randint avec comme parametres 0 et 2
    #attribuer à joueur le retour de l'execution de la fonction input avec comme texte "Pierre, Feuille, Ciseaux? ou tapez Fin pour arrêter le jeu!" et sauter une ligne

    #si la chaine de caractere "joueur" renvoyé en majuscules est égale à "FIN" 
        #alors attribuer à continuer la valeur False

    #sinon si la chaine de caractere "joueur" renvoyé en majuscules est égale à "PUIT"
        #alors afficher "On a dit pierre, feuille ou ciseaux. Dommage le bot gagne 1 point"
        #et incrementer Pointsordi de 1

    #sinon si la chaine de caractere dans joueur renvoyée en majuscules est égale à bot 
        #alors afficher la concatenation de "Joueur et bot ont joué", le retour de l'execution de la fonction string de bot et ".Egalité!"
    
    #sinon si la chaine de caractere dans joueur renvoyée en majuscules est égale à "PIERRE"
            #alors si bot à pour valeur "PAPIER"
                #alors afficher la concaténation de "Perdu!", bot, "recouvre", joueur
                #et incrementer Pointsordi de 1 
            #sinon
                #alors afficher la concaténation de "Gagné!", joueur, "écrase", bot
                #et incrementer Pointsjoueur de 1

    #sinon si la chaine de caractere dans joueur renvoyée en majuscules est égale à "FEUILLE"
            #alors si bot est égal à "CISEAUX"
                #alors afficher la concaténation de "Perdu!", bot, "coupe", joueur
                #et incrementer Pointsordi de 1 
            #sinon
                #alors afficher la concaténation de "Gagné!", joueur, "recouvre", bot
                #et incrementer Pointsjoueur de 1

    #sinon si la chaine de caractere dans joueur renvoyée en majuscules est égale à "CISEAUX"
            #alors si bot à pour valeur pierre
                #alors afficher la concaténation de "Perdu!", bot, "écrase", joueur
                #et incrementer Pointsordi de 1 
            #sinon
                #alors afficher la concatenation de "Gagné!", joueur, "coupe" et bot
                #et incrementer Pointsjoueur de 1

    #sinon
        #alors afficher "Votre choix n'est pas correct, vérifiez l'orthographe!"
    #incrémenter tour de 1
    #afficher la concatenation de "Tour n°", tour et "fini" et sauter une ligne

#afficher la concatenation de "Le joueur à obtenue: ", Pointsjoueur, "points. Le bot à obtenue:", Pointsordi, "points."
#et sauter une ligne

#si Pointsjoueur est supérieur à Pointsordi
    #alors afficher "BRAVO! Le gagnant est le joueur."

#sinon si Pointsjoueur est inférieur à Pointsordi
    #alors afficher "PERDU! Le gagnant est le bot."

#sinon
    #alors afficher "Il y a égalité, rejouez pour vous départager"

#FIN

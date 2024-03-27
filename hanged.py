# coding : utf-8

# pendu.py

from dessins import *
import random

MAX_CHANCES = 10

class Pendu:
    def __init__(self):
        self.mot_a_deviner = self.choisir_mot()
        self.mot_trouve = ['_' for _ in self.mot_a_deviner]
        self.lettres_deja_devinees = []
        self.nb_erreurs = 0

    def choisir_mot(self):
        # Code pour choisir un mot aléatoire à partir d'un fichier de dictionnaire
        with open('dictionnaire.txt', 'r') as f:
            mots = f.readlines()
        return random.choice(mots).strip().lower()

    def deviner_lettre(self, lettre):
        # Code pour vérifier si la lettre est dans le mot et mettre à jour le mot trouvé
        lettre = lettre.lower()
        if lettre in self.lettres_deja_devinees:
            print("Vous avez déjà deviné cette lettre. Essayez-en une autre.")
            return
        self.lettres_deja_devinees.append(lettre)

        if lettre in self.mot_a_deviner:
            print("Bon choix ! La lettre {} est dans le mot.".format(lettre))
            for i, char in enumerate(self.mot_a_deviner):
                if char == lettre:
                    self.mot_trouve[i] = lettre # Mettre à jour le mot trouvé avec la lettre devinée
        else:
            print("La lettre '{}' n'est pas dans le mot. Essaie encore.".format(lettre))
            self.nb_erreurs += 1
        
        # Afficher le mot trouvé avec les lettres devinées jusqu'à présent
        print("Mot actuel :", ' '.join(self.mot_trouve))
        print(DESSINS_PENDU[self.nb_erreurs])

    def verifier_victoire(self):
        # Code pour vérifier si le joueur a deviné correctement le mot
        if '_' not in self.mot_trouve:
            return True
        return False

    def verifier_defaite(self):
        # Code pour vérifier si le joueur a perdu toutes ses chances
        if self.nb_erreurs >= MAX_CHANCES:
            return True
        return False

    def jouer(self):
        # Code pour démarrer le jeu et gérer les tours du joueur
        print("Bienvenue dans le jeu du Pendu !")
        print("Devinez le mot en essayant de trouver une lettre à chaque tour.")
        print("Vous avez {} chances pour deviner le mot.".format(MAX_CHANCES))
        print("Mot à deviner :", ' '.join(self.mot_trouve))

        while True:
            lettre = input("Entrez une lettre : ")
            self.deviner_lettre(lettre)
            
            if self.verifier_victoire():
                print("Félicitations ! Vous avez trouvé le mot '{}' !".format(self.mot_a_deviner))
                break
            elif self.verifier_defaite():
                print("Dommage ! Vous avez épuisé toutes vos chances.")
                print("Le mot était '{}'.".format(self.mot_a_deviner))
                break

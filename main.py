"""
Rayna Sillini
TP3
Combat des Monstres
"""
import random

niveau_vie = 20
force_adversaire = random.randint(1, 5)
numero_adversaire = 0
nombre_victoires = 0
nombre_defaites = 0

boucle_jeu = True
while boucle_jeu:
    print("Vous tombez face à face avec un adversaire de difficulté",force_adversaire,)
    choix = int(input("Que voulez-vous faire?\n" 
	"1- Combattre cet adversaire \n"
	"2- Contourner cet adversaire et aller ouvrir une autre porte \n"
	"3- Afficher les règles du jeu \n"
	"4- Quitter la partie \n"))
    if choix == 1:
        dice = random.randint(1, 6)
        numero_adversaire = numero_adversaire + 1;
        print("Adversaire:", numero_adversaire, "\n"
              "Force de l'adversaire", force_adversaire, "\n"
              "Niveau de vie de l'usager:", niveau_vie, "\n"
              "Combat", numero_adversaire, "\n"
              ":", nombre_victoires, "vs", nombre_defaites,)
        if dice <= 4:
            print("Vous avez perdu")
            niveau_vie = niveau_vie - 4;
            nombre_defaites = nombre_defaites + 1
        if dice >= 5:
            print("Vous avez gagner")
            niveau_vie = niveau_vie + 4;
            nombre_victoires = nombre_victoires + 1



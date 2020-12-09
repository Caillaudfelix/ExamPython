mot1="boulet"
mot2="plante"
mot3="ramene"
mot4="pecher"
mot5="renard"
mot6="orange"
mot7="citron"
mot8="lettre"
mot9="wagons"
mot10="entrer"
from colorama import init
init()
from colorama import Fore, Back
mot_mystere=mot5
tour=1
tableau_base=["_","_","_","_","_","_"]
tableau_mm=["renard"]
tableau_joueur=[""]
print(tableau_base)
guess=input("Quel est votre choix ?")
for x in range(1):
    nbrLettres=len(guess)
    if(nbrLettres!=6):
        print("Votre mot ne compte pas 6 lettres !")
        continue
    else:
        tableau_joueur[x]=guess
        print(tableau_joueur)
        print(tableau_base)
        tour+=1
        continue

def perdu(guess):
    if(tour==8) and (guess!=mot_mystere):
        print("Vous avez perdu !")
    return

def victoire(guess):
    if(guess==mot_mystere):
        print("Vous avez gagné !")
    return
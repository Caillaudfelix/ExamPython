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
tableau_mm=["r","e","n","a","r","d",]
tableau_joueur=[" "]

def perdu(tableau_joueur,tableau_mm):
    for i in range(1,7):
        if(tour==8):
            print("Vous avez perdu !")
    return

def victoire(tableau_joueur,tableau_mm):
    for i in range(1,7):
        if(tableau_joueur[1] and tableau_joueur[2] and tableau_joueur[3] and tableau_joueur[4] and tableau_joueur[5] and tableau_joueur[6] == tableau_mm[1] and tableau_mm[2] and tableau_mm[3] and tableau_mm[4] and tableau_mm[5] and tableau_mm[6]):
            print("Vous avez gagné !")
    return

def recommencer(tableau_joueur,tableau_mm):
	for i in range(1,7):
		if(tableau_joueur[1] or tableau_joueur[2] or tableau_joueur[3] or tableau_joueur[4] or tableau_joueur[5] or tableau_joueur[6] != tableau_mm[1] or tableau_mm[2] or tableau_mm[3] or tableau_mm[4] or tableau_mm[5] or tableau_mm[6]):
			print("Votre mot ne correspond pas au mot mystère !")
	return

def mauvaiseLettre1(tableau_joueur,tableau_mm):
	for i in range(1,7):
		if(tableau_joueur[1] != tableau_mm[1]):
			print(tableau_joueur)
			print(back.BLUE+tableau_joueur[1])
	return

def mauvaiseLettre2(tableau_joueur,tableau_mm):
	for i in range(1,7):
		if(tableau_joueur[2] != tableau_mm[2]):
			print(tableau_joueur)
			print(back.BLUE+tableau_joueur[2])
	return

def mauvaiseLettre3(tableau_joueur,tableau_mm):
	for i in range(1,7):
		if(tableau_joueur[3] != tableau_mm[3]):
			print(tableau_joueur)
			print(back.BLUE+tableau_joueur[3])
	return

def mauvaiseLettre4(tableau_joueur,tableau_mm):
	for i in range(1,7):
		if(tableau_joueur[4] != tableau_mm[4]):
			print(tableau_joueur)
			print(back.BLUE+tableau_joueur[4])
	return

def mauvaiseLettre5(tableau_joueur,tableau_mm):
	for i in range(1,7):
		if(tableau_joueur[5] != tableau_mm[5]):
			print(tableau_joueur)
			print(back.BLUE+tableau_joueur[5])
	return

def mauvaiseLettre6(tableau_joueur,tableau_mm):
	for i in range(1,7):
		if(tableau_joueur[6] != tableau_mm[6]):
			print(tableau_joueur)
			print(back.BLUE+tableau_joueur[6])
	return


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
	

input()
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
mot_mystere=mot5
tour=1
tableau=[" "," "," "," "," "," "]
tableau_mm=["renard"]
tableau_joueur=[""]
print(tableau)
guess=input("Quel est votre choix ?")
for x in range(1):
    nbrLettres=len(guess)
    if(nbrLettres!=6):
        print("Votre mot ne compte pas 6 lettres !")
        tour=tour
        continue
    else:
        tableau_joueur[x]=guess
        print(tableau_joueur)
        continue

def perdu(tableau_joueur):
    if(tour==8) and (guess!=mot_mystere):
        print("Vous avez perdu !")
    return

def victoire(tableau_joueur):
    if(guess==mot_mystere):
        print("Vous avez gagné !")
    return

input()
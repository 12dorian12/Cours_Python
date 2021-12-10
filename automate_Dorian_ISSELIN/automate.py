#Header
"""
definit la fonction verif_phrase qui 
Dorian ISSELIN
26/11/21
fini
"""

"""
//////////////////////////////////////////////////////creation du dictoinaire entrée -> valeur/////////////////////////////////////////////////////////
"""

#0 article
#1 adjectif
#2 nom
#3 verbe
#4 nom propre
#5 point

#on ecrit un mot par ligne 
#on fait suivre le mot par un espave est ca valeur
dictionnaire = {}
for ligne in open(__file__[0:-11]+"dictionaire", "r").readlines():
    ligne = ligne.split()
    dictionnaire[ligne[0]] = eval(ligne[1])

"""
//////////////////////////////////////////////////////creation de la table de transition/////////////////////////////////////////////////////////
"""

TableTransition = [
    #article, adjectif, nom, verbe, nom propre, point
    [1,8,8,8,4,8], #0 attente article ou nom propre
    [8,1,2,8,8,8], #1 boucle adjectif attente nom
    [8,2,8,3,8,8], #2 boucle adjectif attente verbe
    [5,8,8,8,7,9], #3 attente article ou nom propre ou point
    [8,8,8,3,8,8], #4 attente verbe
    [8,5,6,8,8,8], #5 boucle adjectif attente verbe
    [8,6,8,8,8,9], #6 boucle adjectif attente point
    [8,8,8,8,8,9]  #7 attente point
]

"""
//////////////////////////////////////////////////////fonction/////////////////////////////////////////////////////////
"""

def verif_phrase(phrase):
    """
    phrase = string
    fonction qui prend une phrase en parametre et qui affiche si la phrase est bonne ou non dans la console
    fonctoinne sous le principe d'automate grace au dictionaire et la table de transition definit plus haut
    """
    etat = 0
    if len(phrase)>0:
        if phrase[-1] == ".":
            phrase = phrase[0:-1] + " ."

            for mot in phrase.split():
                mot = mot.lower()
                if mot in dictionnaire.keys():
                    etat = TableTransition[etat][dictionnaire[mot]]
                if etat == 8:
                    break
        else:
            print("la phrase n'est pas fini par un point ou vide")
    else:
        print("la phrase est vide")

    if etat == 9:
        print("La phrase est OK")
    elif etat == 8:
        print("La phrase est NULLE")

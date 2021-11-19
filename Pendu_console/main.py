leMot = input("\n \033[1m \033[4mVeillez entrez le mot a deviner :\033[0m ").lower()
print("\033[F \033[K") #pour revenir a la ligne d'avant, puis pour suprimer la ligne, ANSI escape code
laReponse = ""
lesPropositions = [" "]
nbVie = 5


def fabriqueMot(proposition, mot):
    """
    Fonction qui prend une liste de lettre et un mot,
    elle remplace les lettre du mot qui ne sont pas dans les proposition par un _ 

    *** proposition est une liste
    *** mot est un string
    """
    for i,lettre in enumerate(mot):
        if lettre not in proposition:
            mot = mot[:i] + "_" + mot[i+1:]
    return mot

while leMot != laReponse and nbVie>0:
    print("\033[35m \n Le mot est : {} \033[0m".format(fabriqueMot(lesPropositions, leMot)))
    laReponse = input("Votre proposition : ").lower()
    if len(laReponse) == 1 :
        lesPropositions.append(laReponse)
        if laReponse in leMot :
            print("\033[32m oui -" + laReponse + "- appartient au mot \033[0m")
        else:
            nbVie -= 1
            print("\033[31m non tu perd une vie il t'en reste plus que : {} \033[0m".format(nbVie))
    else:
        if laReponse == leMot :
            print("\033[33m c'est gangner le mot etait : {}\033[0m".format(laReponse))
        else:
            nbVie -= 1
            print("\033[31m non tu perd une vie il t'en reste plus que : {} \033[0m".format(nbVie))
    if nbVie == 0 :
        print("\033[31m tu as perdu \033[0m")
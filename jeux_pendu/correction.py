# import modules
import random
#liste 
words=["hello","world","python","tree","conversly","three","congatrulations","apple"]
# tirage au sort
wordChosen=words[random.randint(0,7)]
# variables 
nombreVie=8
motActuel=[]
#print(wordChosen)
# ajouter autant tirets que de lettres dans le mot
for i in range(len(wordChosen)):
    motActuel.append('_')
# boucle principale qui s'arrête lorqu'il ya plus de vies.
for i in range(nombreVie):
# input
    lettreChoisie=input("Devinez une lettre: ")

    if  lettreChoisie in wordChosen:
        print("lettre trouvée!") # Si la lettre de l'utilisateur est dans le mot alors le signaler
        for j in range(len(wordChosen)):
            if lettreChoisie == wordChosen[j]:
                motActuel[j] = lettreChoisie
    # si le mot est complet alors afficher le mot
    if "".join(motActuel) == wordChosen: # transformation en chaîne de caractères de mot actuel
        print("Vous avez trouvé:", motActuel)
        break
    print("Vous en êtes là :", motActuel)
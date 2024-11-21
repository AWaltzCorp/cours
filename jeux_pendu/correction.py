import random
words=["hello","world","python","tree","conversly","three","congatrulations","apple"]
wordChosen=words[random.randint(0,7)]
nombreVie=8
motActuel=[]
#print(wordChosen)
for i in range(len(wordChosen)):
    motActuel.append('_')
for i in range(nombreVie):
    lettreChoisie=input("Devinez une lettre: ")
    if  lettreChoisie in wordChosen:
        print("lettre trouvée!")
        for j in range(len(wordChosen)):
            if lettreChoisie == wordChosen[j]:
                motActuel[j] = lettreChoisie
    if "".join(motActuel) == wordChosen:
        print("Vous avez trouvé:", motActuel)
        break
    print("Vous en êtes là :", motActuel)

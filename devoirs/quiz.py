import random
# améliorations
# Si la réponse n'est pas bonne, continuer de demander à l'utilisateur en comptant le nombre d'erreurs
# Demander les questions et réponses au début à l'utilisateur
quiz = {
    "Quelle est la capitale de la France ?": "paris",
    "Combien font 5 x 6 ?": "30",
    "Quel est le langage de programmation de ce quiz ?": "python"
}
points = 0

for i in range(3): 
    question = random.choice(list(quiz.keys()))  
    print(question)
    userInput = input("Votre réponse : ")
    
    if userInput == quiz[question]:  
        points += 1  
        print("Bonne réponse !")
    else :
      print("mauvaise réponse")
      print(quiz.get(question))
    del quiz[question]
print("vous avez obtenu  "+str(points)+"/3")


    



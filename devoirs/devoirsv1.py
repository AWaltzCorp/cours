import random
words=["hello","world","Python"]
hints=['a word to say hi','the planet','a powerful programming language']
number=random.randint(0,2)
wordChosen=words[number]
hintChosen=hints[number]

def main() :
    choixUtilisateur=input("devinez le mot")
    while choixUtilisateur!= wordChosen :
        print(hintChosen)
        choixUtilisateur=input("devinez le mot")
        
try :    
    main()
except KeyboardInterrupt :
    print('Ctrl +C hit')
   
    
    
    
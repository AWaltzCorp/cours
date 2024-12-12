somme=0
userInput=int(input('entez un nombre'))
if userInput %2==0 :
  somme+=userInput

while userInput !=0:
    userInput=int(input('entrez un nombre'))
    if userInput %2==0 :
      somme+=userInput
print(somme)

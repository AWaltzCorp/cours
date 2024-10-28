from random import randint
Nombretrouve = False
nombre = randint(1,20)
# correction
#if answer < nombre_secret:
 #       print("Plus grand !")
#    elif answer > nombre_secret:
 #       print("Plus petit !")
 #   else:
 # #      print("Bravo, tu as trouvé le nombre !")

while Nombretrouve == False :
    answer = int(input("Deviner le nombre"))
    if answer == nombre :
        Nombretrouve = True
        print('Bravo')
        
    

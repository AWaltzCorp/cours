from random import randint
Nombretrouve = False
nombre = randint(1,20)


while Nombretrouve == False :
    answer = int(input("Deviner le nombre entre 1 et 20"))
    if answer == nombre :
        Nombretrouve = True
        print('Bravo')
        
    

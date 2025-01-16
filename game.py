"""
Manque de commentaires
Modifier la fonction d'affichage des marchandises
Rajouter un paramètre de quantité pour les fonctions achat et vente
Vérifier la demande d'action (si l'action n'existe pas, passer le tour)
Généraliser le fait d'avoir gagné ou perdu (en fonction de si on a acheté ou vendu)
Rendre plus esthétique les affichages de texte
"""
import random
money=100
marchandises={
    "or":{
        "stock":0,
        "prix":0
    },
    "argent":{
        "stock":0,
        "prix":0
    },
    "fruit":{
        "stock":1,
        "prix":0
    }

    
    
}
def print_marchandises():
    print("Price of the gold:",str(marchandises["or"]["prix"])+"\n"+"Price of the silver : ",str(marchandises["argent"]["prix"])+"\n")
def buy(items_to_buy,quantity) :
    global money
    if money-marchandises[items_to_buy]["prix"]<0:
        print("Not enough money") 
    else :
        try:
            money-=marchandises[items_to_buy]["prix"]*quantity
            marchandises[items_to_buy]["stock"]+=quantity
        except KeyError :
            print('no items')
def sell(items_to_sell,quantity) :
    global money
    if marchandises[items_to_sell]["stock"]>=quantity:
        try : 
            marchandises[items_to_sell]["stock"]-=quantity
            money+=marchandises[items_to_sell]["price"]*quantity
        except KeyError:
            print("no items")
            
    else :
        print('Nothing to sell')
for _ in range(10):
    marchandises["fruit"]["prix"]=random.randint(5,15)
    marchandises["or"]["prix"]=random.randint(25,200)
    marchandises["argent"]["prix"]=random.randint(20,150)
    print_marchandises()
    action=input("voulez vous passez votre tour/buy/sell")
    if action =='buy':
       item_to_buy=input('item to buy:')
       buy(item_to_buy)
    if action =='sell':
        item_to_sell=input('item to sell :')
        sell(item_to_sell)
    print(money)
print("Tu a gagné/ perdu"+""+str(money-100))
        
   
   
       
       
   
    
            
    
  
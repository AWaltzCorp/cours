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
MONEY_INITIAL=100
marchandises={
    "gold":{
        "stock":0,
        "price":0
    },
    "silver":{
        "stock":0,
        "price":0
    },
    "fruit":{
        "stock":1,
        "price":0
    }

    
    
}
def end_game () :
    for value in marchandises.values():
        money+value["stock"]*value["price"]
    if MONEY_INITIAL>money :
        print('Vous avez perdu',str(MONEY_INITIAL-money))
    elif MONEY_INITIAL<money :
        print('Vous avez gagné ', str(money-MONEY_INITIAL))
    else :
        print("Match nul")
            
def print_marchandises():
    print("Here are the caractestics of our products :") 
    for clef,valeur in marchandises.items() :
        print("\t Here are the caracteristics of",clef)
        for key,value in valeur.items() :
            print("\t \t"+key,":",value)
def buy(items_to_buy,quantity) :
    global money
    if money-marchandises[items_to_buy]["price"]<0:
        print("Not enough money") 
    else :
        try:
            money-=marchandises[items_to_buy]["price"]*quantity
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
    marchandises["fruit"]["price"]=random.randint(5,15)
    marchandises["gold"]["price"]=random.randint(25,200)
    marchandises["silver"]["price"]=random.randint(20,150)
    print_marchandises()
    action=input("voulez vous passez votre tour/buy/sell")
    if action =='buy':
       item_to_buy=input('item to buy:')
       buy(item_to_buy)
    if action =='sell':
        item_to_sell=input('item to sell :')
        sell(item_to_sell)
    print(money)
end_game()

        
   
   
       
       
   
    
            
    
  
import random
wealth={
  "money":100,
  "fruit":0,
  "gold":0,
  "silver":0
  
}
prices= [0,1,2,200;235,300,500]

prices_wealth={

"fruit":0,
"gold":0,
"silver":0



   
  
}
def buy(item) :
    if item=="fruit":
        wealth["money"]-=prices_wealth["fruit"]
        wealth["fruit"]+=1
    if item=="silver":
        wealth["money"]-=prices_wealth["silver"]
        wealth["silver"]+=1
    if item=="fruit":
        wealth["gold"]-=prices_wealth["gold"]
        wealth["gold"]+=1

for _ in range (10) :
    prices_wealth["fruit"]=random.choice(prices)
    prices_wealth["gold"]=random.choice(prices)
    prices_wealth["silver"]=random.choice(prices)
    print("prices:   " +""+str(prices_wealth))
    print("your wealth"+""+str(wealth))
    nbr_items_to_sell=input("enter numbers of items to sell")
    

  
"""
optimiser les code en utilisant les notions aprises
"""
#  

import random
class Warrior :

    def __init__(self,nom):
        self.nom=nom
        self.pv=1000
        self.is_alive=True
    def show_pv (self):
        print(f"J'ai {self.pv} pv!")
        
    def punch(self,victim) :
        damage=5
        victim.pv-=damage
        print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
    def verify_if_alive(self):
        if self.pv > 0:
            return True
        else:
            self.is_alive = False
            return False
    
        
    

class Elf(Warrior):
    def __init__(self,nom):
        self.bow = random.choice(["leather bow", "iron bow","wood bow"])
        super().__init__(nom)
        
       

    def arrow (self,victim):
        if self.bow== "leather bow" :
            damage=random.randint(10,15)
            victim.pv-=damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
        if self.bow== "wood bow" :
            damage=random.randint(20,25)
            victim.pv-=damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
        if self.bow== "iron bow" :
            damage=random.randint(10,30)
            victim.pv-=damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
   


class Troll(Warrior):
    def __init__(self,nom, ):
        
        super().__init__(nom)
        
        self.shield=random.choice(["wood","iron"])

    
    def pickaxe (self,victim):
        if self.shield =="wood":
            self.pv+=5
            damage=random.randint(10,20)
            victim.pv-=damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
        if self.shield =="iron":
            self.pv+=10
            damage=random.randint(10,20)
            victim.pv-=damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
class Aid (Warrior) :
    def __init__(self, nom):
        super().__init__(nom)
    def aid (self,victim):
        heal_amount=random.randint(1,5)
        victim.pv+=heal_amount
        print(f'{self.nom} a guéri {victim.nom} de {heal_amount}pv')
    

    
    
    
        

Legolas=Elf('Legolas')
Sauron=Troll('Sauron')
Mary=Aid('Mary')
Elisabeth=Aid('Elisabeth')
while Legolas.verify_if_alive() and Sauron.verify_if_alive():

    action = random.choice(["punch", "pickaxe"])
    if action=="punch":
        Sauron.punch(Legolas)
        

    else :
        Sauron.pickaxe(Legolas)
    Mary.aid(Sauron)
    action = random.choice(["punch", "arrow"])
    if action=="punch":
        Legolas.punch(Sauron)
    else :
        Legolas.arrow(Sauron)
    Elisabeth.aid(Legolas)
if Legolas.verify_if_alive() :
    print("Legolas a gagné")
else :
    print("Sauron a gagné")
    
    
  
    

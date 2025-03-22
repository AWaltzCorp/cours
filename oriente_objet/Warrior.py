""""
S'occuper des classes filles en ajoutant des objets avec le add-weapon() de Warrior
Ajouter des armes à l'inventaire de tes personnages

"""
import random
class Inventory :
    def __init__(self):
        self.weapon=dict()
        self.epic_weapon=set()
    def add_weapon(self,name,quantity=1) :
        self.weapon[name]+=quantity
    def del_weapon(self,name,quantity):
        if name in self.weapon :
            self.object[name]-=quantity
        else :
            del self.object[name]
    def add_epic_object(self,name) :
        self.epic_weapon.add(name)
class Warrior :
    def __init__(self,nom):
        self.inventory=Inventory()
        self.nom=nom
        self.pv=1000
        self.is_alive=True
    def add_weapon(self,name,quantity=1) :
        self.inventory.weapon[name] = quantity
        
        
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
        super().__init__(nom)
        self.add_weapon(self,random.choice(["leather bow","wood bow","iron bow"]))
        if  "leather bow" in self.inventory.weapon :
            self.inventory.weapon["leather bow"]=random.randint(15,25)
        if  "wood bow"in self.inventory.weapon :
            self.inventory.weapon["wood bow"]=random.randint(30,35)
        if  "iron bow" in self.inventory.weapon :
            self.inventory.weapon["iron bow"]=random.randint(40,45)

    def arrow (self,victim):
        if  "leather bow" in self.inventory.weapon :
            
            victim.pv-=self.inventory.weapon["leather bow"]
            print(f"{self.nom} attaque {victim.nom} et inflige {self.inventory.weapon["leather bow"]} dégâts !")
        if  "wood bow"in self.inventory.weapon :
            
            victim.pv-=self.inventory.weapon["wood bow"]
            print(f"{self.nom} attaque {victim.nom} et inflige {self.inventory.weapon["wood bow"]} dégâts !")
        if  "iron bow" in self.inventory.weapon :
            victim.pv-=self.inventory.weapon["iron bow"]
            print(f"{self.nom} attaque {victim.nom} et inflige {self.inventory.weapon["iron bow"]} dégâts !")
class Troll(Warrior):
    def __init__(self,nom, ):
        super().__init__(nom)
        self.shield=random.choice(["wood","iron"])
    def pickaxe (self,victim):
        if self.shield =="wood":
            if self.pv<=100:
                self.pv+=5
            damage=random.randint(10,20)
            victim.pv-=damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
        if self.shield =="iron":
            if self.pv<=100:
                self.pv+=10
            damage=random.randint(10,20)
            victim.pv-=damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
class Aid (Warrior) :
    def __init__(self, nom):
        super().__init__(nom)
    def aid (self,victim):
        heal_amount=random.randint(1,15)
        victim.pv+=heal_amount
        print(f'{self.nom} a guéri {victim.nom} de {heal_amount}pv')
    
Legolas=Elf('Legolas')
Sauron=Troll('Sauron')

Elisabeth=Aid('Elisabeth')
while Legolas.verify_if_alive() and Sauron.verify_if_alive():

    action = random.choice(["punch", "pickaxe"])
    if action=="punch":
        Sauron.punch(Legolas)
        

    else :
        Sauron.pickaxe(Legolas)

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
    
    
  
    

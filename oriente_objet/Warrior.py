import random
from time import sleep
class Inventory:
    def __init__(self):
        self.weapon = dict()
        self.epic_weapon = set()

    def add_weapon(self, name, quantity=1):
        self.weapon[name] = self.weapon.get(name, 0) + quantity

    def del_weapon(self, name, quantity):
        if name in self.weapon:
            self.weapon[name] -= quantity
            if self.weapon[name] <= 0:
                del self.weapon[name]
        else:
            print(f"{name} n'existe pas dans l'inventaire.")

    def add_epic_object(self, name):
        self.epic_weapon.add(name)


class Warrior:
    def __init__(self, nom):
        self.inventory = Inventory()
        self.nom = nom
        self.pv = 1000
        self.is_alive = True

    def add_weapon(self, name, quantity=1):
        self.inventory.weapon[name] = quantity

    def show_pv(self):
        print(f"J'ai {self.pv} pv!")

    def punch(self, victim):
        damage = 5
        victim.pv -= damage
        print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")

    def verify_if_alive(self):
        if self.pv > 0:
            return True
        else:
            self.is_alive = False
            return False


class Elf(Warrior):
    def __init__(self, nom):
        super().__init__(nom)
        bow_type = random.choice(["leather bow", "wood bow", "iron bow"])
        if bow_type == "leather bow":
            self.add_weapon("leather bow", random.randint(15, 25))
        elif bow_type == "wood bow":
            self.add_weapon("wood bow", random.randint(30, 35))
        elif bow_type == "iron bow":
            self.add_weapon("iron bow", random.randint(40, 45))

    def arrow(self, victim):
        for bow, damage in self.inventory.weapon.items():
            victim.pv -= damage
            print(f"{self.nom} attaque {victim.nom} avec un {bow} et inflige {damage} dégâts !")
            break  # Sortir de la boucle après avoir utilisé la première arme


class Troll(Warrior):
    def __init__(self, nom):
        super().__init__(nom)
        self.shield = random.choice(["wood", "iron"])

    def pickaxe(self, victim):
        if self.shield == "wood":
            if self.pv <= 100:
                self.pv += 5
            damage = random.randint(10, 20)
            victim.pv -= damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
        if self.shield == "iron":
            if self.pv <= 100:
                self.pv += 10
            damage = random.randint(10, 20)
            victim.pv -= damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")


class Aid(Warrior):
    def __init__(self, nom):
        super().__init__(nom)

    def aid(self, victim):
        heal_amount = random.randint(1, 15)
        victim.pv += heal_amount
        print(f'{self.nom} a guéri {victim.nom} de {heal_amount}pv')


# Création des personnages
Legolas = Elf('Legolas')
Sauron = Troll('Sauron')
Elisabeth = Aid('Elisabeth')

# Combat
while Legolas.verify_if_alive() and Sauron.verify_if_alive():
    action = random.choice(["punch", "pickaxe"])
    if action == "punch":
        Sauron.punch(Legolas)
    else:
        Sauron.pickaxe(Legolas)

    action = random.choice(["punch", "arrow"])
    if action == "punch":
        Legolas.punch(Sauron)
    else:
        Legolas.arrow(Sauron)

    Elisabeth.aid(Legolas)

# Déclaration du vainqueur
if Legolas.verify_if_alive():
    print("Legolas a gagné")
else:
    print("Sauron a gagné")
sleep(10)
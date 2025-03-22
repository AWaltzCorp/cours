# Aide

``` python
class Inventory:
    def __init__(self):
        self.objects = {}  # Dictionnaire {name_objet: quantité}
        self.epic_objects = set()  # Set pour les objects uniques

    def add_object(self, name, quantity=1):
        """Ajoute un objet dans l'inventaire."""
        if name in self.objects:
            self.objects[name] += quantity
        else:
            self.objects[name] = quantity
def del_object(self, name, quantity=1):
        """Retire une certaine quantité d'un objet."""
        if name in self.objects:
            self.objects[name] -= quantity
            if self.objects[name] <= 0:
                del self.objects[name]

    def add_epic_object(self, name):
        """Ajoute un objet unique."""
        self.epic_objects.add(name)
def print_inventory(self):
        """Affiche tout l'inventaire avec une boucle."""
        print("Inventaire :")
        for objet, quantity in self.objects.items():
            print(f"- {objet} : {quantity}")
        print("Objects rares :", " - ".join(self.epic_objects))
class Caracter:
    def __init__(self):
        self.inventory = Inventory()

    def pick_object(self, object, type='normal', quantity=1):
        if type != 'normal':
            self.inventory.add_epic_object(object)
        else:
            self.inventory.add_object(object, quantity=quantity)

    def open_inventory(self):
        self.inventory.print_inventory()
        

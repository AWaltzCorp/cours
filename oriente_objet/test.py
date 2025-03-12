
class Animal:
    def __init__(self, nom, taille,age):
        self.nom = nom
        self.taille = taille
        self.age=age

    def marcher(self):
        print("Je marche")

    def ma_taille(self):
        print(f"Je fais {self.taille} de haut")

class Chien(Animal):
    def __init__(self, race, nom, taille):
        self.race = race
        super().__init__(nom, taille)

    def abboyer(self):
        print("J'abboie")

    def presentation(self):
        print(f"Je suis un chien de la race {self.race}")

chien = Chien("Labrador", "Rex", 12)
chien.marcher()
chien.ma_taille()
chien.presentation()

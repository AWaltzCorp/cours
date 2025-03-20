
class Animal:
    def __init__(self, nom, taille,age):
        self.nom = nom
        self.taille = taille
        self.age=age
        self.couleur="brown"
    def marcher(self):
        print("Je marche")

    def ma_taille(self):
        print(f"Je fais {self.taille} de haut")

class Chien(Animal):
    def __init__(self, race, nom, taille,age):
        self.race = race
        super().__init__(nom, taille,age)

    def abboyer(self):
        print("J'abboie")

    def presentation(self):
        print(f"Je suis un chien de la race {self.race} et de couleur {self.couleur}")

chien = Chien("Labrador", "Rex", 12,6)
chien.marcher()
chien.ma_taille()
chien.presentation()

class Personnage ():
    def __init__(self,nom,taille,age):
        self.nom = nom
        self.taille = taille    
        self.age = age
    def parler(self,phrase):
        print(self.nom + " dit : " + phrase)
    def grandir(self,taille,age):
        self.taille=taille
        self.age=age
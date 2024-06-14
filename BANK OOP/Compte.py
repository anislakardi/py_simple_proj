


class Compte:
    code = 0
    solde = 0.0
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom= prenom
        self.code += self.code + 1

    def verser(self, mt):
        self.solde += mt

    def retirer(self, mt):
        self.solde -= mt
    def afficher(self):
        print(f"********** Mr.{self.nom} {self.prenom} **********")
        print(f"Code: {self.code}| Solde: {self.solde}")
        print()





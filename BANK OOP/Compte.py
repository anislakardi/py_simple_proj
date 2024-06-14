


class Compte:
    code = 0
    solde = 0.0
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom= prenom
        # Increment the class-level code variable
        Compte.code += 1
        # Assign the incremented code to the instance
        self.code = Compte.code

    def verser(self, mt):
        self.solde += mt

    def retirer(self, mt):
        self.solde -= mt
    def afficher(self):
        print(f"********** Mr.{self.nom} {self.prenom} **********")
        print(f"Code: {self.code}| Solde: {self.solde: ,}$")
        print()





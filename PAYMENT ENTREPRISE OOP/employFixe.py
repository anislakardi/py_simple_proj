from employe import Employe


class EmployFixe(Employe):

    def __init__(self , name, salaire):
        super().__init__(name)
        self.salaire = salaire

    def salaire_mensuel(self):
        return self.salaire



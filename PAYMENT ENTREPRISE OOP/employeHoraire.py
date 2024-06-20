from employe import Employe


class EmployeHoraire(Employe):

    def __init__(self , name , nbHeure , tauxHeure):
        super().__init__(name)
        self.nbHeure = nbHeure
        self.tauxHeure = tauxHeure

    def salaire_mensuel(self):
        return self.tauxHeure * self.nbHeure

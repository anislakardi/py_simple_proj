from employe import Employe

class EmployeCommission(Employe):

    def __init__(self, name ,pourcentage, nbVentes , salaireBase):
        super().__init__(name)
        self.pourcentage = pourcentage
        self.nbVentes = nbVentes
        self.salaireBase= salaireBase

    def salaire_mensuel(self):
        return self.salaireBase + (self.pourcentage * self.nbVentes)

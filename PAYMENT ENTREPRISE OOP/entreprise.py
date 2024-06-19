class Entreprise:
    Employees = []
    total = 0
    def __init__(self, name):
        self.name = name
    def ajouter(self, emp):
        self.Employees.append(emp)

    def Moyenne(self):
        for x in self.Employees:
            self.total += x.salaire_mensuel()
        return self.total/len(self.Employees)

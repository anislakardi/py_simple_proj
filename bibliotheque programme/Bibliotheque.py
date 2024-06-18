import Section
import Livre

class Bivliotheque:
    lesSection = []
    maximum = 0
    Nom = ""
    def __init__(self , nom , localisation):
        self.nom = nom
        self.localisation = localisation
        self.Nom =nom


    def ajouterSection(self, sec):
        self.lesSection.append(sec)

    def section_plus_grande(self):
        for x in self.lesSection:
            if self.maximum < x.totalPages:
                self.maximum = x.totalPages
                self.Sec = x

        print(f"La section qui avez la plus grande nombre de pages dans la bibliotheque: {self.Nom} est :"
              f" {self.Sec.nom}")
import Section

class Bibliotheque:
    def __init__(self, nom, localisation):
        self.nom = nom
        self.localisation = localisation
        self.lesSections = []
        self.maximum = 0
        self.Sec = None

    def ajouterSection(self, sec):
        self.lesSections.append(sec)

    def section_plus_grande(self):
        for section in self.lesSections:
            if section.totalPages > self.maximum:
                self.maximum = section.totalPages
                self.Sec = section

        if self.Sec:
            print(f"La section qui a le plus grand nombre de pages dans la bibliotheque {self.nom} est : {self.Sec.nom}")
        else:
            print(f"Aucune section trouvée dans la bibliotheque {self.nom}")

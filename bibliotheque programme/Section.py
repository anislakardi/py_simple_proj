import Livre
import Bibliotheque
class Section(Bibliotheque):
    lesLivres = []
    totalPages = 0
    def __init__(self, nom, responsableSection):
        self.nom = nom
        self.responsableSection = responsableSection

    def ajouterNoveauLivre(self, code, titre, pages):
        self.lesLivres.append(Livre.__init__(code, titre, pages))
        self.totalPages += pages
    def ajouterLivreExister(self, livre):
        self.lesLivres.append(livre)
        self.totalPages += livre.nombrePages


    def nombre_total_pages(self):
        return self.totalPages



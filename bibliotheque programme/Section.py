import Livre

class Section:
    def __init__(self, nom, responsableSection):
        self.nom = nom
        self.responsableSection = responsableSection
        self.lesLivres = []
        self.totalPages = 0

    def ajouterNouveauLivre(self, code, titre, pages):
        nouveau_livre = Livre.Livre(code, titre, pages)
        self.lesLivres.append(nouveau_livre)
        self.totalPages += pages

    def ajouterLivreExister(self, livre):
        self.lesLivres.append(livre)
        self.totalPages += livre.nombrePages

    def nombre_total_pages(self):
        return self.totalPages

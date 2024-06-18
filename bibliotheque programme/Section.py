class Section:
    lesLivres = []
    totalPages = 0
    def __init__(self, nom, responsableSection):
        self.nom = nom
        self.responsableSection = responsableSection

    def ajouterNoveauLivre(self, Code, Titre, Pages):
        self.lesLivres.append(Code, Titre, Pages)
        self.totalPages += Pages
    def ajouterLivreExister(self, livre):
        self.lesLivres.append(livre)
        self.totalPages += livre.nombrePages


    def nombre_total_pages(self):
        return self.totalPages



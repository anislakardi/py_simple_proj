class Livre:
    def __init__(self, code, titre, nombrePages):
        self.code = code
        self.titre = titre
        self.nombrePages = nombrePages

    def info(self):
        return f"le code de ce livre est: {self.code} de titre: {self.titre} avec {self.nombrePages} pages"

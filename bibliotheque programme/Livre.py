import Section
class Livre(Section):

    def __init__(self, code, titre, nombrePages):
        self.code = code
        self.titre = titre
        self.nombrePages = nombrePages

    def info(self):
        return "le code de ce livre est: " +self.code +" de titre: " +self.titre + "avec "+ self.nombrePages+ " de pages"

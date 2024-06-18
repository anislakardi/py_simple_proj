import Bibliotheque
import Section
import Livre

Livre1 = Livre.Livre("2017", "NEYMARJR11", 1400)
Livre2 = Livre.Livre("2018", "CRISTIANO7", 900)
Livre3 = Livre.Livre("2021", "MESSI10", 2000)
Livre4 = Livre.Livre("2023", "MAHREZ", 1200)

GEN2 = Section.Section("FCBERCALON", "LA PORTA")
GEN2.ajouterLivreExister(Livre1)
GEN2.ajouterLivreExister(Livre3)
GEN2.ajouterLivreExister(Livre2)

GEN3 = Section.Section("ALGERIE", "BELMADI")
GEN3.ajouterLivreExister(Livre4)
GEN3.ajouterNouveauLivre("0000", "MBAPEE", 79900)

BEEESTS = Bibliotheque.Bibliotheque("BEST GEN", "PLANET EARTH")
BEEESTS.ajouterSection(GEN2)
BEEESTS.ajouterSection(GEN3)

# Affichage:
print(Livre1.info())
BEEESTS.section_plus_grande()

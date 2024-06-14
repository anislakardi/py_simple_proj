import Compte


Compte1 = Compte.Compte("Anis", "Lakardi")
Compte2 = Compte.Compte("Nassim", "Lakardi")

Compte1.verser(1000)
Compte1.retirer(300)
Compte2.verser(100)

Compte2.afficher()
Compte1.afficher()
import Compte


Compte1 = Compte.Compte("Messi", "Leonel")
Compte2 = Compte.Compte("Neymar jr", "Dasilva Santos")
Compte3 = Compte.Compte("Ronaldo", "Cristiano")

Compte1.verser(500000000)
Compte1.retirer(150000)
Compte2.verser(90000000)
Compte2.retirer(15000000)
Compte3.verser(450000000)
Compte3.retirer(1000000)


Compte1.afficher()
Compte2.afficher()
Compte3.afficher()
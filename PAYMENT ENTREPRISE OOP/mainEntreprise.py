import entreprise
import employe
import employeCommission
import employeHoraire
import employFixe


anis = employeHoraire.EmployeHoraire("Anis Lkd", 10 , 809009)
nassim = employeCommission.EmployeCommission("Nassim Lkd",10,10,50000)
djilali = employeCommission.EmployeCommission("Djilali Lkd",40,15,70000)
riadh = employFixe.EmployFixe("Riadh Lkd",1000000)
neymarjr = employeHoraire.EmployeHoraire("Neymar Dasilva Dantos", 6 , 70990)
leo = employeHoraire.EmployeHoraire("Leo Messi", 8 , 80300)
saures = employFixe.EmployFixe("Luis Saurés",30000)

ASO = entreprise.Entreprise("ASO")
BAR = entreprise.Entreprise("BARCA")
ASO.ajouter(anis)
ASO.ajouter(djilali)
ASO.ajouter(riadh)
BAR.ajouter(neymarjr)
BAR.ajouter(leo)
BAR.ajouter(saures)

print(f"le salaire de {anis.name} est de : {anis.salaire_mensuel():,.0f}$ ,C'est un salarier Horaire")
print(f"le salaire de {djilali.name} est de : {djilali.salaire_mensuel():,.0f}$ ,C'est un salarier Commission")
print(f"le salaire de {saures.name} est de : {saures.salaire_mensuel():,.0f}$ ,C'est un salarier  Fixe")

print(f"le salaire de Moyende de {ASO.name} est de : {ASO.Moyenne():,.0f}$")
print(f"le salaire de Moyende de {BAR.name} est de : {BAR.Moyenne():,.0f}$")





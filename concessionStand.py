menu = {
    "pizza": 8.00,
    "nachos": 5.50,
    "pop-corn": 4.00,
    "frites": 3.50,
    "chips": 2.00,
    "bretzel": 4.00,
    "soda": 2.50,
    "limonade": 3.75
}
panier =[]
total = 0.00
choix = "a"
while choix.lower() != "q":
    print("----- MENU -----")
    for cle, valeur in menu.items():
        print(f"{cle} = {valeur}")
    choix = input("Enter votre ordre (q pour quitez): ")
    for x in menu.keys():
        if x == choix.lower():
            panier.append(choix)
            print("AJOUTER AU PANIER!")
for x in panier:
    for cle, valeur in menu.items():
        if x.lower() == cle:
            total += float(valeur)
print(f"----- TOTAL: {total} -----")








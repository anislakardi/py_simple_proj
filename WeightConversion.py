weight = float(input("Veuillez entrer votre poid : "))
unit = input("quelles est l'unité de le poid que vous avez nous donné :")
x = 0.45359237

if unit == "kg":
  print(f"votre poid est similair a : {round(weight/x,2)} Lbs")
elif unit == "lbs":
  print(f"votre poid est simlair a : { round(weight*x,2)} Kg")
else:
  print("l'unité de mesure est invalid")
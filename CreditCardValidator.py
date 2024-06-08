card = input("Veuillez nous donné votre carte de credit(19 caractere en total): ")
test = True
cardDigit=""
while len(card) < 16 or len(card) > 19:
  print(f"{card} la taille est invalide")
  card = input("Veuillez nous donné votre carte de credit (19 caractere en total): ")

for x in card:
  if not x.isdigit() and x != '-' and x != ' ':
    test = False
  else:
    if x.isdigit():
      cardDigit += x

if test == True: 
  l = len(cardDigit)-1
  digitOdd = 0
  digitEven = 0
  i=0
  for x in range(l,-1,-1):
    if i % 2 == 0:
      digitOdd += int(cardDigit[x])
    else:
      d = int(cardDigit[x])*2
      if d > 9:
        digitEven += ((d % 10)+ int(d / 10))
      else:
        digitEven += d
    i+=1
  total = digitEven+digitOdd
  if total % 10 == 0:
    test = True
  else:
    test = False

#display
if test == True:
  print(f"{card} est VALIDE !")
else:
  print(f"{card} est INVALIDE !")
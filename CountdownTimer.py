import time

t=int(input("Veuillez nous donne le time en seconde : "))


for x in range(t,0,-1):
  s=x % 60
  m=int(x/60)%60
  h=int(x/3600)
  print(f"{h:02}:{m:02}:{s:02}")
  time.sleep(1)

print("FIN!")
import random


low = 1
high = 10
rNumber = random.randint(low, high)
guesses = 0
score = 0

while True:
    number = int(input(f"Guesses the number between {low} and {high}: "))
    if number < rNumber:
        print("FOOOOOOOOOGG!")
        guesses += 1
    elif number > rNumber:
        print("NA9ESS NA9ESS!")
        guesses += 1
    else:
        print("SAHA CHIIIIKH")
        break

print(f"----- SCORE -----")
print(f"{(guesses)} GUESSES")
print(f"RANDOM NUMBER IS :{rNumber}")
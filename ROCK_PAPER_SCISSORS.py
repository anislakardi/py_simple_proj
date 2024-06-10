import random

hand = ["rock", "paper", "scissors"]
score = 0
rounds = 0

print("----- WELCOME TO ROCK PAPER SCISSORS GAME -----")
while True:
    choix = input("Enter your choise if you want to play (q to quit): ")
    choix = choix.lower()
    if choix == "q":
        break
    elif choix != "rock" and choix != "paper" and choix != "scissors":
        print("INVALID INPUT!")
    else:
        rand = random.choice(hand)
        if choix == rand:
            print("DRAW")
            print(f"YOU: {choix.upper()} vs COMPUTER: {rand.upper()}")
        elif choix == "rock" and rand == "scissors" or choix == "paper" and rand == "rock" or choix == "scissors" and rand == "paper":
            print("YOU WIN THIS ROUND!")
            print(f"YOU: {choix.upper()} vs COMPUTER: {rand.upper()}")
            score += 1
        else:
            rounds += 1
            print("YOU LOSE THIS ROUND")
            print(f"YOU: {choix.upper()} vs COMPUTER: {rand.upper()}")
print()
print()
print()
print("----- FINAL SCORE:  -----")
if score == rounds:
    print(f"DRAW! {score}/{rounds}")
elif score > rounds:
    print(f"WIN! {score}/{rounds}")
else:
    print(f"LOSE! {score}/{rounds}")

print("I SAW YOU SMILE!")
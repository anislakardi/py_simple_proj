import functionSlotMachine

print("**********************************")
print("          SLOT MACHINE")
print("**********************************")

balance = 100
while True:
    print(f"Your current balance is: {balance}")
    choise = input("Do you want to spin (Y/N): ")
    if choise.upper() == "N":
        break
    elif choise.upper() == "Y":
        timesOfSpin = int(input("place your bet (1$ for One Spin): "))
        balance += int(functionSlotMachine.Spin(timesOfSpin))
    else:
        print("invalid input")
        break
print()
print()
print("**********************************")
print(f"GAMO OVER! your balance is: {balance}$")
print("**********************************")






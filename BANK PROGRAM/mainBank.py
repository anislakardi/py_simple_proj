import funBank



print("--------------------------")
print("WELCOME TO BANK PROGRAM")
print("--------------------------")
print()
balance = 0
while True:
    print("**************************")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("**************************")
    choise = input("Enter your choise (1-4): ")
    print("**************************")
    if choise == "4":
        break
    elif choise == "1":
        funBank.showBalance(balance)
    elif choise == "2":
        balance += funBank.deposit()
    elif choise == "3":
        balance -= funBank.withdraw(balance)
    else:
        print("INVALID INPUT")
print("BYE")
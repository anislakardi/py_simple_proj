import mesExeptions

def showBalance(totalBalnce):
    print("----- TOTAL BALANCE: -----")
    print(f"{totalBalnce:.2f} DA")
    print("--------------------------")

def deposit():
    print("--------------------------")
    amont = float(input("Enter how much you want to deposit: "))
    while amont <= 0:
        # raise mesExeptions.CustomErrorNegativeAmont(str(amont) +Invalid please enter reel amont )
        print(f"{amont} Invalid please enter reel amont ")
        amont = input("Enter how much you want to deposit(q to quit): ")
        if amont.lower() == "q":
            return 0
        else:
            amont = float(amont)
    
    return amont

def withdraw(totalBalnce):
    print("--------------------------")
    amont = float(input("Enter how much you want to withdraw: "))
    while totalBalnce < amont :
        #raise mesExeptions.CustomErrorLessMoney("YOU HAVE ONLY : " + str(totalBalnce) +"DA")
        print(f"YOU HAVE ONLY : {totalBalnce:.2f}DA")
        amont = input("Enter how much you want to withdaw(q to quit): ")
        if amont.lower() == "q":
            return 0
        else:
            amont = float(amont)
    return amont



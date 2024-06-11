import random

def genPhone(countryCode, areaCode, first4Number, last4Number):
    phoneNum = str(countryCode) + str(areaCode) + str(first4Number) + str(random.randint(10, 99)) + str(last4Number)
    return phoneNum

print("******* WELCOME TO GENERATION OF PHONE NUMBER *******")

CountryCode = input("Enter the Country code: ")
AreaCode = input("Enter the Area code: ")
First4Number = input("Enter the Firsts 4 Numbers: ")
Last4Number = input("Enter the Lastes 4 Numbers: ")

PhoneNum = genPhone(CountryCode, AreaCode, First4Number, Last4Number)
print(f"the phone number is: {PhoneNum}")
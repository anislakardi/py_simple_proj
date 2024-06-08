# Validate user input 
# 1. username is no more than 12 charcters
# 2. username must not contain spaces
# 3. username must not contain digits



username = input("Veulliez entrer votre nom d'utilisateur : ")

len =len(username)
bool = username.isalpha()
print("le nom d'utilisateur est Valide" if len <= 12 and bool else "le nom d'utilisateur est Invalide")
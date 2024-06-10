import random
import string

stringCryp = " " + string.printable + string.punctuation + string.ascii_letters + "_"
listCryp = list(stringCryp)

copyListCrypted = listCryp.copy()

random.shuffle(copyListCrypted)

msgInput = input("Enter text to get crypted one:")
encryptedMsg = ""
for i in msgInput:
    index = listCryp.index(i)
    encryptedMsg += copyListCrypted[index]
print(f"THE ENCRYPTION OF THIS TEXT:{encryptedMsg}")


encryptedMsg = input("Enter the encrypted text to get the reel text:")
discryptionMsg = ""
for x in encryptedMsg:
    index = copyListCrypted.index(x)
    discryptionMsg += listCryp[index]
print(f"THE REEL TEXT IS:{discryptionMsg}")

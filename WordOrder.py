

def wordOrder(NumberWords):
    words = []
    wordTest = []
    repeetTotal = []
    outputstring = []
    for i in range(NumberWords):
        words.append(input(f"please enter the word number {i+1}: "))

    for i in range(NumberWords):
        wordTest = words[i]
        repeat = 0
        j = 0
        for j in range(NumberWords):
            word = words[j]
            if i != j:
                 if len(wordTest) > len(word):
                     repeat = 0
                     break
                 elif wordTest == word:
                     repeat += 1
                 else:
                     k = 0
                     counter = 0
                     while k != len(word):
                         if wordTest[counter] == word[k]:
                             counter += 1
                         else:
                             counter = 0
                         if counter == len(wordTest):
                             repeat += 1
                             break
                         k += 1

        if repeat != 0:
            repeetTotal.append(repeat)



    print(f"{len(repeetTotal)}")
    for x in repeetTotal:
        print(x)
        outputstring = str(x) + " "
    print(outputstring)


























while True:
    num = input("Please enter number of words (x>0): ")
    if int(num) > 0:
        break
    else:
        print(f"{num} INVALIDE INPUT!")
wordOrder(int(num))











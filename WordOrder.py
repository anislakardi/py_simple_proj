

def kifKif(word1, word2):
    return 1 if word1 in word2 else 0


def wordOrder(NumberWords):
    words = []
    newWords = []
    wordTest = []
    repeetTotal = []
    outputstring = ""
    for i in range(NumberWords):
       #words.append(input(f"please enter the word number {i+1}: "))
       words.append(input())
    for x in words:
        if x not in newWords:
            newWords.append(x)
    for i in range(len(newWords)):
        wordTest = newWords[i]
        repeat = 0
        j = i
        for j in range(i+1, NumberWords):
            word = words[j-1]

            repeat += kifKif(wordTest, word)
        if repeat != 0:
            repeetTotal.append(repeat)


    print(f"{len(repeetTotal)}")
    for x in repeetTotal:
        outputstring += str(x) + " "
    print(outputstring)

# main programme
while True:
    #num = input("Please enter number of words (x>0): ")
    num = input()
    if int(num) > 0:
        break
    else:
        print(f"{num} INVALIDE INPUT!")
wordOrder(int(num))











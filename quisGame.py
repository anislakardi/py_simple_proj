questions = ("What is the largest planet in our solar system?: ",
             "Which element has the chemical symbol 'O'?: ",
             "What is the capital of Japan?: ",
             "Which ocean is the largest?: ",
             "Who wrote 'Hamlet'?: ")

options = (("A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"),
           ("A. Gold", "B. Oxygen", "C. Silver", "D. Iron"),
           ("A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"),
           ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
           ("A. William Wordsworth", "B. Charles Dickens", "C. William Shakespeare", "D. Mark Twain"))
answeres = ["B", "B", "C", "D", "C"]

score = 0
number_qustion = 0

for o in options:
    print(f"la qustion numero {number_qustion +1}:")
    print(questions[number_qustion])
    for x in o:
        print(x)
    reponse = input("votre choix (A.B.C.D): ")
    if reponse.upper() == answeres[number_qustion]:
        print("----- BON CHOIX! -----")
        score += 1
    else:
        print("----- MOVAISE CHOIX! -----")
    number_qustion += 1

print("----- SCORE -----")
print((score*100)/5)









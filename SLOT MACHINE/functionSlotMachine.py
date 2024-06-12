import random
import time

def Spin(timesspin):
    symbols = ['🍍', '🍒', '🥑', '🍇', '🍉']
    bet = 0
    for i in range(timesspin):
        pos1 = random.choice(symbols)
        pos2 = random.choice(symbols)
        pos3 = random.choice(symbols)
        print("spinning...")
        time.sleep(3)
        print()
        print(f"{pos1}|{pos2}|{pos3}")
        if pos1 == pos2 and pos2 == pos3:
            bet += 50
            print("YOU WIN !")
            return bet
        elif pos1 != pos2 or pos2 != pos3 or pos1 != pos3:
            bet -= 1
            print("YOU LOSE ROUND")

    return bet


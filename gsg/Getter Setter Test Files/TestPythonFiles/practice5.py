# Practice 5 Lucky Number

import sys
import random

def main():

    luckyNum = random.randint(1,10)
    guessNum = luckyNum+50000

    while (guessNum != luckyNum):

        guessNum = int(input("Guess the Lucky number: "))
        if (guessNum == luckyNum):
            print("Congratualtions you picked the correct number!")
            break
        else: print("Not correct. Please try again.")


main()

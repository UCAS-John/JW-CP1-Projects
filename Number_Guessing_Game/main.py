#John Wangwang RAID: Number Guessing Game

import random

def check(answer: int, number: int) -> bool:
    if answer == number:
        return False
    else:
        return True
    
def diff(answer: int, number: int) -> str:
    if answer == number:
        return "Correct"
    elif answer > number:
        return "Too High"
    elif answer < number:
        return "Too Low"
    else:
        return "Unexpected Error"
    
def main():

    game = True

    num = random.randint(1,10)

    print("\nIn this game you have too gues between number 1 and 10\n")

    while game == True:
        guess = input("Guess a whole number between 1 and 10: ")

        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please type integer!")
            continue

        game = check(guess, num)
        ans = diff(guess, num)

        print(ans)
            

if __name__ == "__main__":
    main()

#John Wangwang RAID: Number Guessing Game

import random

def check(answer: int, number: int) -> bool:
    """
    Get in guess number and compare number as integers
    return boolean data type
    return TRUE if they are the same
    return FLASE if they are different
    """
    if answer == number:
        return False
    else:
        return True
    
def diff(answer: int, number: int) -> str:
    """
    Get in guess number and compare number as integers
    return string data type
    Compare the number if they are too high or too Low
    """
    if answer == number:
        return "Correct"
    elif answer > number:
        return "Too High"
    elif answer < number:
        return "Too Low"
    else:
        return "Unexpected Error"
    
def main():

    #Initialize game to True
    game = True

    #random intgers between 1 to 10
    num = random.randint(1,10)

    print("\nIn this game you have too gues between number 1 and 10\n")

    #Loop if the game is not end
    while game == True:
        guess = input("Guess a whole number between 1 and 10: ")

        #Handling if user doesn't type in integers
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please type integer!")
            continue
        
        #Check if user guess correct
        game = check(guess, num)
        ans = diff(guess, num)

        #print the result
        print(ans)
            

if __name__ == "__main__":
    main()

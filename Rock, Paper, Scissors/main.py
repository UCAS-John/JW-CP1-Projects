#John Wangwang ProficiencyTest: Rock, Paper, Scissors

import random

def convert(choice: int) -> str:
    """
    Get integer 1-3
    return rock, paper or scissors
    """
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    else:
        return "scissors"

def check(user: str, computer: str) -> dict:  
    """
    Get user and computer choices
    return dictionary result of the game
    """
    result = {
        "win" : False,
        "lose" : False,
        "draw" : False
    }

    if user == "rock" and computer == "scissors":
        result["win"] = True
    elif user == "rock" and computer == "paper":
        result["lose"] = True
    elif user == "paper" and computer == "rock":
        result["win"] = True
    elif user == "paper" and computer == "scissors":
        result["lose"] = True
    elif user == "scissors" and computer == "paper":
        result["win"] = True
    elif user == "scissors" and computer == "rock":
        result["lose"] = True
    else:
        result["draw"] = True
    
    return result

def main():

    #initialize score
    user_score = 0
    computer_score = 0

    print("In this game you're going to play rock, paper, scissors against computer!")

    while True:

        computer_choice = random.randint(1, 3) #random computer choice between 1-3

        print("1.Rock\n2.Paper\n3.Scissors")

        #Try getting user choice between 1-3 let user try again if not in range
        try:
            user_choice = int(input("Enter one of the followig number to choose: "))
            if user_choice not in [1,2,3]:
                print("Please enter a valid choice!\n")
                continue
        except ValueError:
            print("Please enter a valid choice!\n")
            continue
        
        #Convert integer choices to string
        computer = convert(computer_choice)
        user = convert(user_choice)
        
        #print what user and computer played
        print(f"\nYou played {user}!\nComputer played {computer}!")

        result = check(user, computer)

        #print out the result and increment score
        if result["win"]:
            user_score += 1
            print("You win the game!")
        elif result["lose"]:
            computer_score += 1
            print("You lose the game!")
        else:
            print("The game is draw!")

        print(f"\nCurrent score:\nPlayer: {user_score}\nComputer: {computer_score}\n") #print out the score

        stop = input("Press any key to continue playing the game\nPress 1 to stop playing\nEnter your choice:")#get user choice if they wish to stop

        #Check if user wish to continue the game
        if stop == "1":
            break
        else:
            continue

if __name__ == "__main__":
    main()
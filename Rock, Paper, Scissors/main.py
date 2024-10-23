#John Wangwang ProficiencyTest: Rock, Paper, Scissors

import random

def convert(choice: int) -> str:

    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    else:
        return "scissors"

def check(user: str, computer: str) -> dict:

    result = {
        "win" : False,
        "lose" : False,
        "draw" : False
    }

    if user == computer:
        return "draw"
    elif user == "rock" and computer == "scissors":
        return "win"
    elif user == "rock" and computer == "paper":
        return "lose"
    elif user == "paper" and computer == "scissors":
        return "win"
    elif user == "paper" and computer == "paper":
        return "lose"
    elif user == "scissors" and computer == "scissors":
        return "win"
    elif user == "scissors" and computer == "paper":
        return "lose"

def main():

    print("In this game you're going to play rock, paper, scissors against computer!")

    while True:

        computer_choice = random.randint(1, 3)

        print("1.Rock\n2.Paper\n3.Scissors")

        try:
            user_choice = int(input("Enter one of the followig number to choose: "))
        except ValueError:
            print("Please enter a valid choice!")
            continue
        
        computer = convert(computer_choice)
        user = convert(user_choice)

        print(f"You played {user}!\nComputer played {computer}!")


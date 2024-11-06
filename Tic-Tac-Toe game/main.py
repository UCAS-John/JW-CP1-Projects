#John Wangwang ProficiencyTest: Tic-Tac-Toe game

import random

board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def print_board():

    print("-----------")
    for row in board:
        for grid in row:
            print(f"|{grid}| ", end="")
        print("\n-----------")

def user_play(user: int):

    for (row_index, row) in enumerate(board):
        for (grid_index, grid) in enumerate(row):
            if user == grid:
                board[row_index][grid_index] = "X"
    
def computer_play():

    computer = random.randint(1,9)

    for (row_index, row) in enumerate(board):
        for (grid_index, grid) in enumerate(row):
            if computer == grid:
                board[row_index][grid_index] = "O"

def check_state() -> dict:

    result = {
        "win" : False,
        "lose" : False,
        "draw" : False
    }

    for row in board:
        if all(grid == row[0] for grid in row):
            if row[0] == "O":
                result["lose"] = True
            else:
                result["win"] = True

def main():
    
    error_message = "Please enter a valid grid number!\nMake sure it is unoccupied!"

    print("Tic-Tac-Toe game")
    print("You will play as X and Computer will play as O.")
    print("This is the current board.")

    while True:
        print_board()

        while True:

            valid = False

            try:
                user = int(input("Enter the number of grid you want to play: "))
            except ValueError:
                print(error_message)
                continue

            for row in board:
                if user in row:
                    valid = True
                    print(f"You played on grid {user}!")
                    break

            if valid:
                break

            print(error_message)
            continue

        user_play(user)
        computer_play()



if __name__ == "__main__":
    main()
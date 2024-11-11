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

def game() -> dict:

    result = {
        "win" : False,
        "lose" : False,
        "draw" : False,
    }

    #Check for draw
    if all(type(grid) is str for row in board for grid in row):
        result["draw"] = True
        return result
    
    #Check column win
    for (grid_index, grid) in enumerate(board[0]):
            if grid == board[1][grid_index] and grid == board[2][grid_index]:
                if board[0][grid_index] == "X":
                    result["win"] = True
                    return result
                elif board[0][grid_index] == "O":
                    result["lose"] = True
                    return result

    #Check row win
    for (row_index, row) in enumerate(board):
        if all(grid == board[row_index][0] for grid in row):
            if board[0][grid_index] == "X":
                result["win"] = True
                return result
            elif board[0][grid_index] == "O":
                result["lose"] = True
                return result
    
    #Check Diagonal win
    for (row_index, row) in enumerate(board):
        for (grid_index, grid) in enumerate(row):
            if grid_index == 0 and row_index == 0:
                if grid == board[1][1] and grid == board[2][2]:
                    if board[0][grid_index] == "X":
                        result["win"] = True
                        return result
                    elif board[0][grid_index] == "O":
                        result["lose"] = True
                        return result
            elif grid_index == 2 and row_index == 0:
                if grid == board[1][1] and grid == board[2][0]:
                    if board[0][grid_index] == "X":
                        result["win"] = True
                        return result
                    elif board[0][grid_index] == "O":
                        result["lose"] = True
                        return result
    return result

def main():
    
    error_message = "Please enter a valid grid number!\nMake sure it is unoccupied!"

    print("Tic-Tac-Toe game")
    print("You will play as X and Computer will play as O.")
    print("This is the current board.")

    print_board()

    while True:

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
        print_board()

        result = game()

        if result["draw"]:
            print("The game is draw!")
            break
        elif result["win"]:
            print("You won the game!")
            break
        elif result["lose"]:
            print("You lost the game!")
            break
        else:
            continue

if __name__ == "__main__":
    main()
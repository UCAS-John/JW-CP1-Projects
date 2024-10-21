import random

def start_game():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False

    while not game_over:
        """
        Guess variable is string
        Runtime error
        Can't compare string to integers
        """
        guess = int(input("Enter your guess: "))

        """
        Number of attempt is not increment
        Logic error
        This will allow user to guess more than 10 times
        """
        attempts += 1

        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
            break

        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        continue

    print("Game Over. Thanks for playing!")
    
start_game()

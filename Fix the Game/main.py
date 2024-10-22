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
        Attempts checking
        Logic error
        number of attempts is check after enter the guess it need to check before enter the guess
        """
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
            break

        """
        Guess variable is string
        Runtime error
        Can't compare string to integers
        """
        guess = int(input("Enter your guess: "))

        """
        Program run after guess is correct
        Logic error
        Program will keep checking even after user guessed correctly
        """
        """
        Number of attempt is not increment
        Logic error
        This will allow user to guess more than 10 times
        """
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
            attempts += 1
            break
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1
            continue
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts += 1
            continue

    print("Game Over. Thanks for playing!")
    
start_game()

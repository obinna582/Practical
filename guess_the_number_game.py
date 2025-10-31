
import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()

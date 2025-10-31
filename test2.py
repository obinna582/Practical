import tkinter as tk
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number Game")

        self.number_to_guess = random.randint(1, 10)
        self.attempts = 0

        self.label = tk.Label(master, text="I'm thinking of a number between 1 and 10.")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} tries.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

# Create the main window and run the game
root = tk.Tk()
game = GuessTheNumberGame(root)
root.mainloop()

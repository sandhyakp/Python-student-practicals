import tkinter as tk
from tkinter import messagebox
import random

word_list = ["python", "java", "sandhya", "ranjit", "om", "shalini","truebeauty"]

def get_word():
    return random.choice(word_list)  # Use choice() to select a random word

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word = get_word()
        self.guesses = set()
        self.max_attempts = 6
        self.remaining_attempts = self.max_attempts

        self.word_display = ['_' for _ in self.word]  # Initialize word display

        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack(pady=10)

        self.word_label = tk.Label(self.root, text=" ".join(self.word_display), font=('Helvetica', 18))
        self.word_label.pack(pady=10)

        self.attempts_label = tk.Label(self.root, text=f"Remaining attempts: {self.remaining_attempts}")
        self.attempts_label.pack(pady=10)

        self.letter_entry = tk.Entry(self.root)
        self.letter_entry.pack(pady=10)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.guess_letter)
        self.guess_button.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def guess_letter(self):
        letter = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)

        if len(letter) != 1 or not letter.isalpha():
            messagebox.showerror("Invalid input", "Please enter a single letter")
            return

        if letter in self.guesses:
            messagebox.showerror("Already guessed", "You have already guessed this letter")
            return

        self.guesses.add(letter)
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.word_display[i] = letter

        else:
            self.remaining_attempts -= 1
            self.draw_hangman()

        self.update_display()
        self.check_game_status()

    def update_display(self):
        self.word_label.config(text=' '.join(self.word_display))
        self.attempts_label.config(text=f"Remaining attempts: {self.remaining_attempts}")

    def check_game_status(self):
        if '_' not in self.word_display:
            messagebox.showinfo("Hangman", "Congratulations! You Won!")
            self.reset_game()

        elif self.remaining_attempts <= 0:
            messagebox.showinfo("Hangman", f"You Lost! The word was '{self.word}'")
            self.reset_game()

    def draw_hangman(self):
        if self.remaining_attempts == 5:
            self.canvas.create_oval(130, 100, 170, 140, width=2)  # Head

        elif self.remaining_attempts == 4:
            self.canvas.create_line(150, 140, 150, 200, width=2)  # Body

        elif self.remaining_attempts == 3:
            self.canvas.create_line(150, 160, 130, 180, width=2)  # Left arm
            self.canvas.create_line(150, 160, 170, 180, width=2)  # Right arm

        elif self.remaining_attempts == 2:
            self.canvas.create_line(150, 200, 130, 240, width=2)  # Left leg
            self.canvas.create_line(150, 200, 170, 240, width=2)  # Right leg

        elif self.remaining_attempts == 1:
            self.canvas.create_line(150, 50, 150, 100, width=2)  # Rope

        elif self.remaining_attempts == 0:
            self.canvas.create_line(100, 280, 100, 50, width=2)  # Pole
            self.canvas.create_line(100, 50, 150, 50, width=2)  # Top of the gallows
            self.canvas.create_line(20, 280, 180, 280, width=2)  # Base

    def reset_game(self):
        self.word = get_word()
        self.guesses.clear()
        self.word_display = ['_' for _ in self.word]
        self.remaining_attempts = self.max_attempts
        self.canvas.delete("all")
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

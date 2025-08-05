
import tkinter as tk
import random

# Choices
choices = ['Rock', 'Paper', 'Scissors']

# Main function to determine winner
def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == 'Rock' and computer == 'Scissors') or
        (user == 'Paper' and computer == 'Rock') or
        (user == 'Scissors' and computer == 'Paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Set up GUI window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=('Arial', 18))
title_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=12, command=lambda: play('Rock'))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=12, command=lambda: play('Paper'))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=12, command=lambda: play('Scissors'))
scissors_button.grid(row=0, column=2, padx=5)

# Result label
result_label = tk.Label(root, text="", font=('Arial', 14), fg="blue")
result_label.pack(pady=20)

# Run the GUI loop
root.mainloop()

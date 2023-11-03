import tkinter as tk
from tkinter import messagebox

# Define the quiz questions, answer options, and correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin"],
        "correct_option": 0,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter"],
        "correct_option": 0,
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale"],
        "correct_option": 2,
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Au", "Ag"],
        "correct_option": 1,
    },
]

# Create a variable to keep track of the current question
current_question = 0

# Create a function to check the answer
def check_answer():
    global current_question
    selected_option = var.get()
    correct_option = questions[current_question]["correct_option"]
    if selected_option == correct_option:
        messagebox.showinfo("Correct", "You got it right!")
    else:
        messagebox.showerror("Incorrect", "Sorry, that's wrong.")

    # Move to the next question or finish the quiz
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("Quiz Completed", "You've completed the quiz!")
        root.destroy()

# Create a function to display the next question
def display_question():
    question_label.config(text=questions[current_question]["question"])
    var.set(-1)  # Reset the selected option
    for i, option in enumerate(option_buttons):
        option.config(text=questions[current_question]["options"][i])

# Create the main window
root = tk.Tk()
root.title("Multiple Choice Quiz")

# Create a question label
question_label = tk.Label(root, text="", font=("Arial", 12))
question_label.pack(pady=20)

# Create a variable to track the selected option
var = tk.IntVar()
var.set(-1)

# Create radio buttons for answer options
option_buttons = []
for i in range(3):
    option_button = tk.Radiobutton(root, text="", variable=var, value=i)
    option_button.pack(pady=5)
    option_buttons.append(option_button)

# Create a button to submit the answer
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack()

# Display the first question
display_question()

# Start the application
root.mainloop()

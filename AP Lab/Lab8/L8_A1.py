import tkinter as tk
from tkinter import messagebox

# Define the quiz questions and answers
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal in the world?",
    "What is the chemical symbol for gold?"
]

correct_answers = ["Paris", "Mars", "Blue Whale", "Au"]

# Create a variable to keep track of the current question
current_question = 0

# Create a function to check the answer
def check_answer():
    global current_question
    user_answer = user_input.get()
    if user_answer == correct_answers[current_question]:
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
    question_label.config(text=questions[current_question])
    user_input.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Quiz Application")

# Create a question label
question_label = tk.Label(root, text="", font=("Arial", 12))
question_label.pack(pady=20)

# Create an entry for user input
user_input = tk.Entry(root, font=("Arial", 12))
user_input.pack(pady=10)

# Create a button to submit the answer
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack()

# Display the first question
display_question()

# Start the application
root.mainloop()
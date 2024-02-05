import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create the main Tkinter window
root = tk.Tk()
root.title("Quiz App")

# Database connection
conn = sqlite3.connect("quiz/db.sqlite3")
cursor = conn.cursor()

# Sample questions for testing
questions = [
    ("What is the capital of France?", "B"),
    ("What is the largest planet in our solar system?", "A"),
    ("Which programming language is this quiz written in?", "C"),
]


# Function to start the quiz
def start_quiz():
    # Get the username from the entry widget
    username = username_entry.get()

    # Insert the username into the User table
    cursor.execute("INSERT INTO quiz_app_user (username) VALUES (?)", (username,))
    conn.commit()

    # Fetch the user's ID
    cursor.execute("SELECT id FROM quiz_app_user WHERE username = ?", (username,))
    user_id = cursor.fetchone()[0]

    for question_text, correct_option in questions:
        # Display the question and options with buttons
        answer = ask_question(question_text, ["A", "B", "C", "D"])

        # Insert the user's answer into the UserAnswer table
        cursor.execute(
            "INSERT INTO quiz_app_useranswer (user_id, question_id, chosen_option, is_correct) VALUES (?, ?, ?, ?)",
            (user_id, 0, answer, answer == correct_option),
        )
        conn.commit()

        # Display the result to the user
        messagebox.showinfo(
            "Result",
            f"Your answer for the question is {'correct' if answer == correct_option else 'incorrect'}",
        )


def ask_question(question_text, options):
    answer = ""

    # Function to set the answer variable when a button is clicked
    def set_answer(option):
        nonlocal answer
        answer = option
        root.quit()

    # Display the question
    tk.Label(root, text=question_text).pack()

    # Create buttons for each option, aligned horizontally
    for option in options:
        button = tk.Button(root, text=option, command=lambda o=option: set_answer(o))
        button.pack(side=tk.LEFT, padx=5)

    # Wait for the user to click a button
    root.mainloop()

    # Clear the window for the next question
    for widget in root.winfo_children():
        widget.destroy()

    return answer


# Create and pack widgets
username_label = tk.Label(root, text="Enter your username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_button.pack()

# Start the Tkinter event loop
root.mainloop()

# Close the database connection when the program ends
conn.close()

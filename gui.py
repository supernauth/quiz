import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter.constants import END
import sqlite3
from django.db import models

# Create the main Tkinter window
root = tk.Tk()
root.title("Quiz App")

# Database connection
conn = sqlite3.connect("quiz/db.sqlite3")
cursor = conn.cursor()


# Function to start the quiz
def start_quiz():
    # Get the username from the entry widget
    username = username_entry.get()

    # Close the entire Tkinter window
    root.destroy()

    # Insert the username into the User table
    cursor.execute("INSERT INTO quiz_app_user (username) VALUES (?)", (username,))
    conn.commit()

    # Fetch the user's ID
    cursor.execute("SELECT id FROM quiz_app_user WHERE username = ?", (username,))
    user_id = cursor.fetchone()[0]

    # Retrieve questions from the Question table
    cursor.execute("SELECT * FROM quiz_app_question")
    questions = cursor.fetchall()

    # Iterate through the questions
    for question in questions:
        # Display the question in a popup window
        answer = simpledialog.askstring("Question", question[-1])

        # Insert the user's answer into the UserAnswer table
        cursor.execute(
            "INSERT INTO quiz_app_useranswer (user_id, question_id, chosen_option, is_correct) VALUES (?, ?, ?, ?)",
            (
                user_id,
                question[0],
                answer,
                False,
            ),
        )
        conn.commit()

        # Check if the answer is correct and update the UserAnswer table accordingly
        is_correct = answer == question[1]
        cursor.execute(
            "UPDATE quiz_app_useranswer SET is_correct = ? WHERE user_id = ? AND question_id = ?",
            (is_correct, user_id, question[0]),
        )
        conn.commit()

        # Display the result to the user
        messagebox.showinfo(
            "Result",
            f"Your answer for the question is {'correct' if is_correct else 'incorrect'}",
        )


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

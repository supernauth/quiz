import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

# Create the main Tkinter window
root = tk.Tk()
root.geometry("250x125")
root.title("Quiz App")
root.configure(bg="lightgrey")
font_style = ("Verdana", 14, "normal")

# Database connection
conn = sqlite3.connect("quiz/db.sqlite3")
cursor = conn.cursor()


# Function to start the quiz
def start_quiz():
    # Get the username
    username = username_entry.get()

    # Insert the username into the User table
    cursor.execute("INSERT INTO quiz_app_user (username) VALUES (?)", (username,))
    conn.commit()

    # Fetch the user's ID
    cursor.execute("SELECT id FROM quiz_app_user WHERE username = ?", (username,))
    user_id = cursor.fetchone()[0]

    # Retrieve questions from the Question table
    cursor.execute("SELECT * FROM quiz_app_question")
    questions = cursor.fetchall()

    # Close the name entry window
    root.destroy()

    # Iterate through the questions
    for question in questions:
        # Initialize the answer variable
        answer = ""

        # Keep asking the question until a valid answer is provided
        while True:
            # Display the question in a popup window
            answer = simpledialog.askstring("Question", question[-1])

            # Check if the user canceled the dialog
            if answer is None:
                messagebox.showinfo("Quiz App", "Quiz cancelled.")
                conn.close()
                return

            # Check if the answer is not empty and is one of A, B, C, or D
            if answer.upper() in ["A", "B", "C", "D"]:
                break  # Break the loop if a valid answer is provided

            # Inform the user about the invalid answer
            messagebox.showwarning(
                "Invalid Answer", "Please choose one of the options A, B, C, or D."
            )

        # Convert the answer to uppercase
        answer = answer.upper()

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

        # Add the results in a string
        result_string = ""

        # Add the question and result to the result string
        result_string += f"{question[-1]}\nYour answer was {'correct.' if is_correct else 'incorrect'}"

        # Include the correct answer only when the user's answer is incorrect
        if not is_correct:
            result_string += (
                f", the correct answer was: {question[1]}.\n(You chose {answer}.)"
            )

        result_string += "\n"

        # Display the accumulated results to the user
        messagebox.showinfo("Question and Result", result_string)

    conn.close()


# Create and pack widgets
username_label = tk.Label(
    root, text="Enter your username:", font=font_style, bg="lightgrey"
)
username_label.pack()

username_entry = tk.Entry(root, font=font_style)
username_entry.pack()

start_button = tk.Button(root, text="Start Quiz", command=start_quiz, font=font_style)
start_button.pack()

# Start the Tkinter event loop
root.mainloop()

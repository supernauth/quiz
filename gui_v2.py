import os
import django
import tkinter as tk
from tkinter import simpledialog
from django.db import models

# Set the Django settings module before importing models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz.quiz.settings")
django.setup()

# Now you can import your models
from quiz.quiz_app.models import (
    User,
    Question,
    UserAnswer,
)  # Adjust the import based on your app structure

# Create the main Tkinter window
root = tk.Tk()
root.title("Quiz App")


# Function to start the quiz
def start_quiz():
    # Get the username from the entry widget
    username = username_entry.get()

    # Insert the username into the User table
    user = User.objects.create(username=username)

    # Retrieve questions from the Question table
    questions = Question.objects.all()

    # Iterate through the questions
    for question in questions:
        # Display the question in a popup window
        answer = simpledialog.askstring("Question", question.question_text)

        # Insert the user's answer into the UserAnswer table
        user_answer = UserAnswer.objects.create(
            user=user, question=question, chosen_option=answer
        )

        # Check if the answer is correct and update the UserAnswer table accordingly
        user_answer.is_correct = answer == question.correct_option
        user_answer.save()


# Create and pack widgets
username_label = tk.Label(root, text="Enter your username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_button.pack()

# Start the Tkinter event loop
root.mainloop()

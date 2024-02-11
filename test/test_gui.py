import unittest
from unittest.mock import patch
import sqlite3
import os


class TestQuizApp(unittest.TestCase):
    DB_NAME = "test_db.sqlite3"

    @classmethod
    def setUpClass(cls):
        # Create a temporary database for testing
        cls.conn = sqlite3.connect(cls.DB_NAME)
        cls.cursor = cls.conn.cursor()

        # Create test tables
        cls.cursor.execute(
            "CREATE TABLE quiz_app_user (id INTEGER PRIMARY KEY, username TEXT)"
        )
        cls.cursor.execute(
            "CREATE TABLE quiz_app_question (id INTEGER PRIMARY KEY, correct_option TEXT, question TEXT)"
        )
        cls.cursor.execute(
            "CREATE TABLE quiz_app_useranswer (id INTEGER PRIMARY KEY, user_id INTEGER, question_id INTEGER, chosen_option TEXT, is_correct INTEGER)"
        )

        # Insert sample data
        cls.cursor.execute(
            "INSERT INTO quiz_app_question (correct_option, question) VALUES ('A', 'What is 1+1?')"
        )
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # Close the temporary database connection and remove the temporary file
        cls.conn.close()
        os.remove(cls.DB_NAME)

    @patch("tkinter.simpledialog.askstring", return_value="A")
    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.messagebox.showwarning")
    def test_start_quiz(self, mock_showwarning, mock_showinfo, mock_askstring):
        import quiz_app  # Assuming the code is in quiz_app.py

        # Mocking user input
        mock_askstring.side_effect = ["John"]

        # Call the start_quiz function
        quiz_app.start_quiz()

        # Check if the messagebox was shown for each question
        self.assertEqual(mock_askstring.call_count, 1)
        self.assertEqual(mock_showinfo.call_count, 1)
        self.assertEqual(mock_showwarning.call_count, 0)

        # Check if the database has been updated correctly
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM quiz_app_user")
        self.assertEqual(cursor.fetchone()[1], "John")

        cursor.execute("SELECT * FROM quiz_app_useranswer")
        user_answer = cursor.fetchone()
        self.assertEqual(user_answer[1], 1)  # Assuming question ID is 1
        self.assertEqual(user_answer[2], "A")
        self.assertEqual(user_answer[3], 1)  # Assuming the answer is correct


if __name__ == "__main__":
    unittest.main()

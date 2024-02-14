import sqlite3
import unittest


db = "db.sqlite3"

query1 = """SELECT correct_option 
    FROM quiz_app_question 
    WHERE id=1;"""

query2 = """SELECT correct_option 
    FROM quiz_app_question 
    WHERE id=3;"""

query3 = """SELECT correct_option 
    FROM quiz_app_question 
    WHERE id=5;"""


def query_executer(query, database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()
    s = ""

    for row in rows:
        for ele in row:
            s += str(ele)
            print(s)

    if cursor:
        cursor.close()
    if conn:
        conn.close()

    return s


class TestQuery(unittest.TestCase):
    def test_query1(self):
        self.assertEqual("B", query_executer(query1, db))

    def test_query2(self):
        self.assertEqual("C", query_executer(query2, db))

    def test_query3(self):
        self.assertEqual("C", query_executer(query3, db))


unittest.main()

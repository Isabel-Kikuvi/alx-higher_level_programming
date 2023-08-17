#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Retrieves states from database"""
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    curr = conn.cursor()
    curr.execute("SELECT * FROM states")
    myresult = curr.fetchall()
    for row in myresult:
        print(row)

#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

"""prints all states tha start with N in Asc order"""


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    curr = conn.cursor()
    curr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
            ORDER BY id ASC")
    myresult = curr.fetchall()
    for row in myresult:
        print(row)

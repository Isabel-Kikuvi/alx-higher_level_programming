#!/usr/bin/python3
"""script that lists all cities of the state provided as an arg"""

import MySQLdb
from sys import argv

"""prints a list of cities"""

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    curr = conn.cursor()
    curr.execute("""
        SELECT
            cities.id, cities.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE states.name LIKE BINARY %(name)s
        ORDER BY
            cities.id ASC
        """, {'name': argv[4]})
    myresult = curr.fetchall()

    if myresult is not None:
        print(", ".join([row[1] for row in myresult]))

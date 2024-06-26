#!/usr/bin/python3
"""
Lists all states from database hbtn_0e_0_usa
Ordered by states.id
Used the module MySQLdb (import MySQLdb)
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting to hbtn_0e_0_usa d
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    curx = db.cursor()
    curx.execute("SELECT * FROM states ORDER BY id ASC")
    rows = curx.fetchall()
    for row in rows:
        print(row)
    # Close  cursor and db
    curx.close()
    db.close()

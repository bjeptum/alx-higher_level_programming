#!/usr/bin/python3
"""
Lists all states from database base hbtn_0e_0_usa
Starting with N(upper N)
Ordered by states.id
Used the module MySQLdb
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    # Create cursor
    curx = db.cursor()
    # Execute select to query data
    curx.execute("SELECT * FROM states WHERE name LIKE 'N%'
                 COLLATE SQL_Latin1_General_CP1_CS_AS
                 ORDER BY id ASC")
    rows = curx.fetchall()
    for row in rows:
        print(row)
    # Close cursor and db
    curx.close()
    db.close()

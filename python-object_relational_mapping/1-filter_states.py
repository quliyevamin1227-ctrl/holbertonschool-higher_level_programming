#!/usr/bin/python3
"""List states whose names start with N."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT id, name FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )
    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()

#!/usr/bin/python3

"""listing
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    result = c.fetchall()

    for r in result:
        print(r)

    c.close()
    db.close()

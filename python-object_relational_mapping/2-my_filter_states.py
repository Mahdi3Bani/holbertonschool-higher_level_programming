#!/usr/bin/python3
"""
list all tates with name

"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute(
        "SELECT * FROM states WHERE name LIKE  BINARY '{}' ORDER BY id"
        .format(argv[4]))
    result = c.fetchall()

    for r in result:
        print(r)

    c.close()
    db.close()

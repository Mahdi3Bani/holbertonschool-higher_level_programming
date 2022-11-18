#!/usr/bin/python3
""""
script that lists all lists all the states
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost', user=argv[1], password=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.excute("""SELECT id, name FROM states ORDER BY id;""")
    res = cursor.fetchall()

    for r in res:
        print(r)

    cursor.close()
    db.close()


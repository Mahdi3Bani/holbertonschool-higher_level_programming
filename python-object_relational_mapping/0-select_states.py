#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.excute("SELECT * FROM states ORDER BY id")
    result = cursor.fetchall()

    for r in result:
        print(r)

    cursor.close()
    db.close()

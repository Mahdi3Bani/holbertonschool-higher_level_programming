#!/usr/bin/python3

"""
same as previous but safe from sql injection

"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute(
        "SELECT * FROM states WHERE name LIKE  = %s ORDER BY id"
        ,(argv[4],))
    result = c.fetchall()

    for r in result:
        print(r)

    c.close()
    db.close()

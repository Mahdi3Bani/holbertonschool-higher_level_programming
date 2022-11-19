#!/usr/bin/python3

"""
listing everything

"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute(
        "SELECT * states.id, cities.name, states.name FROM citites JOIN states ON states.id = cities.state_id  ORDER BY cities.id")
    result = c.fetchall()

    for r in result:
        print(r)

    c.close()
    db.close()

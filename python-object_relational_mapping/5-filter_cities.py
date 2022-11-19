#!/usr/bin/python3

"""
listing by cities name
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id""",(argv[4],))
    result = c.fetchall()

    for r in result:
        print(r)

    c.close()
    db.close()

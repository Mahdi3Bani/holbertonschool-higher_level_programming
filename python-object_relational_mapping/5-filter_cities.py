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
        """SELECT cities.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id""",(argv[4],))
    result = c.fetchall()

    tab = []
    for r in result:
        tab.append(r[0])
        tab.append(', ')
    for i in range(len(tab) - 1):
        print (tab[i], end ="")

    c.close()
    db.close()

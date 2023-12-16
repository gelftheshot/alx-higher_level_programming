#!/usr/bin/python3

""" mysqldb that use python to show every thing from state
    data base """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name, states.name FROM states "
                "INNER JOIN cities ON cities.state_id=states.id")
    cities = [city[0] for city in cur.fetchall() if city[1] == sys.argv[4]]
    print(", ".join(cities))

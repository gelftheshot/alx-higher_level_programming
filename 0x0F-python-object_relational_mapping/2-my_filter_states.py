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
    cur.execute("SELECT * FROM `states` WHERE BINARY \
                     `name`='{}' ORDER BY id".format(sys.argv[4]))
    for state in cur.fetchall():
        print(state)

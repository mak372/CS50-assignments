# TODO
from sys import argv
from cs50 import SQL
import sqlite3
if len(argv) != 2:
    print("Usage: python roster.py house")
    exit(1)
db = SQL("sqlite:///students.db")
output = list(db.execute("SELECT * FROM  students WHERE house = ? ORDER BY last ASC,first ",argv[1]))
for row in output:
    first = row["first"]
    middle = row["middle"]
    last = row["last"]
    birth = row["birth"]
    if not middle:
        print(f"{first} {last}, born {birth}")
    else:
        print(f"{first} {middle} {last}, born {birth}")

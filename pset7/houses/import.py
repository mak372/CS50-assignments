# TODO
from sys import argv
from csv import DictReader
import sqlite3
from cs50 import SQL
import csv
db = SQL("sqlite:///students.db")
if len (argv) != 2:
    print("Usage: python import.py characters.csv")
    exit(1)

with open(argv[1]) as file:
    output = csv.DictReader(file,delimiter = ',')
    for row in output:
          name = row["name"]
          new_name = name.split()
          if len(new_name) < 3:
               db.execute("INSERT INTO students(first,middle,last,house,birth)VALUES(?,?,?,?,?)",
               new_name[0],None,new_name[1],row["house"],row["birth"])


          else:
                db.execute("INSERT INTO students(first,middle,last,house,birth)VALUES(?,?,?,?,?)",
                new_name[0],new_name[1],new_name[2],row["house"],row["birth"])


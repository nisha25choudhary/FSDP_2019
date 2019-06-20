# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:18:09 2019

@author: Lenovo
"""


import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'university.db' )
c = conn.cursor()
c.execute ("""CREATE TABLE students(
          name TEXT,
          age  INTEGER,
          rollno INTEGER,
          branch TEXT
          )""")

c.execute("INSERT INTO students VALUES ('Nisha',20, 101, 'CS')")
c.execute("INSERT INTO students VALUES ('Hanu',21, 102, 'CS')")
c.execute("INSERT INTO students VALUES ('Meenal',20, 103, 'CSE')")
c.execute("INSERT INTO students VALUES ('Naveen',22, 104, 'MGMT')")
c.execute("INSERT INTO students VALUES ('Annu',20, 105, 'MGMT')")
c.execute("INSERT INTO students VALUES ('Ugam',23, 106, 'LOW')")
c.execute("INSERT INTO students VALUES ('Rekha',20, 107, 'LOW')")
c.execute("INSERT INTO students VALUES ('Sanju',24, 108, 'CS')")
c.execute("INSERT INTO students VALUES ('Dipti',22, 109, 'EE')")
c.execute("INSERT INTO students VALUES ('Yogi',25, 110, 'EE')")


c.execute("SELECT * FROM students")


print ( c.fetchall() )

df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Name","Age","RollNo","Branch"]


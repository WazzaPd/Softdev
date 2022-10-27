#Flying Karate Masters: Matthew Yee, Kevin li, Joesph Wu
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#2022-10-25

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O



#print(row)

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


command = "CREATE TABLE roster(name TEXT, age INTEGER, id INTEGER PRIMARY KEY);"  #PRIMARY KEY causes table to be sorted by ID number
c.execute(command)    # run SQL statement

with open('students.csv', newline='') as csvfile: #autocloses file after with block is over
    reader = csv.DictReader(csvfile)
    for row in reader:
        val1 = row['name']
        val2 = row['age']
        val3 = row['id']
        command = f"INSERT INTO roster values( '{val1}' , '{val2}' , '{val3}' );"
        #print(c.fetchall())
        #command = "INSERT INTO roster values(" + row['name'] + "," + row['age'] + "," + row['id'] + ");"
        # old method of inserting values (did NOT work)
        c.execute(command)


command = "CREATE TABLE classes(code TEXT, mark INTEGER, id INTEGER);"
c.execute(command)    # run SQL statement

with open('courses.csv', newline='') as csvfile: #autocloses file after with block is over
    reader = csv.DictReader(csvfile)
    for row in reader:
        val1 = row['code']
        val2 = row['mark']
        val3 = row['id']
        command = f"INSERT INTO classes values( '{val1}' , '{val2}' , '{val3}' );"
        c.execute(command)


#==========================================================

#c.fetchall()
db.commit() #save changes
db.close()  #close database



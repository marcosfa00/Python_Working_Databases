#Install & load sqlite3
#!pip install sqlite3  ##Uncomment the code to install sqlite3
import sqlite3
import pandas as pd

conn = sqlite3.connect('INSTRUCTOR.db')
cursor = conn.cursor()

"""CREAMOS LA TABLA DENTRO DE LA BASE DE DATOS, SOBRE LA CUAL VAMSO A TRABAJAR
"""
cursor.execute("DROP TABLE IF EXISTS INSTRUCTOR")

table = """CREATE TABLE IF NOT EXISTS INSTRUCTOR (
            ID INTEGER PRIMARY KEY NOT NULL,
            FNAME VARCHAR(20),
            LNAME VARCHAR(20),
            CITY VARCHAR(20),
            CCODE CHAR(2));"""

cursor.execute(table)

print("Table is Ready")

"""AHORA INSERTAMOS VALORES EN LA TABLA"""
# UN SOLO INSERT
cursor.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')
# DOS INSERTS A LA VEZ
cursor.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')

"""AHORA MOSTRAREMOS LOS DATOS EN LA TABLA"""
statement ='SELECT * FROM INSTRUCTOR'
cursor.execute(statement)
print("All the data")
# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch, if you cant to show all you just have to put fetchAll
output = cursor.fetchall()
for row in output:
  print(row)
print("UPDATED...")
query_update = '''update INSTRUCTOR set CITY='MOOSETOWN' WHERE FNAME = "Rav"'''

cursor.execute(query_update)

cursor.execute(statement)
output = cursor.fetchall()
for i in output:
  print(i)

"""AHORA PROCEDEMOS A CREAR UN DATAFRAME DE LA TABLA"""
dataframe = pd.read_sql(statement, conn)
print(dataframe.head())
# print solo el Apellido
print(dataframe.LNAME[0])

print("SHAPE: ",dataframe.shape)
conn.close()

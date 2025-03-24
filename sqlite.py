import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Vrinda','Data Analysis','B',92)''')
cursor.execute('''Insert Into STUDENT values('Isha','Data Engineer','C',88)''')
cursor.execute('''Insert Into STUDENT values('Siya','Data Science','A',80)''')
cursor.execute('''Insert Into STUDENT values('Prakash','Data Analysis','B',95)''')

print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()
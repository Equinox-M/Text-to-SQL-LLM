import sqlite3 
## connect to SQLite database
connection = sqlite3.connect('student.db')

# Creating a cursor object to insert records 
cursor=connection.cursor()

# Creating a table
table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), MARK INT); 
"""
cursor.execute(table_info)

# Inserting more record into the table
cursor.execute('''INSERT INTO STUDENT values("Alex","Data Science","A","100")''')
cursor.execute('''INSERT INTO STUDENT values("Mark","DEVOPS","C","100")''')
cursor.execute('''INSERT INTO STUDENT values("Brika","Data Science","A","90")''')
cursor.execute('''INSERT INTO STUDENT values("Sam","BI","A","40")''')
cursor.execute('''INSERT INTO STUDENT values("Ahmed","BI","B","65")''')
cursor.execute('''INSERT INTO STUDENT values("Carline","DEVOPS","C","82")''')
cursor.execute('''INSERT INTO STUDENT values("Suzan","Data Governance","B","77")''')
#DIsplay All the records
print('The the inserted records are')
data = cursor.execute(''' SELECT * FROM STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()
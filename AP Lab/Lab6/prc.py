import sqlite3

#Create a connection object
conn = sqlite3.connect('test.db')
print("Opened databse successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS TEXT,
            SALARY REAL);''')
print("Table created successfully")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (1,'Paul',32,'California',20000.00)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (2,'Allen',25,'texas',15000.00)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (3,'Teddy',23,'Norway',20000.00)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (4,'Mark',25,'Rich-Mond',65000.00)");

print("Values Inserted")
cursor = conn.execute("SELECT id,name,address,salary from COMPANY")
for row in cursor:
    print("ID= ",row[0])
    print("Name= ",row[1])
    print("Address= ",row[2])
    print("Salary= ",row[3],"\n")

conn.execute("UPDATE COMPANY set SALARY = 25000.0 where ID=1")
conn.commit
print("After Update: ")
cursor = conn.execute("SELECT id,name,address,salary from COMPANY where ID=1")
for row in cursor:
    print("ID= ",row[0])
    print("Name= ",row[1])
    print("Address= ",row[2])
    print("Salary= ",row[3],"\n")

conn.execute("DELETE from COMPANY where ID=2;")
conn.commit
cursor = conn.execute("SELECT id,name,address,salary from COMPANY")
for row in cursor:
    print("ID= ",row[0])
    print("Name= ",row[1])
    print("Address= ",row[2])
    print("Salary= ",row[3],"\n")
print("Deleted successfully")
conn.close()

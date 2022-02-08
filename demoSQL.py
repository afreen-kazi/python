import mysql.connector

myDatabase = mysql.connector.connect(
    host="localhost",
    username="root",
    password="RIffat1019*",
    database="mydatabase"
)

myCursor = myDatabase.cursor()
myCursor.execute("SHOW DATABASES")
for x in myCursor:
    print(x)
sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
myCursor.execute(sql)
myCursor.execute("SHOW TABLES")
for x in myCursor:
    print(x)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
add = [
    ('Mary', '22B Liege Street'),
    ('Trent', '23 Crawley Road'),
    ('Abhi', 'Sterling Highway'),
    ('Afreen', 'Wellington Station')
]
myCursor.executemany(sql, add)
myDatabase.commit()
print(myCursor.rowcount, "record was inserted")

sql = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
myCursor.execute(sql)

sql = "UPDATE customers SET ID = 101 WHERE name = 'Mary'"
myCursor.execute(sql)
myDatabase.commit()

sql = "SELECT * FROM customers WHERE ID=101"
myCursor.execute(sql)
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

sql = "INSERT INTO customers (name, address, ID) VALUES ('Ravi', 'Cannington', 104)"
myCursor.execute(sql)
myDatabase.commit()
print(myCursor.rowcount, "row inserted")

sql = "UPDATE customers SET id = 102 WHERE name = 'Trent'"
myCursor.execute(sql)
myDatabase.commit()

sql2 = "UPDATE customers SET id = 103 WHERE name = 'Afreen'"
myCursor.execute(sql2)
myDatabase.commit()

sql3 = "SELECT * FROM customers"
myCursor.execute(sql3)
myResult = myCursor.fetchall()
for x in myResult:
    print(x)








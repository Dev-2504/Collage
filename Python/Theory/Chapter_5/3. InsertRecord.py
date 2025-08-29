import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "database_name"
)

mycursor = mydb.cursor()

querysyntax = "INSERT INTO table_name (column_name, column_name) VALUES (%s, %s)"
query = "INSERT INTO students (name, age) VALUES (%s, %s)"
value = ("Dev",20)

mycursor.execute(query,value)

mydb.commit()

mydb.close()
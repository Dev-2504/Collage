import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "database_name"
)

mycursor = mydb.cursor()

querysyntax = "CREATE TABLE table_name(column_name datatype constraints, column_name datatype constraints)"
query = "CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
value = ("Dev",20)

mycursor.execute(query)

mydb.commit()

mydb.close()
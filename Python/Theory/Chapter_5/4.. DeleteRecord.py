import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "database_name"
)

mycursor = mydb.cursor()

querysyntax = "DELETE FROM table_name WHERE column_name = %s"
query = "DELETE FROM students WHERE id = %s"
value = (1,)

mycursor.execute(query,value)

mydb.commit()

mydb.close()
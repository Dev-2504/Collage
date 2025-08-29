import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "database_name"
)

mycursor = mydb.cursor()

querysyntax = "UPDATE table_name SET column_name = %s, column_name = %s WHERE column_name = %s"
query = "UPDATE students SET name = %s, age = %s WHERE id = %s"
value = (1,)

mycursor.execute(query,value)

mydb.commit()

mydb.close()
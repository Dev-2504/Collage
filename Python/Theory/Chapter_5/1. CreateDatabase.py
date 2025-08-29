import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)

mycursor = mydb.cursor()

query = "CREATE DATABASE database_name"

mycursor.execute(query)

mydb.commit()

mydb.close()
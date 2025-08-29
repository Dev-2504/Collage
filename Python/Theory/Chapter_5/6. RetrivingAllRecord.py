import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "database_name"
)

mycursor = mydb.cursor()

query = "SELECT * FROM table_name"

mycursor.execute(query)

result = mycursor.fetchall()

for row in result:
    print(row)


mydb.close()
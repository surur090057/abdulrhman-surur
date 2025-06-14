import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Aziz112211'
)

cursorObject = database.cursor()

cursorObject.execute("create database clubmng")

print("all done")
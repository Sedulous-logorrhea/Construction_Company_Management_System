import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Sedulous')
mycursor = mydb.cursor()
mycursor.execute("Create database CDBM")
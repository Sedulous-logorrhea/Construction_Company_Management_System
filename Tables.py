import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user="root",
    password="Sedulous",
    database="CDBM"
)
mycursor = mydb.cursor()
execute = [
    "CREATE TABLE Vendor(Name VARCHAR(50), Phone BIGINT , Email VARCHAR(50), ShopName VARCHAR(50), Address VARCHAR(50), Items VARCHAR(50), PRIMARY KEY(Name, Phone))",
    "CREATE TABLE Project(ProjectNumber INT, CustomerName VARCHAR(100), CustomerNumber BIGINT, VendorNumber BIGINT, Item INT, Details VARCHAR(50), PRIMARY KEY(ProjectNumber, CustomerName,CustomerNumber))",
    "CREATE TABLE Payment(Name VARCHAR(50), Phone BIGINT, Address VARCHAR(50), Item VARCHAR(50), PRIMARY KEY(Name, Phone))"
]

for i in execute :
    mycursor.execute(i)

mydb.commit()
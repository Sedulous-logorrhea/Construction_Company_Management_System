import mysql.connector as ms
import time

mydb = ms.connect(host='localhost',
                  user='root',
                  password='Sedulous')
if not mydb.is_connected():
    print('Could not connect to database Assignment')
    print('Exiting ......')
    time.sleep(3)
    exit()
else:
    mycursor = mydb.cursor()

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sedulous",
    database = "CCDBMS" )
mycursor = mydb.cursor()

def NeedItem() :
    global tItem, tQuantity, tOT
    myCursor.execute("SELECT * FROM Item")
    my_wo = tkinter.Tk()
    my_wo.title("Available Items")
    my_wo.geometry("250x250")
    i=0
    for Item in myCursor:
        for j in range(len(Item)):
            e = Entry(my_wo, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, Item[j])
        i+=1
    my_w = tkinter.Tk()
    my_w.geometry("250x250")
    my_w.title("Buy Items")
    l0 = tkinter.Label(my_w,  text='Needs Items',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Item Number : ', width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tItem = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tItem.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Quantity : ', width=10,anchor="c" )
    l2.grid(row=4,column=1)
    tQuantity = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tQuantity.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Order : ', width=10,anchor="c")
    l3.grid(row=5,column=1)
    tOT = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tOT.grid(row=5,column=2)
    b1 = tkinter.Button(my_w,  text='Buy', width=10,command=lambda: delete_data_item())
    b1.grid(row=7,column=2)
def delete_data_item() :
    my_name = tItem.get("1.0",END)
    query="DELETE FROM `Item` WHERE ItemNumber = %s"
    myCursor.execute(query,(my_name,))
    db_connection.commit()
    tItem.delete('1.0',END)
    tQuantity.delete('1.0',END)
    tOT.delete('1.0',END)
    print("Query executed")

def SellsItems() :
    global t1, t2, t3, t4
    my_w = tkinter.Tk()
    my_w.geometry("450x450")
    my_w.title("Needs Items")
    l0 = tkinter.Label(my_w,  text='Needs Items',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Item Number : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    t1 = tkinter.Text(my_w,  height=1, width=10,bg='white')
    t1.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Quantity : ',width=10,anchor="c" )
    l2.grid(row=4,column=1)
    t2 = tkinter.Text(my_w,  height=1, width=10,bg='white')
    t2.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Price : ', width=10,anchor="c")
    l3.grid(row=5,column=1)
    t3 = tkinter.Text(my_w,  height=1, width=10,bg='white')
    t3.grid(row=5,column=2)
    l4 = tkinter.Label(my_w,  text='Order : ', width=10,anchor="c")
    l4.grid(row=6,column=1)
    t4 = tkinter.Text(my_w,  height=1, width=10,bg='white')
    t4.grid(row=6,column=2)
    b1 = tkinter.Button(my_w,  text='Put the item on sale',width=15, command=lambda: add_data_item())
    b1.grid(row=7,column=2)

def add_data_item() :
    my_name = t1.get("1.0",END)
    my_class = t2.get("1.0",END)
    my_mark = t3.get("1.0",END)
    my_gender = t4.get("1.0",END)
    query="INSERT INTO  `Item`(`ItemNumber` ,`Quantity` ,`Price` ,`OrderItem`) VALUES(%s,%s,%s,%s)"
    my_data=(my_name,my_class,my_mark,my_gender)
    myCursor.execute(query,my_data)
    db_connection.commit()
    t1.delete('1.0',END)
    t2.delete('1.0',END)
    t3.delete('1.0',END)
    t4.delete('1.0',END)
    print("Query executed")

def MakePayment() :
    global tNamePay, tPhonePay, tAddressPay, tItemPay
    myCursor.execute("SELECT * FROM Payment")
    my_wo = tkinter.Tk()
    my_wo.title("Requested payments ")
    my_wo.geometry("250x250")
    i=0
    for Item in myCursor:
        for j in range(len(Item)):
            e = Entry(my_wo, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, Item[j])
        i=i+1
    my_w = tkinter.Tk()
    my_w.geometry("250x250")
    my_w.title("Pay")
    l0 = tkinter.Label(my_w,  text='Make Payment',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Name : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tNamePay = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tNamePay.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Phone : ', width=10,anchor="c")
    l2.grid(row=4,column=1)
    tPhonePay = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tPhonePay.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Address : ',width=10,anchor="c" )
    l3.grid(row=5,column=1)
    tAddressPay = tkinter.Text(my_w,  height=1,width=10,bg='white')
    tAddressPay.grid(row=5,column=2)
    l3 = tkinter.Label(my_w,  text='Item : ',width=10,anchor="c" )
    l3.grid(row=5,column=1)
    tItemPay = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tItemPay.grid(row=5,column=2)
    b1 = tkinter.Button(my_w,  text='Pay', width=10,command=lambda: pay())
    b1.grid(row=7,column=2)
    print('Make payment')
def pay() :
    my_name = tNamePay.get("1.0",END)
    my_phone = tPhonePay.get("1.0",END)
    query="DELETE FROM 'Payment' WHERE Name = %s AND Phone = %s"
    myCursor.execute(query,(my_name, my_phone,))
    db_connection.commit()
    tNamePay.delete('1.0',END)
    tPhonePay.delete('1.0',END)
    tAddressPay.delete('1.0',END)
    tItemPay.delete('1.0',END)
    print("Query executed")

def TakePayments() :
    global tNameReq, tPhoneReq, tAddressReq, tItemReq
    my_w = tkinter.Tk()
    my_w.geometry("300x300")
    my_w.title("Request Payment")
    l0 = tkinter.Label(my_w,  text='Request Payments',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Customer Name : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tNameReq = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tNameReq.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Customer Phone: ',width=10,anchor="c" )
    l2.grid(row=4,column=1)
    tPhoneReq = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tPhoneReq.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Customer Address : ',width=10,anchor="c" )
    l3.grid(row=5,column=1)
    tAddressReq = tkinter.Text(my_w,  height=1,width=10,bg='white')
    tAddressReq.grid(row=5,column=2)
    l4 = tkinter.Label(my_w,  text='Ordered Item : ',width=10,anchor="c" )
    l4.grid(row=6,column=1)
    tItemReq = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tItemReq.grid(row=6,column=2)
    b1 = tkinter.Button(my_w,  text='Put the item on sale',width=25, command=lambda: requestPayment())
    b1.grid(row=7,column=2)
def requestPayment() :
    my_name = tNameReq.get("1.0",END)
    my_class = tPhoneReq.get("1.0",END)
    my_mark = tAddressReq.get("1.0",END)
    my_gender = tItemReq.get("1.0",END)
    query="INSERT INTO  'Payment' (`Name` ,`Phone` ,`Address` ,`Item`) VALUES (%s,%s,%s,%s)"
    my_data=(my_name,my_class,my_mark,my_gender)
    myCursor.execute(query,my_data)
    db_connection.commit()
    tNameReq.delete('1.0',END)
    tPhoneReq.delete('1.0',END)
    tAddressReq.delete('1.0',END)
    tItemReq.delete('1.0',END)
    print("Query executed")

def PlaceOrder() :
    global OrderCname, OrderPhone, OrderAddress, OrderAmount,OrderProject, OrderItem
    my_w = tkinter.Tk()
    my_w.geometry("250x250")
    my_w.title("Place Order")
    l0 = tkinter.Label(my_w,  text='Place Order',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Customer Name : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    OrderCname = tkinter.Text(my_w,  height=1,width=10,bg='white')
    OrderCname.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Phone : ', width=10,anchor="c")
    l2.grid(row=4,column=1)
    OrderPhone = tkinter.Text(my_w,  height=1,width=10,bg='white')
    OrderPhone.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Address : ',width=10,anchor="c" )
    l3.grid(row=5,column=1)
    OrderAddress = tkinter.Text(my_w,  height=1,width=10,bg='white')
    OrderAddress.grid(row=5,column=2)
    l4 = tkinter.Label(my_w,  text='Amount : ',width=10,anchor="c" )
    l4.grid(row=6,column=1)
    OrderAmount = tkinter.Text(my_w,  height=1,width=10,bg='white')
    OrderAmount.grid(row=6,column=2)
    l5 = tkinter.Label(my_w,  text='Project : ',width=10,anchor="c" )
    l5.grid(row=7,column=1)
    OrderProject = tkinter.Text(my_w,  height=1,width=10,bg='white')
    OrderProject.grid(row=7,column=2)
    l6 = tkinter.Label(my_w,  text='Item : ',width=10,anchor="c" )
    l6.grid(row=8,column=1)
    OrderItem = tkinter.Text(my_w,  height=1, width=10,bg='white')
    OrderItem.grid(row=8,column=2)
    b1 = tkinter.Button(my_w,  text='Place Order', width=10,command=lambda: give_order())
    b1.grid(row=10,column=2)
    print('Place order')
def give_order() :
    Cname = OrderCname.get('1.0',END)
    Phone = OrderPhone.get('1.0',END)
    Address = OrderAddress.get('1.0',END)
    Amount = OrderAmount.get('1.0',END)
    Project = OrderProject.get('1.0',END)
    Item = OrderItem.get('1.0',END)
    query = 'INSERT INTO OrderTable VALUES (%s,%s,%s,%s,%s,%s)'
    myData = (Cname, Phone, Address, Amount, Project, Item)
    myCursor.execute(query, myData)
    db_connection.commit()
    OrderCname.delete('1.0', END)
    OrderPhone.delete('1.0', END)
    OrderAddress.delete('1.0', END)
    OrderAmount.delete('1.0', END)
    OrderProject.delete('1.0', END)
    OrderItem.delete('1.0', END)
    print('Give order')

def CompleteOrder() :
    global CompCustName, CompCustPhone
    myCursor.execute("SELECT * FROM OrderTable")
    my_wo = tkinter.Tk()
    my_wo.title("Requested orders ")
    my_wo.geometry("250x250")
    i=0
    for Project in myCursor:
        for j in range(len(Project)):
            e = Entry(my_wo, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, Project[j])
        i=i+1
    print('Complete order')
    my_w = tkinter.Tk()
    my_w.geometry("250x250")
    my_w.title("Complete Order")
    l0 = tkinter.Label(my_w,  text='Complete Order',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Customer Name : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    CompCustName = tkinter.Text(my_w,  height=1,width=10,bg='white')
    CompCustName.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Phone : ', width=10,anchor="c")
    l2.grid(row=4,column=1)
    CompCustPhone = tkinter.Text(my_w,  height=1,width=10,bg='white')
    CompCustPhone.grid(row=4,column=2)
    b1 = tkinter.Button(my_w,  text='Complete Order', width=40,command=lambda: comp_the_order())
    b1.grid(row=7,column=2)
def comp_the_order() :
    CustName = CompCustName.get('1.0', END)
    CustPhone = CompCustPhone.get('1.0', END)
    query = "DELETE FROM OrderTable WHERE Phone = %s"
    myData = (CustPhone,)
    myCursor.execute(query, myData)
    db_connection.commit()
    CompCustName.delete('1.0', END)
    CompCustPhone.delete('1.0', END)

def GiveProject() :
    global tGiveProj, tGiveName, tGiveNum, tGiveVend, tGiveItem,tGiveDetails
    my_w = tkinter.Tk()
    my_w.geometry("300x300")
    my_w.title("Give Project")
    l0 = tkinter.Label(my_w,  text='Give Project',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Project Number : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tGiveProj = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tGiveProj.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Customer Name : ',width=10,anchor="c" )
    l2.grid(row=4,column=1)
    tGiveName = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tGiveName.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Customer Number : ',width=10,anchor="c" )
    l3.grid(row=5,column=1)
    tGiveNum = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tGiveNum.grid(row=5,column=2)
    l4 = tkinter.Label(my_w,  text='Vendor Number : ',width=10,anchor="c" )
    l4.grid(row=6,column=1)
    tGiveVend = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tGiveVend.grid(row=6,column=2)
    l5 = tkinter.Label(my_w,  text='Item : ',width=10,anchor="c" )
    l5.grid(row=7,column=1)
    tGiveItem = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tGiveItem.grid(row=7,column=2)
    l6 = tkinter.Label(my_w,  text='Details : ',width=10,anchor="c" )
    l6.grid(row=8,column=1)
    tGiveDetails = tkinter.Text(my_w,  height=1,width=10,bg='white')
    tGiveDetails.grid(row=8,column=2)
    b1 = tkinter.Button(my_w,  text='Give Project', width=10,command=lambda: giveTheProject())
    b1.grid(row=10,column=2)
    print('Give project')
def giveTheProject() :
    my_name = tGiveProj.get("1.0",END)
    my_class = tGiveName.get("1.0",END)
    my_mark = tGiveNum.get("1.0",END)
    my_gender = tGiveVend.get("1.0",END)
    my_item = tGiveItem.get("1.0",END)
    my_details = tGiveDetails.get("1.0",END)
    query=("INSERT INTO  `Project` (`ProjectNumber` ,`CustomerName`,`CustomerNumber` ,`VendorNumber`, `Item`, `Details`) VALUES (%s,%s,%s,%s,%s,%s)")
    my_data=(my_name,my_class,my_mark,my_gender, my_item,my_details)
    myCursor.execute(query,my_data)
    db_connection.commit()
    tGiveProj.delete('1.0',END)
    tGiveName.delete('1.0',END)
    tGiveNum.delete('1.0',END)
    tGiveVend.delete('1.0',END)
    tGiveItem.delete('1.0',END)
    tGiveDetails.delete('1.0',END)
    print("Query executed")

def TakesProjects() :
    global tTakeProj, tTakeName, tTakeDetails
    myCursor.execute("SELECT * FROM Project")
    my_wo = tkinter.Tk()
    my_wo.title("Requested projects ")
    my_wo.geometry("250x250")
    i=0
    for Project in myCursor:
        for j in range(len(Project)):
            e = Entry(my_wo, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, Project[j])
        i=i+1
    my_w = tkinter.Tk()
    my_w.geometry("250x250")
    my_w.title("Take Project")
    l0 = tkinter.Label(my_w,  text='Take Project',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Project Number : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tTakeProj = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tTakeProj.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Vendor Name : ',width=10,anchor="c" )
    l2.grid(row=4,column=1)
    tTakeName = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tTakeName.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Give details : ',width=10,anchor="c" )
    l3.grid(row=4,column=1)
    tTakeDetails = tkinter.Text(my_w,  height=1,width=10,bg='white')
    tTakeDetails.grid(row=4,column=2)
    b1 = tkinter.Button(my_w,  text='Take the project', width=25,command=lambda: taketheProj())
    b1.grid(row=6,column=2)
def taketheProj() :
    my_class = tTakeProj.get("1.0",END)
    my_mark = tTakeDetails.get("1.0",END)
    query = ('''UPDATE Project SET Details = %s WHERE ProjectNumber= %s''')
    my_data = (my_mark,my_class,)
    myCursor.execute(query,my_data)
    db_connection.commit()
    tTakeName.delete('1.0',END)
    tTakeDetails.delete('1.0',END)
    tTakeProj.delete('1.0',END)
    print("Query executed")

def CompletesProjects() :
    global tCompProj, tCompName, tCompDetails
    myCursor.execute("SELECT * FROM Project")
    my_wo = tkinter.Tk()
    my_wo.title("Requested projects ")
    my_wo.geometry("250x250")
    i=0
    for Project in myCursor:
        for j in range(len(Project)):
            e = Entry(my_wo, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, Project[j])
        i=i+1
    my_w = tkinter.Tk()
    my_w.geometry("250x250")
    my_w.title("Take Project")
    l0 = tkinter.Label(my_w,  text='Project Completed!',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Project Number : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tCompProj = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tCompProj.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Vendor Name : ',width=10,anchor="c" )
    l2.grid(row=4,column=1)
    tCompName = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tCompName.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Give details : ',width=10,anchor="c" )
    l3.grid(row=4,column=1)
    tCompDetails = tkinter.Text(my_w,  height=1,width=10,bg='white')
    tCompDetails.grid(row=4,column=2)
    b1 = tkinter.Button(my_w,  text='Completed', width=10,command=lambda: compTheProj())
    b1.grid(row=6,column=2)
def compTheProj() :
    my_class = tCompProj.get("1.0",END)
    query = "DELETE FROM Project WHERE ProjectNumber = %s"
    my_data = (my_class,)
    myCursor.execute(query,my_data)
    db_connection.commit()
    tCompName.delete('1.0',END)
    tCompDetails.delete('1.0',END)
    tCompProj.delete('1.0',END)
    print("Query executed")

import tkinter
from tkinter import *
import mysql.connector

db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sedulous",
    database = "CCDBMS" )
myCursor = db_connection.cursor()
tItem = None
tQuantity = None
tOT = None
tNamePay = None
tPhonePay = None
tAddressPay = None
tItemPay = None
OrderCname = None
OrderPhone = None
OrderAddress = None
OrderAmount = None
OrderProject = None
OrderItem = None
tGiveProj = None
tGiveName = None
tGiveNum = None
tGiveVend = None
tGiveItem = None
tGiveDetails = None
tNameReq = None
tPhoneReq = None
tAddressReq = None
tItemReq = None
t1 = None
t2 = None
t3 = None
t4 = None
tCompProj = None
tCompName = None
tCompDetails = None
tTakeProj = None
tTakeName = None
tTakeDetails = None
CompCustName = None
CompCustPhone = None
main = tkinter.Tk()
main.title('Construction Company Database Management System')
main.configure(bg='Yellow')
main.geometry("400x1366")
def CustomerDial() :
    Customer = tkinter.Tk()
    Customer.configure(bg='wheat')
    Customer.title('Customer Space')
    NeedsItems = tkinter.Button(Customer, text = "Needs Items",command = NeedItem)
    MakesPayments = tkinter.Button(Customer, text = "Makes Payments", command = MakePayment)
    PlacesOrders = tkinter.Button(Customer, text = "Place Orders",command = PlaceOrder)
    GivesProjects = tkinter.Button(Customer, text = "Give Projects", command = GiveProject)
    NeedsItems.pack(padx=100, pady=100)
    MakesPayments.pack(padx=100, pady=100)
    PlacesOrders.pack(padx=100, pady=100)
    GivesProjects.pack(padx=100, pady=100)

def NeedItem() :
    global tItem, tQuantity, tOT
    myCursor.execute("SELECT * FROM Item")
    my_wo = tkinter.Tk()
    my_wo.title("Available Items")
    my_wo.geometry("1366x400")
    i=0
    for Item in myCursor:
        for j in range(len(Item)):
            e = Entry(my_wo, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, Item[j])
        i=i+1
    my_w = tkinter.Tk()
    my_w.geometry("1366x400")
    my_w.title("Buy Items")
    l0 = tkinter.Label(my_w,  text='Needs Items',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Item Number : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tItem = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tItem.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Quantity : ', width=10,anchor="c" )
    l2.grid(row=4,column=1)
    tQuantity = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tQuantity.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Order : ', width=10,anchor="c")
    l3.grid(row=5,column=1)
    tOT = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tOT.grid(row=5,column=2)
    b1 = tkinter.Button(my_w,  text='Buy', width=10,command=lambda: delete_data_item())
    b1.grid(row=7,column=2)
def delete_data_item() :
    my_name = tItem.get("1.0",END)
    query="DELETE FROM `Item` WHERE ItemNumber = %s"
    myCursor.execute(query,(my_name,))
    db_connection.commit()
    tItem.delete('1.0',END)
    tQuantity.delete('1.0',END)
    tOT.delete('1.0',END)
    print("Query executed")
def MakePayment() :
    global tNamePay, tPhonePay, tAddressPay, tItemPay
    myCursor.execute("SELECT * FROM Payment")
    my_wo = tkinter.Tk()
    my_wo.title("Requested payments ")
    my_wo.geometry("1366x400")
    i=0
    for Item in myCursor:
        for j in range(len(Item)):
            e = Entry(my_wo, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, Item[j])
        i=i+1
    my_w = tkinter.Tk()
    my_w.geometry("1366x400")
    my_w.title("Pay")
    l0 = tkinter.Label(my_w,  text='Make Payment',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Name : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tNamePay = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tNamePay.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Phone : ', width=10,anchor="c")
    l2.grid(row=4,column=1)
    tPhonePay = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tPhonePay.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Address : ',width=10,anchor="c" )
    l3.grid(row=5,column=1)
    tAddressPay = tkinter.Text(my_w,  height=1,width=10,bg='white')
    tAddressPay.grid(row=5,column=2)
    l3 = tkinter.Label(my_w,  text='Item : ',width=10,anchor="c" )
    l3.grid(row=5,column=1)
    tItemPay = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tItemPay.grid(row=5,column=2)
    b1 = tkinter.Button(my_w,  text='Pay', width=10,command=lambda: pay())
    b1.grid(row=7,column=2)
    print('Make payment')
def pay() :
    my_name = tNamePay.get("1.0",END)
    my_phone = tPhonePay.get("1.0",END)
    query="DELETE FROM `Payment` WHERE Name = %s AND Phone = %s"
    myCursor.execute(query,(my_name, my_phone,))
    db_connection.commit()
    tNamePay.delete('1.0',END)
    tPhonePay.delete('1.0',END)
    tAddressPay.delete('1.0',END)
    tItemPay.delete('1.0',END)
    print("Query executed")
def PlaceOrder() :
    global OrderCname, OrderPhone, OrderAddress, OrderAmount,OrderProject, OrderItem
    my_w = tkinter.Tk()
    my_w.geometry("1366x400")
    my_w.title("Place Order")
    l0 = tkinter.Label(my_w,  text='Place Order',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Customer Name : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    OrderCname = tkinter.Text(my_w,  height=1,width=10,bg='white')
    OrderCname.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Phone : ', width=10,anchor="c")
    l2.grid(row=4,column=1)
    OrderPhone = tkinter.Text(my_w,  height=1,width=10,bg='white')
    OrderPhone.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Address : ',width=10,anchor="c" )
    l3.grid(row=5,column=1)
    OrderAddress = tkinter.Text(my_w,  height=1,width=10,bg='white')
    OrderAddress.grid(row=5,column=2)
    l4 = tkinter.Label(my_w,  text='Amount : ',width=10,anchor="c" )
    l4.grid(row=6,column=1)
    OrderAmount = tkinter.Text(my_w,  height=1,width=10,bg='white')
    OrderAmount.grid(row=6,column=2)
    l5 = tkinter.Label(my_w,  text='Project : ',width=10,anchor="c" )
    l5.grid(row=7,column=1)
    OrderProject = tkinter.Text(my_w,  height=1,width=10,bg='white')
    OrderProject.grid(row=7,column=2)
    l6 = tkinter.Label(my_w,  text='Item : ',width=10,anchor="c" )
    l6.grid(row=8,column=1)
    OrderItem = tkinter.Text(my_w,  height=1, width=10,bg='white')
    OrderItem.grid(row=8,column=2)
    b1 = tkinter.Button(my_w,  text='Place Order', width=10,command=lambda: give_order())
    b1.grid(row=10,column=2)
    print('Place order')
def give_order() :
    Cname = OrderCname.get('1.0',END)
    Phone = OrderPhone.get('1.0',END)
    Address = OrderAddress.get('1.0',END)
    Amount = OrderAmount.get('1.0',END)
    Project = OrderProject.get('1.0',END)
    Item = OrderItem.get('1.0',END)
    query = """INSERT INTO OrderTable VALUES (%s,%s,%s,%s,%s,%s)"""
    myData = (Cname, Phone, Address, Amount, Project, Item)
    myCursor.execute(query, myData)
    db_connection.commit()
    OrderCname.delete('1.0', END)
    OrderPhone.delete('1.0', END)
    OrderAddress.delete('1.0', END)
    OrderAmount.delete('1.0', END)
    OrderProject.delete('1.0', END)
    OrderItem.delete('1.0', END)
    print('Give order')
def GiveProject() :
    global tGiveProj, tGiveName, tGiveNum, tGiveVend, tGiveItem,tGiveDetails
    my_w = tkinter.Tk()
    my_w.geometry("300x300")
    my_w.title("Give Project")
    l0 = tkinter.Label(my_w,  text='Give Project',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Project Number : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tGiveProj = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tGiveProj.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Customer Name : ',width=10,anchor="c" )
    l2.grid(row=4,column=1)
    tGiveName = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tGiveName.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Customer Number : ',width=10,anchor="c" )
    l3.grid(row=5,column=1)
    tGiveNum = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tGiveNum.grid(row=5,column=2)
    l4 = tkinter.Label(my_w,  text='Vendor Number : ',width=10,anchor="c" )
    l4.grid(row=6,column=1)
    tGiveVend = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tGiveVend.grid(row=6,column=2)
    l5 = tkinter.Label(my_w,  text='Item : ',width=10,anchor="c" )
    l5.grid(row=7,column=1)
    tGiveItem = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tGiveItem.grid(row=7,column=2)
    l6 = tkinter.Label(my_w,  text='Details : ',width=10,anchor="c" )
    l6.grid(row=8,column=1)
    tGiveDetails = tkinter.Text(my_w,  height=1,width=10,bg='white')
    tGiveDetails.grid(row=8,column=2)
    b1 = tkinter.Button(my_w,  text='Give Project', width=10,command=lambda: giveTheProject())
    b1.grid(row=10,column=2)
    print('Give project')
def giveTheProject() :
    my_name = tGiveProj.get("1.0",END)
    my_class = tGiveName.get("1.0",END)
    my_mark = tGiveNum.get("1.0",END)
    my_gender = tGiveVend.get("1.0",END)
    my_item = tGiveItem.get("1.0",END)
    my_details = tGiveDetails.get("1.0",END)
    query="INSERT INTO  `Project` (`ProjectNumber` ,`CustomerName`,`CustomerNumber` ,`VendorNumber`, `Item`, `Details`) VALUES (%s,%s,%s,%s,%s,%s)"
    my_data=(my_name,my_class,my_mark,my_gender, my_item,my_details)
    myCursor.execute(query,my_data)
    db_connection.commit()
    tGiveProj.delete('1.0',END)
    tGiveName.delete('1.0',END)
    tGiveNum.delete('1.0',END)
    tGiveVend.delete('1.0',END)
    tGiveItem.delete('1.0',END)
    tGiveDetails.delete('1.0',END)
    print("Query executed")
def VendorDial() :
    Vendor = tkinter.Tk()
    Vendor.configure(bg='wheat')
    Vendor.title('Vendor Functions')
    TakesPayment = tkinter.Button(Vendor, text = "Take Payments",command = TakePayments)
    SellsItem = tkinter.Button(Vendor, text = "Sell Items",command = SellsItems)
    CompletesOrder = tkinter.Button(Vendor, text = "Complete Order", command = CompleteOrder)
    TakesProject = tkinter.Button(Vendor, text = "Takes Projects",command = TakesProjects)
    CompletesProject = tkinter.Button(Vendor, text = "Complete Project", command = CompletesProjects)
    TakesPayment.pack(padx=20, pady=20)
    SellsItem.pack(padx=20, pady=20)
    CompletesOrder.pack(padx=20, pady=20)
    TakesProject.pack(padx=20, pady=20)
    CompletesProject.pack(padx=20, pady=20)
def TakePayments() :
    global tNameReq, tPhoneReq, tAddressReq, tItemReq
    my_w = tkinter.Tk()
    my_w.geometry("300x300")
    my_w.title("Request Payment")
    l0 = tkinter.Label(my_w,  text='Request Payments',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Customer Name : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tNameReq = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tNameReq.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Customer Phone: ',width=10,anchor="c" )
    l2.grid(row=4,column=1)
    tPhoneReq = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tPhoneReq.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Customer Address : ',width=10,anchor="c" )
    l3.grid(row=5,column=1)
    tAddressReq = tkinter.Text(my_w,  height=1,width=10,bg='white')
    tAddressReq.grid(row=5,column=2)
    l4 = tkinter.Label(my_w,  text='Ordered Item : ',width=10,anchor="c" )
    l4.grid(row=6,column=1)
    tItemReq = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tItemReq.grid(row=6,column=2)
    b1 = tkinter.Button(my_w,  text='Put the item on sale',width=10, command=lambda: requestPayment())
    b1.grid(row=7,column=2)
def requestPayment() :
    my_name = tNameReq.get("1.0",END)
    my_class = tPhoneReq.get("1.0",END)
    my_mark = tAddressReq.get("1.0",END)
    my_gender = tItemReq.get("1.0",END)
    query="INSERT INTO  `Payment`(`Name` ,`Phone` ,`Address` ,`Item`) VALUES (%s,%s,%s,%s)"
    my_data=(my_name,my_class,my_mark,my_gender)
    myCursor.execute(query,my_data)
    db_connection.commit()
    tNameReq.delete('1.0',END)
    tPhoneReq.delete('1.0',END)
    tAddressReq.delete('1.0',END)
    tItemReq.delete('1.0',END)
    print("Query executed")

def SellsItems() :
    global t1, t2, t3, t4
    my_w = tkinter.Tk()
    my_w.geometry("250x250")
    my_w.title("Needs Items")
    l0 = tkinter.Label(my_w,  text='Needs Items',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Item Number : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    t1 = tkinter.Text(my_w,  height=1, width=10,bg='white')
    t1.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Quantity : ',width=10,anchor="c" )
    l2.grid(row=4,column=1)
    t2 = tkinter.Text(my_w,  height=1, width=10,bg='white')
    t2.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Price : ', width=10,anchor="c")
    l3.grid(row=5,column=1)
    t3 = tkinter.Text(my_w,  height=1, width=10,bg='white')
    t3.grid(row=5,column=2)
    l4 = tkinter.Label(my_w,  text='Order : ', width=10,anchor="c")
    l4.grid(row=6,column=1)
    t4 = tkinter.Text(my_w,  height=1, width=10,bg='white')
    t4.grid(row=6,column=2)
    b1 = tkinter.Button(my_w,  text='Put the item on sale',width=10, command=lambda: add_data_item())
    b1.grid(row=7,column=2)
def add_data_item() :
    my_name = t1.get("1.0",END)
    my_class = t2.get("1.0",END)
    my_mark = t3.get("1.0",END)
    my_gender = t4.get("1.0",END)
    query="INSERT INTO  `Item`(`ItemNumber` ,`Quantity` ,`Price` ,`OrderItem`) VALUES(%s,%s,%s,%s)"
    my_data=(my_name,my_class,my_mark,my_gender)
    myCursor.execute(query,my_data)
    db_connection.commit()
    t1.delete('1.0',END)
    t2.delete('1.0',END)
    t3.delete('1.0',END)
    t4.delete('1.0',END)
    print("Query executed")
def CompleteOrder() :
    global CompCustName, CompCustPhone
    myCursor.execute("SELECT * FROM OrderTable")
    my_wo = tkinter.Tk()
    my_wo.title("Requested orders ")
    my_wo.geometry("250x250")
    i=0
    for Project in myCursor:
        for j in range(len(Project)):
            e = Entry(my_wo, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, Project[j])
        i=i+1
    print('Complete order')
    my_w = tkinter.Tk()
    my_w.geometry("250x250")
    my_w.title("Complete Order")
    l0 = tkinter.Label(my_w,  text='Complete Order',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Customer Name : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    CompCustName = tkinter.Text(my_w,  height=1,width=10,bg='white')
    CompCustName.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Phone : ', width=10,anchor="c")
    l2.grid(row=4,column=1)
    CompCustPhone = tkinter.Text(my_w,  height=1,width=10,bg='white')
    CompCustPhone.grid(row=4,column=2)
    b1 = tkinter.Button(my_w,  text='Complete Order', width=40,command=lambda: comp_the_order())
    b1.grid(row=7,column=2)
def comp_the_order() :
    CustName = CompCustName.get('1.0', END)
    CustPhone = CompCustPhone.get('1.0', END)
    query = """DELETE FROM OrderTable WHERE Phone = %s"""
    myData = (CustPhone,)
    myCursor.execute(query, myData)
    db_connection.commit()
    CompCustName.delete('1.0', END)
    CompCustPhone.delete('1.0', END)
def TakesProjects() :
    global tTakeProj, tTakeName, tTakeDetails
    myCursor.execute("SELECT * FROM Project")
    my_wo = tkinter.Tk()
    my_wo.title("Requested projects ")
    my_wo.geometry("250x250")
    i=0
    for Project in myCursor:
        for j in range(len(Project)):
            e = Entry(my_wo, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, Project[j])
        i=i+1
    my_w = tkinter.Tk()
    my_w.geometry("250x250")
    my_w.title("Take Project")
    l0 = tkinter.Label(my_w,  text='Take Project',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Project Number : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tTakeProj = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tTakeProj.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Vendor Name : ',width=10,anchor="c" )
    l2.grid(row=4,column=1)
    tTakeName = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tTakeName.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Give details : ',width=10,anchor="c" )
    l3.grid(row=4,column=1)
    tTakeDetails = tkinter.Text(my_w,  height=1,width=10,bg='white')
    tTakeDetails.grid(row=4,column=2)
    b1 = tkinter.Button(my_w,  text='Take the project', width=10,command=lambda: taketheProj())
    b1.grid(row=6,column=2)
def taketheProj() :
    my_class = tTakeProj.get("1.0",END)
    my_mark = tTakeDetails.get("1.0",END)
    query = """UPDATE Project SET Details = %s WHERE ProjectNumber= %s"""
    my_data = (my_mark,my_class,)
    myCursor.execute(query,my_data)
    db_connection.commit()
    tTakeName.delete('1.0',END)
    tTakeDetails.delete('1.0',END)
    tTakeProj.delete('1.0',END)
    print("Query executed")
def CompletesProjects() :
    global tCompProj, tCompName, tCompDetails
    myCursor.execute("SELECT * FROM Project")
    my_wo = tkinter.Tk()
    my_wo.title("Requested projects ")
    my_wo.geometry("250x250")
    i=0
    for Project in myCursor:
        for j in range(len(Project)):
            e = Entry(my_wo, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, Project[j])
        i=i+1
    my_w = tkinter.Tk()
    my_w.geometry("250x250")
    my_w.title("Take Project")
    l0 = tkinter.Label(my_w,  text='Project Completed!',font=('Helvetica', 16), width=30,anchor="c" )
    l0.grid(row=1,column=1,columnspan=4)
    l1 = tkinter.Label(my_w,  text='Project Number : ',width=10,anchor="c" )
    l1.grid(row=3,column=1)
    tCompProj = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tCompProj.grid(row=3,column=2)
    l2 = tkinter.Label(my_w,  text='Vendor Name : ',width=10,anchor="c" )
    l2.grid(row=4,column=1)
    tCompName = tkinter.Text(my_w,  height=1, width=10,bg='white')
    tCompName.grid(row=4,column=2)
    l3 = tkinter.Label(my_w,  text='Give details : ',width=10,anchor="c" )
    l3.grid(row=4,column=1)
    tCompDetails = tkinter.Text(my_w,  height=1,width=10,bg='white')
    tCompDetails.grid(row=4,column=2)
    b1 = tkinter.Button(my_w,  text='Completed', width=10,command=lambda: compTheProj())
    b1.grid(row=6,column=2)
def compTheProj() :
    my_class = tCompProj.get("1.0",END)
    query = """DELETE FROM Project WHERE ProjectNumber = %s"""
    my_data = (my_class,)
    myCursor.execute(query,my_data)
    db_connection.commit()
    tCompName.delete('1.0',END)
    tCompDetails.delete('1.0',END)
    tCompProj.delete('1.0',END)
    print("Query executed")
def HelloCallBack() :
    C = tkinter.Button(main, text = "Customer", command = CustomerDial, compound = "c",height=10,width=50)
    V = tkinter.Button(main, text = "Vendor", command = VendorDial, compound = "c",height=10,width=50)
    C.pack(padx=20, pady=20)
    V.pack(padx=20, pady=20)
HelloCallBack()
main.mainloop()
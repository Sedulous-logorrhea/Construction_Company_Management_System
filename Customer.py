

from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector as ms
import smtplib
#SQL Connection
db_connection = ms.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "CCDBMS" )
myCursor = db_connection.cursor()

class Customer:
    def __init__(self, root):

        self.root = root
        self.root.title("Customer Space")
        self.root.geometry("1366x700+0+0")  # sze of window
        self.root.resizable(True, True)  # to allow resizing swap False with True
        self.Customer_home()

    def Customer_home(self):  # Login Window
        # Frame for BG image
        Frame_bg = Frame(self.root, bg='white')
        Frame_bg.place(x=0, y=0, height=700, width=1366)  # Frame size same as size of Window

        self.img = ImageTk.PhotoImage(file="Customer_screen.png")
        img = Label(Frame_bg, image=self.img)
        img.place(x=0, y=0, width=1366, height=700)  # img made as a label nd placed on the frame

        # Frame for arranging widgets like Labels, textboxes, command buttons
        frame_input = Frame(self.root, bg='#505050')
        frame_input.place(x=190, y=195, height=400, width=400)

        # Arranging every element onto the frame_input
        NeedsItems = Button(frame_input, text="Need Items", command=self.NeedItem, height=5, width=50)
        MakesPayments = Button(frame_input, text="Makes Payments", command=self.MakePayment, height=5, width=50)
        PlacesOrders = Button(frame_input, text="Place Orders", command=self.PlaceOrder, height=5, width=50)
        GivesProjects = Button(frame_input, text="Give Projects", command=self.GiveProject, height=5, width=50)
        NeedsItems.place(x=20, y=10)
        MakesPayments.place(x=20, y=105)
        PlacesOrders.place(x=20, y=200)
        GivesProjects.place(x=20, y=295)

    def NeedItem(self):
        global ItemNoInput, QuantityInput, OrderInput
        myCursor.execute("SELECT * FROM Item")
        my_wo = Tk()
        my_wo.title("Available Items")
        my_wo.geometry("1366x700")
        '''i = 500
        for Item in myCursor:
            for j in range(len(Item)):
                e = Entry(my_wo, width=30, fg='blue')
                e.place(x=i, column=j+300)
                e.insert(END, Item[j])
            i = i + 50'''

        NeedItemLabel = Label(my_wo, text='Needs Items', font=('Organic', 32),width=30,height=3, anchor="c")
        NeedItemLabel.place(x=400,y=10)

        ItemNumberLabel = Label(my_wo, text='Item Number : ',font=('Times',20),width=30,height=3)
        ItemNumberLabel.place(x=360,y=125)
        ItemNoInput = Text(my_wo, width=30,height=3, bg='white')
        ItemNoInput.place(x=670,y=135)

        QuantityLabel = Label(my_wo, text='Quantity : ',font=('Times',20), width=30,height=3)
        QuantityLabel.place(x=30,y=175)
        QuantityInput = Text(my_wo,width=30,height=3,bg='white')
        QuantityInput.place(x=340,y=195)

        OrderLabel = Label(my_wo, text='Order : ',font=('Times',20),width=30,height=3)
        OrderLabel.place(x=30,y=235)
        OrderInput= Text(my_wo, width=30,height=3, bg='white')
        OrderInput.place(x=340,y=260)

        b1 = Button(my_wo, text='Buy', width=100, height=3, bg='white',command=self.delete_data_item())
        b1.place(x=670,y=135)
        b2= Button(my_wo, text='tEST', width=100, height=3, bg='RED', command=self.delete_data_item())
        b2.place(x=0, y=0)
    def MakePayment(self):
        pass
    def PlaceOrder(self):
        pass
    def GiveProject(self):
        pass

    def delete_data_item(self):#NeedItem
        my_name = ItemNoInput.get("1.0", END)
        query = "DELETE FROM `Item` WHERE ItemNumber = %s"
        myCursor.execute(query, (my_name,))
        db_connection.commit()
        ItemNoInput.delete('1.0', END)
        QuantityInput.delete('1.0', END)
        OrderInput.delete('1.0', END)
        print("Query executed")


        print("Query executed")

root = Tk()
object = Customer(root)

root.mainloop()

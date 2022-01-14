from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector as ms
import smtplib


class Vendor:
    def __init__(self, root):

        self.root = root
        self.root.title("Vendor Functions")
        self.root.geometry("1366x700+0+0")  # sze of window
        self.root.resizable(True, True)  # to allow resizing swap False with True
        self.Customer_home()

    def Customer_home(self):  # Login Window
        # Frame for BG image
        Frame_bg = Frame(self.root, bg='white')
        Frame_bg.place(x=0, y=0, height=700, width=1366)  # Frame size same as size of Window

        self.img = ImageTk.PhotoImage(file="Vendor_Window.png")
        img = Label(Frame_bg, image=self.img)
        img.place(x=0, y=0, width=1366, height=700)  # img made as a label nd placed on the frame

        # Frame for arranging widgets like Labels, textboxes, command buttons
        frame_input = Frame(self.root, bg='#505050')
        frame_input.place(x=190, y=195, height=400, width=400)

        # Arranging every element onto the frame_input
        NeedsItems = Button(frame_input, text="Need Items", command=self.NeedItem, height=5, width=40)
        MakesPayments = Button(frame_input, text="Makes Payments", command=self.MakePayment, height=5, width=40)
        PlacesOrders = Button(frame_input, text="Place Orders", command=self.PlaceOrder, height=5, width=40)
        GivesProjects = Button(frame_input, text="Give Projects", command=self.GiveProject, height=5, width=40)
        NeedsItems.place(x=20, y=10)
        MakesPayments.place(x=20, y=105)
        PlacesOrders.place(x=20, y=200)
        GivesProjects.place(x=20, y=295)

    def NeedItem(self):
        pass
    def MakePayment(self):
        pass
    def PlaceOrder(self):
        pass
    def GiveProject(self):
        pass


root = Tk()
object = Vendor(root)

root.mainloop()
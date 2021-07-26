from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


class Login:
    def __init__(self, root):

        self.root = root
        self.root.title("Login and registration system for Apps")
        self.root.geometry("1366x700+0+0")  # sze of window
        self.root.resizable(False, False)  # to allow resizing swap False with True
        self.loginform()

    def loginform(self):  # Login Window
        # Frame for BG image
        Frame_login = Frame(self.root, bg='white')
        Frame_login.place(x=0, y=0, height=700, width=1366)  # Frame size same as size of Window

        self.img = ImageTk.PhotoImage(file="Dubai Skyline.jpg")
        img = Label(Frame_login, image=self.img)
        img.place(x=0, y=0, width=1366, height=700)  # img made as a label nd placed on the frame

        # Frame for arranging widgets like Labels, textboxes
        frame_input = Frame(self.root, bg='white')
        frame_input.place(x=320, y=130, height=450, width=350)

        # Arranging every element onto the frame
        label1 = Label(frame_input, text="Login Here", font=('impact', 32, 'bold'), fg="black", bg='white')
        label1.place(x=75, y=20)

        label2 = Label(frame_input, text="Username", font=("Goudy old style", 20, "bold"), fg='#40e0d0', bg='white')
        label2.place(x=30, y=95)

        self.email_txt = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.email_txt.place(x=30, y=145, width=270, height=35)

        label3 = Label(frame_input, text="Password", font=("Goudy old style", 20, "bold"), fg='#40e0d0', bg='white')
        label3.place(x=30, y=195)

        self.password = Entry(frame_input, font=("times new roman", 15, "bold"), bg='lightgray')
        self.password.place(x=30, y=245, width=270, height=35)

        Button1 = Button(frame_input, text="forgot password?", cursor='hand2',
                         font=('calibri', 10), bg='white', fg='black', bd=0)
        Button1.place(x=125, y=305)

        Button2 = Button(frame_input, text="Login", command=self.login, cursor="hand2",
                         font=("times new roman", 15), fg="white", bg="#40e0d0", bd=0, width=15, height=1)
        Button2.place(x=90, y=340)

        Button3 = Button(frame_input, command=self.Register, text="Not Registered?register", cursor="hand2",
                         font=("calibri", 10), bg='white', fg="black", bd=0)
        Button3.place(x=110, y=390)


    def login(self):
        if self.email_txt.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:  # SQL connection
            try:
                Connection = pymysql.connect(host='localhost', user='root', password='12345', database='CCDBMS')

                cur = Connection.cursor()
                cur.execute('select * from register where emailid=%s and password=%s',
                            (self.email_txt.get(), self.password.get()))  # Need clarity

                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Username And Password', parent=self.root)

                    self.loginclear()
                    self.email_txt.focus()

                else:
                    self.appscreen()
                    Connection.close()
            except Exception as es:
                messagebox.showerror('Error', f'Error Due to : {str(es)}', parent=self.root)

    def Register(self):  # Frame for first tym registrations .. Page design

        Frame_login1 = Frame(self.root, bg="white")  # guess its for Back ground image
        Frame_login1.place(x=0, y=0, height=700, width=1366)

        self.img = ImageTk.PhotoImage(file="Dubai Skyline.jpg") #loading img from local drive
        img = Label(Frame_login1, image=self.img)
        img.place(x=0, y=0, width=1366, height=700)


        frame_input2 = Frame(self.root,
                             bg='White')  # and this for register here, username passwqord etc etc   labels and entry boxes
        frame_input2.place(x=320, y=130, height=450, width=630)

        label1 = Label(frame_input2, text="Register Here", font=('impact', 32, 'bold'), fg="black", bg='white')
        label1.place(x=45, y=20)

        # For username... label and textbox
        label2 = Label(frame_input2, text="Username", font=("Goudy old style", 20, "bold"), fg='#40e0d0', bg='white')
        label2.place(x=30, y=95)

        self.entry1 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry1.place(x=30, y=145, width=270, height=35)

        # For Password... Label and textbox
        label3 = Label(frame_input2, text="Password", font=("Goudy old style", 20, "bold"), fg='#40e0d0', bg='white')
        label3.place(x=30, y=195)

        self.entry2 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry2.place(x=30, y=245, width=270, height=35)

        #  For Email ID ...
        label4 = Label(frame_input2, text="Email-id", font=("Goudy old style", 20, "bold"), fg='#40e0d0', bg='white')
        label4.place(x=330, y=95)

        self.entry3 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry3.place(x=330, y=145, width=270, height=35)

        # Confirm Passowrd... Label and Box
        label5 = Label(frame_input2, text="Confirm Password", font=("Goudy old style", 20, "bold"), fg='#40e0d0',
                       bg='white')
        label5.place(x=330, y=195)

        self.entry4 = Entry(frame_input2, font=("times new roman", 15, "bold"), bg='lightgray')
        self.entry4.place(x=330, y=245, width=270, height=35)

        # Register Button
        btn2 = Button(frame_input2, command=self.register, text="Register", cursor="hand2",
                      font=("times new roman", 15), fg="white", bg="#40e0d0", bd=0, width=15, height=1)

        btn2.place(x=90, y=340)

        # Already registered  button
        btn3 = Button(frame_input2, command=self.loginform, text="Already Registered?Login", cursor="hand2",
                      font=("calibri", 10), bg='white', fg="black", bd=0)
        btn3.place(x=110, y=390)

    def register(self):  # Button function
        if self.entry.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.entry2.get() != self.entry4.get():
            messagebox.showerror("Error", "Password and Confirm Password Should Be Same", parent=self.root)

        else:
            con = pymysql.connect(host="localhost", user="root", password="shivakesh2", database="pythongui")
            cur = con.cursor()

            cur.execute("select * from register where emailid=%s", self.entry3.get())
            row = cur.fetchone()
            try:
                if row != None:
                    messagebox.showerror("Error", "User already Exist,Please try with another Email", parent=self.root)

                    self.regclear()
                    self.entry.focus()

                else:
                    cur.execute("insert into register values(%s,%s,%s,%s)", (self.entry.get(), self.entry3.get(),
                                                                             self.entry2.get(), self.entry4.get()))
                    con.commit()
                    con.close()

                    messagebox.showinfo("Success", "Registration Succesful", parent=self.root)

                    self.regclear()

            except Exception as es: \
 \
                    messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    def appscreen(self):
        pass


root = Tk()
object = Login(root)

root.mainloop()

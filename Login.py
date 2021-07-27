from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector as ms


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
        frame_input.place(x=320, y=130, height=450, width=700)

        # Arranging every element onto the frame_input
        label1 = Label(frame_input, text="Login Here", font=('Bernard MT Condensed', 32, 'bold'), fg="black",
                       bg='white')
        label1.place(x=200, y=20)

        Username_label = Label(frame_input, text="Username", font=("Goudy old style", 20, "bold"), fg='#40e0d0',
                               bg='white')
        Username_label.place(x=155, y=95)

        self.Username_txt = Entry(frame_input, font=("times new roman", 12), bg='lightgray')
        self.Username_txt.place(x=155, y=145, width=270, height=35)
        self.Username_txt.insert(0, 'Enter your Username or E-mail')

        Password_label = Label(frame_input, text="Password", font=("Goudy old style", 20, "bold"), fg='#40e0d0',
                               bg='white')
        Password_label.place(x=155, y=195)

        self.Password_txt = Entry(frame_input, font=("times new roman", 12), bg='lightgray')
        self.Password_txt.place(x=155, y=245, width=270, height=35)
        self.Password_txt.insert(0, 'Enter your Password')

        Forgot_pass_btn = Button(frame_input, text="Forgot Password?", cursor='hand2', command=self.forgot_pass,
                                 font=('calibri', 10), bg='white', fg='black', bd=0)
        Forgot_pass_btn.place(x=250, y=305)

        Login_btn = Button(frame_input, text="Login", command=self.login, cursor="hand2",
                           font=("times new roman", 15), fg="white", bg="#40e0d0", bd=0, width=15, height=1)
        Login_btn.place(x=215, y=340)

        Register_btn = Button(frame_input, command=self.Register, text="Not Registered?register", cursor="hand2",
                              font=("calibri", 10), bg='white', fg="black", bd=0)
        Register_btn.place(x=235, y=390)  # Register button for those not registered

    def login(self):
        if self.Username_txt.get() == "" or self.Password_txt.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:  # SQL connection
            try:
                mydb = ms.connect(host='localhost', user='root', password='12345', database='CCDBMS')

                cur = mydb.cursor()
                cur.execute("select * from users where username='{}' and password='{}'".
                            format(self.Username_txt.get(), self.Password_txt.get()))  # Need clarity
                if not mydb.is_connected():
                    print('Connection Failed  !!')
                row1 = cur.fetchone()
                if row1 == None:
                    # messagebox.showerror('Error', 'Invalid Username And Password', parent=self.root)
                    # self.login_clear()
                    # self.Username_txt.focus_set()
                    cur.execute("select * from users where email='{}' and password='{}'".
                                format(self.Username_txt.get(), self.Password_txt.get()))
                    row2 = cur.fetchone()

                    if row2 == None:
                        messagebox.showerror('Error', 'Invalid Username And Password', parent=self.root)

                        self.login_clear()
                        self.Username_txt.focus_set()
                    else:
                        messagebox.showinfo('Login Status', 'You Have Successfully Logged in', parent=self.root)
                else:
                    messagebox.showinfo('Login Status', 'You Have Successfully Logged in', parent=self.root)


            except:
                messagebox.showinfo('ERROR !!', 'An Unexpected Error has occurred', parent=self.root)

    def Register(
            self):  # Frame for first tym registrations .. Page design.. Comes here after clicking 'not registered' 'button

        Frame_login1 = Frame(self.root, bg="white")  # Frame for Back ground image
        Frame_login1.place(x=0, y=0, height=700, width=1366)

        self.img = ImageTk.PhotoImage(file="Dubai Skyline.jpg")  # loading img from local drive
        img = Label(Frame_login1, image=self.img)
        img.place(x=0, y=0, width=1366, height=700)

        frame_input = Frame(self.root,
                            bg='White')  # and this Frame for register here, username password etc etc   labels and entry boxes
        frame_input.place(x=320, y=130, height=450, width=630)

        label1 = Label(frame_input, text="Register Here", font=('Bernard MT Condensed', 32, 'bold'), fg="black",
                       bg='white')
        label1.place(x=45, y=20)

        # For username... label and textbox
        Username_label = Label(frame_input, text="Username", font=("Goudy old style", 20, "bold"), fg='#40e0d0',
                               bg='white')
        Username_label.place(x=30, y=95)

        self.Username_Entry = Entry(frame_input, font=("times new roman", 15), bg='lightgray')
        self.Username_Entry.place(x=30, y=145, width=270, height=35)
        self.Username_Entry.insert(0, 'Enter your Username')

        # For Password... Label and textbox
        Password_label = Label(frame_input, text="Password", font=("Goudy old style", 20, "bold"), fg='#40e0d0',
                               bg='white')
        Password_label.place(x=30, y=195)

        self.Password_Entry = Entry(frame_input, font=("times new roman", 15), bg='lightgray')
        self.Password_Entry.place(x=30, y=245, width=270, height=35)
        self.Password_Entry.insert(0, 'Enter your Password')

        #  For Email ID ...
        Email_label = Label(frame_input, text="Email-id", font=("Goudy old style", 20, "bold"), fg='#40e0d0',
                            bg='white')
        Email_label.place(x=330, y=95)

        self.Email_Entry = Entry(frame_input, font=("times new roman", 15), bg='lightgray')
        self.Email_Entry.place(x=330, y=145, width=270, height=35)
        self.Email_Entry.insert(0, 'Enter your E-mail ID')

        # Confirm Password... Label and Box
        Confirm_pass = Label(frame_input, text="Confirm Password", font=("Goudy old style", 20, "bold"), fg='#40e0d0',
                             bg='white')
        Confirm_pass.place(x=330, y=195)

        self.Confirm_pass = Entry(frame_input, font=("times new roman", 15), bg='lightgray')
        self.Confirm_pass.place(x=330, y=245, width=270, height=35)
        self.Confirm_pass.insert(0, 'Re-enter your Password')

        # Register Button
        Register_btn = Button(frame_input, command=self.register, text="Register", cursor="hand2",
                              font=("times new roman", 15), fg="white", bg="#40e0d0", bd=0, width=15, height=1)

        Register_btn.place(x=240, y=340)

        # Already registered  button
        btn3 = Button(frame_input, command=self.loginform, text="Already Registered?Login", cursor="hand2",
                      font=("calibri", 10), bg='white', fg="black", bd=0)
        btn3.place(x=248, y=390)

    def register(self):  # Register Button function
        if self.Username_Entry.get() == "" or self.Password_Entry.get() == "" or self.Email_Entry.get() == "" or self.Confirm_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.Password_Entry.get() != self.Confirm_pass.get():
            messagebox.showerror("Error", "Password and Confirm Password Should Be Same", parent=self.root)

        else:
            mydb = ms.connect(host="localhost", user="root", password="12345", database="CCDBMS")
            cursor = mydb.cursor()

            cursor.execute("select * from users where email='{}'".format(self.Email_Entry.get()))
            row = cursor.fetchone()
            try:
                if row != None:
                    messagebox.showerror("Error", "User already Exist,Please try with another Email", parent=self.root)

                    self.reg_clear()
                    self.Username_Entry.focus()

                else:
                    cursor.execute("insert into users values('{}','{}','{}')".format(self.Email_Entry.get(),
                                                                                     self.Username_Entry.get(),
                                                                                     self.Password_Entry.get()))
                    mydb.commit()
                    mydb.close()

                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)

                    self.reg_clear()

            except Exception as es: \
 \
                    messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    def login_clear(self):
        self.Username_txt.delete(0, END)
        self.Password_txt.delete(0, END)

    def reg_clear(self):
        self.Username_Entry.delete(0, END)
        self.Password_Entry.delete(0, END)
        self.Confirm_pass.delete(0, END)
        self.Email_Entry.delete(0, END)

    def forgot_pass(self):
        Frame_bg = Frame(self.root, bg="white")  # guess its for Back ground image
        Frame_bg.place(x=0, y=0, height=700, width=1366)

        self.img = ImageTk.PhotoImage(file="Dubai Skyline.jpg")  # loading img from local drive
        img = Label(Frame_bg, image=self.img)
        img.place(x=0, y=0, width=1366, height=700)

        # Frame for arranging widgets like Labels, textboxes
        frame_input = Frame(self.root, bg='white')
        frame_input.place(x=320, y=130, height=450, width=700)

        # Arranging every element onto the frame

        label1 = Label(frame_input, text="Trouble Login in?", font=('Bernard MT Condensed', 28, 'bold'), fg="black",
                       bg='white')
        label1.place(x=330, y=45, anchor='center')  # trouble login label

        Username_label = Label(frame_input, text="Username", font=("Goudy old style", 20, "bold"), fg='#40e0d0',
                               bg='white')
        Username_label.place(x=50, y=110)

        self.Username_Entry = Entry(frame_input, font=("times new roman", 12), bg='lightgray')
        self.Username_Entry.place(x=260, y=110, width=270, height=35)
        self.Username_Entry.insert(0, "Enter your Username")

        Reg_email_label = Label(frame_input, text="Registered Mail", font=("Goudy old style", 20, "bold"), fg='#40e0d0',
                                bg='white')
        Reg_email_label.place(x=50, y=170)

        self.Reg_email_entry = Entry(frame_input, font=("times new roman", 12), bg='lightgray')
        self.Reg_email_entry.place(x=260, y=170, width=270, height=35)
        self.Reg_email_entry.insert(0, "Enter your Registered Email Address")

        send_mail_btn = Button(frame_input, text="Send Mail", command=self.send_mail, cursor="hand2",
                               font=("times new roman", 15), fg="white", bg="#40e0d0", bd=0, width=15, height=1)
        send_mail_btn.place(x=80, y=270)
        # Back to Login form
        Back_btn = Button(frame_input, text="Back", command=self.loginform, cursor="hand2",
                          font=("times new roman", 15), fg="white", bg="#40e0d0", bd=0, width=15, height=1)
        Back_btn.place(x=350, y=270)

        Label_note = Label(frame_input,
                           text='An E-mail with the Login Credentials will be sent to the Registered Email, after verification',
                           font=('Kozuka Gothic Pr6N M', 12, 'bold'), bg='white', fg='Grey')
        Label_note.place(x=10, y=320)

    def send_mail(self):
        pass

    def appscreen(self):  # after login
        pass


root = Tk()
object = Login(root)

root.mainloop()

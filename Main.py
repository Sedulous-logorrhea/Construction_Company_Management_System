class Quotation:

    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1000, name='', address='', cindate='', coutdate='', rno=1):

        print("\n\n*****WELCOME TO Construction management System*****\n")

        self.rt = rt

        self.r = r

        self.t = t

        self.p = p

        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nEnter your Fullname:")
        self.address = input("\nEnter your address:")
        self.cindate = input("\nPropsoed Enquiry Start Date:")
        self.coutdate = input("\nProposoed Enquiry Deadline :")
        print("Your Enquiry no.:", self.rno, "\n")

    def Quotation_Value(self):  # sel1353

        print('''We offer complete solution to all your Structual
        Steel related construction works.''')

        print("1.  WARE-HOUSE CONSTRUCTION -&gt;")
        print("2.  STRUCTURAL STEEL FABRICATION AND ERECTION -&gt;")
        print("3.  OIL STORAGE TANK FARM CONSTRUCTION -&gt;")
        print("4.  LUBRICANT MANUFACTURING PLANT -&gt;")
        print("5.  OIL REFINING FACTORY -&gt;")
        print("6.  LUBRICANT MANUFACTURING PLANT -&gt;")

        x = int(input("Enter the number of your choice Please-&gt;"))

        n = input("Do you have a sub-contractor?:")

        if (x == 1):

            print("you have choose room Class A")

            self.s = 4000 * n

        elif (x == 2):

            print("you have choose room Class B")

            self.s = 3000 * n

        elif (x == 3):

            print("you have choose room Class C")

            self.s = 2000 * n

        elif (x == 4):
            print("you have choose room Class D")

            self.s = 1000 * n

        else:

            print("please choose a work")

        print("Your Estimated cost of work =", self.s, "\n")

    def foodpurchased(self):

        print("*****RESTAURANT MENU*****")

        print("1.Dessert-----&gt;100", "2.Drinks-----&gt;50", "3.Breakfast---&gt;90", "4.Lunch----&gt;110",
              "5.Dinner---&gt;150", "6.Exit")

        while (1):

            c = int(input("Enter the number of your choice:"))

            if (c == 1):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 100 * d

            elif (c == 2):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 50 * d

            elif (c == 3):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 90 * d

            elif (c == 4):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 110 * d

            elif (c == 5):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 150 * d

            elif (c == 6):
                break
            else:
                print("You've Enter an Invalid Key")

        print("Total food Cost=Rs", self.r, "\n")

    def display(self):
        print("******HOTEL BILL******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check in date:", self.cindate)
        print("Check out date", self.coutdate)
        print("Room no.", self.rno)
        print("Your Room rent is:", self.s)
        print("Your Food bill is:", self.r)

        self.rt = self.s + self.t + self.p + self.r

        print("Your sub total Purchased is:", self.rt)
        print("Additional Service Charges is", self.a)
        print("Your grandtotal Purchased is:", self.rt + self.a, "\n")
        self.rno += 1


def main():
    a = Quotation()

    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate Room Rent")

        print("3.Calculate Food Purchased")

        print("4.Show total cost")

        print("5.EXIT")

        b = int(input("\nEnter the number of your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):
            a.Quotation_Value()

        if (b == 3):
            a.foodpurchased()

        if (b == 4):
            a.display()

        if (b == 5):
            quit()
main()
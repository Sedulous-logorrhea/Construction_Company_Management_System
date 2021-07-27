class Quotation:
    def __init__(self, rt='', s=0, p=0, r=0, a=1000, name='', address='', cindate='', coutdate='', rno=1001):
        print("\n\n*****WELCOME TO Construction Management System*****\n")
        self.rt = rt
        self.r = r
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
        self.cindate = input("\nProposed Enquiry Start Date:")
        self.coutdate = input("\nProposed Enquiry Deadline :")
        print("Your Enquiry no.:", self.rno, "\n")

    def Quotation_Value(self):
        print('''We offer complete solution to all your Structural
        Steel related construction works.''')

        print("1.  WARE-HOUSE CONSTRUCTION -&gt;")
        print("2.  OIL STORAGE TANK FARM CONSTRUCTION-&gt;")
        print("3.  LUBRICANT MANUFACTURING PLANT -&gt;")
        print("4.  OIL REFINING FACTORY-&gt;")
        print("5.  OIL AND GAS PIPELINES -&gt;")

        x = int(input("Enter the number of your choice Please-&gt;"))

        if x in (1,2,3,4,5):
            n = input("Do you have a sub-contractor?:")
            mes=input("Do you want to proceed with m or feet :")
            area=int(input("Enter the area of constructables:"))        # Single . mezzanine(70%)
            excavation=int(input("Enter the Excavation volume:"))
            Back_filing=int(input("Enter the Back-filing volume:"))
            R_base_f=int(input("Enter the Road base for foundation volume per ton:"))
            Anti_termite=int(input("Enter the Anti-Termite volume:"))
            PCC=int(input("Enter the PCC volume:"))
            RCC_f=int(input("Enter the RCC for footing volume:"))
            RCC_p = int(input("Enter the RCC for pedestal volume:"))
            RCC_tb = int(input("Enter the RCC for tie beam volume:"))
            SBW=int(input("Enter the Solid Block work volume:"))
            BRC_mesh=int(input("Enter the Floor concrete with BRC mesh volume:"))
            P_s=













        else:
            print("please choose a work")

        print("Your Estimated cost of work =", self.s, "\n")

    def display(self):
        print("******The Quotation Summary******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Proposed contract start date:", self.cindate)
        print("Proposed contract End date:", self.coutdate)
        print("Enquiry no.", self.rno)
        print("Estimated Construction value:", self.s)

        print("Your Grand total Purchased is:", self.rt , "\n")
        self.rno += 1


def main():
    a = Quotation()

    while (1):
        print("1.Enter Customer Data")

        print("2.Central Job")

        print("3.Estimated total cost")

        print("4.EXIT")

        b = int(input("\nEnter the number of your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):
            a.Quotation_Value()

        if (b == 3):
            a.display()

        if (b == 4):
            quit()
main()

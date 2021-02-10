class Bank:
    def withdraw(self):
        print("Inside withdraw")

    def enquiry(self):
        print("INside enquiry")

    def __deposit(self):
        print("Inside deposit")

b=Bank()
b.withdraw()
b.enquiry()
b._Bank__deposit()
from datetime import datetime

class Bank:
    Bank_name="SBI"
    #def create_acc(self,acc_no,name,balance):
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.bal=balance
        #self.bank_name=bank_name

    def deposit(self,amount):
        self.bal+=amount
        print("Your",Bank.Bank_name,"account",self.acc_no,"is credited with",amount,"on",datetime.today(),"available balance",self.bal)

    def withdrawal(self,amount):
        if self.bal>amount:
            self.bal-=amount
            print("Your account", self.acc_no, "is debited with", amount, "on", datetime.today(), "available balance",self.bal)

        else:
            print("Transaction cancelled with error code")

    def enquiry(self):
        print("Available Balance is",self.bal)

#obj=Bank()
#obj.create_acc("10000235xxxxx","Hanna",15000)

obj=Bank("10000235xxxxx","Hanna",15000)
obj.enquiry()
obj.withdrawal(10000)
obj.enquiry()
obj.deposit(20000)
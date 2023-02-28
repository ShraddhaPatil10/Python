class Bank_Account:
    Bank_Name="HDFC Bank PVT LTD"
    ROI_ON_FD=6.7

    def __init__(self):
        self.Name=""
        self.Amount=0
        self.Address=""
        self.AccountNo=0

    def CreateAccount(self):
        print("Enter your name:")
        self.Name=input()

        print("Enter initial amount:")
        self.Amount=int(input())

        print("Enter your address:")
        self.Address=input()

        print("Enter your account number:")
        self.AccountNo=int(input())

    def DisplayAccountInfo(self):
        print("Name of account holder:",self.Name)
        print("Current amount in account:",self.Amount)
        print("Address of account holder:",self.Address)
        print("Account Number:",self.AccountNo)

    @classmethod
    def DisplayBankInfo(cls):
        print("Welcome to banking console")
        print("Name of our bank is:",cls.Bank_Name)
        print("Rate of Intrest we offer on fixed deposit is:",cls.ROI_ON_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC Information")
        print("Accordinhg to rules of Government of India you have to submit below documents")
        print("1.Clear & Recent passport size photo")
        print("2.Photo of Adhar Card")
        print("3.Photo of PAN Card")

    def Deposit(self,value):
        self.Amount=self.Amount+value

    def Withdraw(self,value):
        self.Amount=self.Amount-value

def main():
    print("**********Banking Application**********")

    print("\n****************************************************")
    print("Calling static method to display KYC Info")
    Bank_Account.DisplayKYCInfo()

    print("\n****************************************************")
    print("Access the class variables from main")
    print("Name of bank :",Bank_Account.Bank_Name)
    print("Rate of Interest on fixed deposite:",Bank_Account.ROI_ON_FD)

    print("\n****************************************************")
    print("Calling the class method to display Bank Information")
    Bank_Account.DisplayBankInfo()

    print("\n****************************************************")
    print("Creating the objects of class")
    User1=Bank_Account()
    User2=Bank_Account()

    print("\n****************************************************")
    print("Creating 1st account")
    print("Enter details for 1st account holder:")
    User1.CreateAccount()

    print("\n****************************************************")
    print("Creating 2nd account")
    print("Enter details for 2nd account holder:")
    User2.CreateAccount()

    print("\n****************************************************")
    print("Calling instance method to display information of first account")
    User1.DisplayAccountInfo()

    print("\n****************************************************")
    print("Calling instance method to display information of second account")
    User2.DisplayAccountInfo()

    print("\n****************************************************")
    print("Depositing 500 in User1")
    User1.Deposit(500)

    print("Depositing 1200 in User2")
    User2.Deposit(1200)

    print("Amount of {} after deposit is {}".format(User1.Name,User1.Amount))
    print("Amount of {} after deposit is {}".format(User2.Name,User2.Amount))

    print("\n****************************************************")
    print("Withdraw 200 in User1")
    User1.Withdraw(200)

    print("Withdraw 3000 in User2")
    User2.Withdraw(3000)
    
    print("Amount of {} after withdraw is {}".format(User1.Name,User1.Amount))
    print("Amount of {} after withdraw is {}".format(User2.Name,User2.Amount))

    print("\n*******************************************************")
    print("End of Banking Application")
    print("\n*******************************************************")
    
if __name__=="__main__":
    main()
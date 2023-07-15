from newacc import NewAccount
from deposit import Deposit
from withdraw import Withdraw
from balanceenquiry import BalanceEnquiry
from closeaccount import Closeaccount
class Bank:
    def __init__(self):
        self.new = NewAccount()
        self.new2= Deposit()
        self.new3 = Withdraw()
        self.new4 = BalanceEnquiry()
        self.new5 = Closeaccount()
    
    def start(self): 
        while True:
            print("Welcome to Payments Bank")
            print("1. Open a New Account")
            print("2. Deposit Amount")
            print("3. Withdraw Amount")
            print("4. Balance Check")
            print("5. Close Bank Account")
            choice = int(input("Input your choice: "))

            if choice==1:     
                name, contact, dob, addr, email = self.new.new_user_details()
                accnumber = self.new.new_account_no()
                self.new.save_user_details(accnumber,name,contact,dob,addr,email,balance=0)

            elif choice==2:
                accnumber = int(input("Enter your Acc Number : "))
                balance = self.new2.deposit_cash(accnumber)
                self.new.update_details(accnumber,balance)
                
            elif choice==3:
                accnumber = int(input("Enter your Acc Number : "))
                balance = self.new3.withdraw_cash(accnumber)
                self.new.update_details(accnumber,balance)

            elif choice==4:
                accnumber = int(input("Enter your Acc Number : "))
                self.new4.balance_enquire(accnumber)
            
            elif choice==5:
                accnumber = int(input("Enter your Acc Number : "))
                self.new5.close_acc(accnumber)

            else:
                print("Invalid Entry.\nThank You for using our portal")
            
            
acc=Bank()
acc.start()
        


    
    




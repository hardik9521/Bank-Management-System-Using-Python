from image import Image
import random
class NewAccount:

    def __init__(self):
        self.new = Image()

    def new_user_details(self):
        name = input("Enter your Full Name : ")
        contact = input("Enter your contact details : ")
        dob = input("Enter your date of birth in DD/MM/YY format : ")
        addr = input("Enter your address : ")
        email = input("Enter your email address : ")
        return name,contact,dob,addr,email
    
    

    def new_account_no(self):
        accountno = random.randint(10000000000,99999999999)
        print("Your Account Number ",accountno)
        password = input("Enter a strong password")
        with open("admin.txt","a") as file:
            file.write(str(accountno) + " : "+ password + "\n")
        self.new.capture_image(accountno)
        return accountno
    
    def save_user_details(self,accountno,name,contact,dob,addr,email,balance):
        file = f"{accountno}.txt"
        with open(file,"w") as f:
            f.write(f"Account Number : {accountno}\n")
            f.write(f"Customer Name : {name}\n")
            f.write(f"Contact : {contact}\n")
            f.write(f"DateOfBirth : {dob}\n")
            f.write(f"Address : {addr}\n")
            f.write(f"Email Address : {email}\n")
            f.write(f"Balance : {balance}\n")

    def update_details(self,accountno,balance):
        file_path = f"{accountno}.txt"
        try:
            with open(file_path,"r") as file:
                text = file.readlines()
            
            with open(file_path,"w") as file:
                for txt in text:
                    if txt.startswith("Balance"):
                        txt = f"Balance: {balance}\n"
                    file.write(txt)
        
        except FileNotFoundError:
            return None


            







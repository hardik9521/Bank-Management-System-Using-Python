class BalanceEnquiry:
    def balance_enquire(self,accnumber):
        file_path = f"{accnumber}.txt"
        try:
            with open(file_path,"r") as file:
                passw = input("Enter your password")
                with open("admin.txt","r") as admin:
                    admintxt = admin.readlines()
                    for line in admintxt:
                        if line.split(":")[0].strip()==str(accnumber):
                            if line.split(":")[1].strip()==passw:
                                text = file.readlines()
                                for txt in text:
                                    if txt.startswith("Balance"):
                                        balance = float(txt.split(":")[1].strip())
                                        print("your bank balance is Rs.",balance," only.")
                                        return balance
                            else:
                                print("Wrong Password")
                    
        except FileNotFoundError:
            print("Account Doesn't Exist")


        
class Withdraw:

    def withdraw_cash(self,accnumber):
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
                                        cash = int(input("How much do you want to withdraw? "))
                                        if cash<=balance:
                                            print("Here's your Rs.",cash," cash")
                                            balance-=cash
                                        else:
                                            print("You dont have enough balance to withdraw")
                                            print("Your balance is Rs.",balance," only")

                                        return balance
                            else:
                                print("Wrong Password")
                                
        except FileNotFoundError:
            print("Account Doesn't Exist")
            return None
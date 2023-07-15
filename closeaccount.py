import os
class Closeaccount:
    def close_acc(self,accnumber):
        file_path = f"{accnumber}.txt"
        passw = input("Enter your password")
        with open("admin.txt","r") as admin:
            admintxt = admin.readlines()
            for line in admintxt:
                if line.split(":")[0].strip()==str(accnumber):
                    if line.split(":")[1].strip()==passw:
                        if os.path.exists(file_path):
                            os.remove(file_path)
                            print("Account deleted successfully")
                        else:
                            print("Account Doesn't exist")
                    else:
                        print("Wrong Password")
                        return

                        file_path2 = f"{accnumber}.jpg"
                        if os.path.exists(file_path2):
                            os.remove(file_path2)
            
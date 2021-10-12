print("\n####################################         Case-Studies/ Projects         ############################################")




print("Project 01:")

class Bank_Account:
    def __init__(self,accno,name,balance):
        self.accno = accno
        self.name = name
        self.balance = balance


    def Withdrawal(self):
        withdrawal = int(input("Enter Withdrawal Amount:"))
        if withdrawal % 100 == 0:
            T_balance = self.balance - withdrawal
            if T_balance >= 1000:
                # Tax = 5 / 100 * self.balance
                print('Please wait while your treansaction being processing...')
                print("Please Collect your amount:", withdrawal)
                # print("Tax for maintaning balance is:",Tax)
                # print("Your Updated Balance is:", T_balance-Tax)
                print("Your Total balance is:", T_balance)

            else:
                print("Insufficient balance. Enter Less Amount !!!")
        else:
            print("Enter Amount like: 100,200,500,1000,2000")
            print("Please Try again")
    def Deposite(self):
        Deposit = int(input("Enter Deposit amount:"))
        if Deposit % 100 == 0:
            T_balance = Deposit + self.balance
            print("Your Updated Balance is:", T_balance)
            Tax = 5 / 100 * Deposit
            print("Tax for maintaning balance is:", Tax)
            print("Your Updated Balance is:", T_balance - Tax)
        else:
            print("Enter Amount like: 100,200,500,1000,2000")
            print("Please Try again")
    def display(self):
        print("☺☺☺☺☺☺☺☺ Welcome",self.name,"☺☺☺☺☺☺☺☺")
        print("acc.no:",self.accno,",name:",self.name,",balance:",self.balance,sep=" ")



obj1 = Bank_Account(1234,"Anil",10000)
obj1.display()
obj1.Withdrawal()
obj1.display()
obj1.Deposite()

obj2 = Bank_Account(1566,"Rockey",87000)
obj2.display()
obj2.Withdrawal()
obj2.display
obj2.Deposite()

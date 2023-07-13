# create a bank with python language 

# define a custim exception 
class AbortTransaction(Exception):
    pass

# create an account class to manage what you can do with an account class 
# 1. check password 
# 2. get balance 
# 3. withdraw
# 4. deposit 
# 5. check amount (positive), check amount entered is also in money form, as in floats(cant use int, what about cents?)
# 6. show info 

# can only put opening and closing of account in bank class because of the manipulation of bank dict 
# when trying to increase or decrease the number of accounts in the bank dict 

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.checkAmount(balance)
        self.password = password

    def checkAmount(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise AbortTransaction("Invalid form of money")
        if amount<=0:
            raise AbortTransaction("Amount must be positive")
        return amount
    
    def checkPassword(self):
        password = input("Please enter your password: ")
        if password != self.password:
            raise AbortTransaction("Incorrect user password")
        
    def getBalance(self):
        return self.balance
    
    def deposit(self):
        amountToDeposit = input("Enter amount to deposit: ")
        amountToDeposit = self.checkAmount(amountToDeposit)
        self.balance += amountToDeposit
        print("You deposited:", amountToDeposit)
        return self.balance

    def withdraw(self):
        amountToWithdraw = input("Enter amount to wtihdraw: ")
        amountToWithdraw = self.checkAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction("You cannot withdraw a larger sum than your balance")
        self.balance -= amountToWithdraw
        print("You withdrew:", amountToWithdraw)
        return self.balance

# bank that manages a dictionary of Account objects
# what can a bank do?
# create account 
# close account, rmb to check for user pw before closing
# get user account number to direct to the account + check valid acc no

# need to encompass all the functions an account can do 

# admin can see all bank acc 
# but require admin password

class Bank():
    def __init__(self):
        self.accountsDict = {}
        self.currentAccNo = 0
        self.adminPassword = "123"

    def checkAccNo(self):
        accNo = input("What is your account number: ")
        try:
            accNo = int(accNo)
        except ValueError:
            raise AbortTransaction("Invalid account number")
        if accNo not in self.accountsDict:
            raise AbortTransaction("No such account found in bank")
        return accNo

    def getAcc(self):
        accNo = self.checkAccNo()
        oAccount = self.accountsDict[accNo]
        oAccount.checkPassword()
        return oAccount
        
    def createAccount(self):
        print("-------Open account------")
        theName = input("What is the name of the account user: ")
        theStartBalance = input("What is the starting balance: ")
        thePassword = input("Set a pin for your account: ")
        oAccount = Account(theName, theStartBalance, thePassword)
        newAccountNo = self.currentAccNo
        self.accountsDict[newAccountNo] = oAccount
        self.currentAccNo += 1
        print("Your new account number is:", newAccountNo)

    
    def closeAccount(self):
        print("-------Close Account------")
        userAccNo = self.checkAccNo()
        oAccount = self.accountsDict[userAccNo]
        oAccount.checkPassword()
        userBalance = oAccount.getBalance()
        print("Your account is now closed with " + str(userBalance) + " returned to you")
        del self.accountsDict[userAccNo]

    def balance(self):
        print("-----Get balance-----")
        oAccount = self.getAcc()
        theBalance = oAccount.getBalance()
        print("Your balance is:", theBalance)

    def deposit(self):
        print("------Deposit------")
        oAccount = self.getAcc()
        theBalance = oAccount.deposit()
        print("Your new balance is:", theBalance)

    def withdraw(self):
        print("-----Withdraw------")
        oAccount = self.getAcc()
        theBalance = oAccount.withdraw()
        print("Your new balance is:", theBalance)


    # for admin
    def checkAdminPassword(self):
        aP = input("Are you an admin? Enter admin password: ")
        if aP != self.adminPassword:
            raise AbortTransaction("Incorrect admin password")


    def show(self):
        self.checkAdminPassword()
        print("Admin looking through bank accounts.....")
        for userAccNo in self.accountsDict:
            oAccount = self.accountsDict[userAccNo]
            print("Account:", userAccNo)
            oAccount.show()
            print("")

 
oBank = Bank()

while True:
    print("")
    print("A) Create an account")
    print("B) Get account balance")
    print("C) Close an account")
    print("D) Make a deposit")
    print("E) Make a withdrawal")
    print("Q) Quit")
    print("Z) Admin show accounts")

    action = input("What do you want to do?")
    action = action.lower()
    try:
        if action == 'a':
            oBank.createAccount()
        elif action == 'b':
            oBank.balance()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'd':
            oBank.deposit()
        elif action == 'e':
            oBank.withdraw()
        elif action == 'q':
            break
        elif action == 'z':
            oBank.show()

    except AbortTransaction as error:
        print(error)


print("Done, thank you")
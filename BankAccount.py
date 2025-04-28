# Dom Stencel
# CSC 330 100
# Session 7
# Final Project - BankAccount Class
# 4/27/25

############################################
#####           BANKACCOUNT         ########
############################################
class BankAccount():
    allAccounts = [] # list of all BankAccount objects
    accountNums = [] # list of all account numbers
    currNum = 100000 # first number used for account

#############################################
#########   Bank account constructor ########
#############################################
    def __init__(self, firstName, lastName) : # Removed account num and balance parameters - LH

        self.__firstName = firstName
        self.__lastName = lastName
        self.__accountNum = self.generateAccount()
        self.__balance = 0.0

    def __str__ (self): # removed parameters
        return f'{self.__firstName} {self.__lastName} account: #{self.__accountNum} \nBalance: {self.__balance}'

###############################################################
#####   generateAccount() - creates new account number ########
###############################################################
    def generateAccount(self):

        first = self.__firstName[0].upper() # first letter of first name
        last = self.__lastName[0].upper() # first letter of last name
        num_part = f'{BankAccount.currNum}' # uses number for number part of account number
        #randomNums = ''.join(str(random.randint(0, 9)) for _ in range(6))
        account_num = first + last + num_part

        if account_num in BankAccount.accountNums:
            account_num = self.generateAccount()
        else:
            BankAccount.accountNums.append(account_num)
            BankAccount.currNum += 1
            return account_num

#########################################
#######         GETTERS         #########
#########################################
    def get_firstName(self):
        return self.__firstName # get first name

    def get_lastName(self):
        return self.__lastName # get last name

    def get_accountNumber(self):
        return self.__accountNum # get account Number

    def get_balance(self):
        return self.__balance # get balance
########################################
######           SETTERS        ########
########################################
    def set_firstName(self, first_name):
        self.__firstName = first_name # set first name

    def set_lastName(self, last_name):
        self.__lastName = last_name # set last name

    def set_balance(self, amount):
        if amount >= 0: # set positive balance
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative.")

    ###############################################################
    ######     deposit() - deposit money to an account     ########
    ###############################################################
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount # add money to account if amount is positive
            return self.__balance
        else:
            raise ValueError("Deposit must be positive.")

    ###############################################################
    ######      withdraw() - withdraw from an account      ########
    ###############################################################
    def withdraw(self, amount):
        if 0 < amount <= self.__balance: # withdraws amount, so long as amount is positive and less than balance
            self.__balance -= amount
            return self.__balance
        else:
            raise ValueError("Invalid withdrawal amount.")
    


   

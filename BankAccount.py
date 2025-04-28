import random


class BankAccount(): # removed parameters - LH
    allAccounts = []
    accountNums = []
    currNum = 100000

    def __init__(self, firstName, lastName) : # Removed account num and balance parameters - LH
        self.__firstName = firstName
        self.__lastName = lastName
        self.__accountNum = self.generateAccount() # removed parameters - LH
        self.__balance = 0.0

    def __str__ (self): # removed parameters
        return f'{self.__firstName} {self.__lastName} account: #{self.__accountNum} \nBalance: {self.__balance}'

    # -------- Generate Account --------
    def generateAccount(self):

        first = self.__firstName[0].upper()
        last = self.__lastName[0].upper()
        num_part = f'{BankAccount.currNum}'
        #randomNums = ''.join(str(random.randint(0, 9)) for _ in range(6))
        account_num = first + last + num_part

        if account_num in BankAccount.accountNums:
            account_num = self.generateAccount()
        else:
            BankAccount.accountNums.append(account_num)
            BankAccount.currNum += 1
            return account_num


    # -------- Getters --------
    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_accountNumber(self):
        return self.__accountNum

    def get_balance(self):
        return self.__balance


    # -------- Setters --------
    def set_firstName(self, first_name):
        self.__firstName = first_name

    def set_lastName(self, last_name):
        self.__lastName = last_name

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative.")

    # -------- Deposit & Withdraw --------
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            raise ValueError("Deposit must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            raise ValueError("Invalid withdrawal amount.")
    


   

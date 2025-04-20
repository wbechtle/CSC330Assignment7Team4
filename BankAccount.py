import random

# Dictionary to keep track of current accounts
currAccounts = {}

class BankAccount(self, firstName, lastName, accountNum, balance):
    
    def __init__(self, firstName, lastName, accountNum, balance ):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__accountNum = generateAccount(firstName, lastName)
        self.__balance = 0.0

    def __str__ (self, firstName, lastName, accountNum, balance):
        return f'{self.firstName} + ' ' + {self.lastName} + 'account: ' + {self.accountNum} +
        \n'Balance: ' + {self.balance}'

    # -------- Generate Account --------
    def generateAccount(self):
        ''' Generate account with first two letters are the first intial of the first name
        and first initial of the last name. Then followed by six random numbers. '''
        prefix = self.__firstName[0].upper() + self.__lastName[0].upper()
        
        # Source: https://www.geeksforgeeks.org/python-generate-random-string-of-given-length/
        randomNums = ''.join(str(random.randint(0, 9)) for _ in range(6))
        
        accountNum = prefix + randomNums

        # Check and see if account num already exists
        for acc in currAccounts:
            if acc['Account'] == accountNum:
               return generateAccount(self)

        ''' If it passes through the for loop then it is unique and can be appended
        to the currAccounts dictionary. '''
        currAccounts.append({
            'name': f"{self.__firstName} {self.__lastName}",
            'account': self.__accountNum
        })
        
    # -------- Getters --------
    def get_firstName(self):
        return self.__first_name

    def get_lastName(self):
        return self.__last_name

    def get_accountNumber(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    # -------- Setters --------
    def set_firstName(self, first_name):
        self.__first_name = first_name

    def set_lastName(self, last_name):
        self.__last_name = last_name

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
    


   

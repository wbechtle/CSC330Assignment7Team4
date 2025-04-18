import random

class BankAccount(self, firstName, lastName, accountNum, balance):
    # Dictionary to keep track of current accounts
    currAccounts = {}
    
    def __init__(self, firstName, lastName, accountNum, balance ):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__accountNum = generateAccount(firstName, lastName)
        self.__balance = 0.0

    def __repr__ (self, firstName, lastName, accountNum, balance):
        return f'{self.firstName} + ' ' + {self.lastName} + 'account: ' + {self.accountNum} +
        \n'Balance: ' + {self.balance}'
        
    def generateAccount(firstName, lastName):
        ''' Generate account with first two letters are the first intial of the first name
        and first initial of the last name. Then followed by six random numbers. '''
        prefix = firstName[0].upper() + lastName[0].upper()
        # Source: https://www.geeksforgeeks.org/python-generate-random-string-of-given-length/
        randomNums = ''.join(str(random.randint(0, 9)) for _ in range(6))
        accountNum = prefix + randomNums

        # Check and see if account num already exists
        for acc in currAccounts:
            if acc['Account'] == accountNum:
               return generateAccount(firstName, lastName)

        ''' If it passes through the for loop then it is unique and can be appended
        to the currAccounts dictionary. '''
        currAccounts.append({
            'name': f"{firstName} {lastName}",
            'account': accountNum
        })
        

    

    


    def
   

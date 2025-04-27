# Layla Heath
# CSC 330 100
# Session 7
# Final Project - Interpreter Class
# 4/27/2025

from Parser import Deposit, Withdraw, Balance, CreateNew
from BankAccount import BankAccount

####################################################
######               Interpreter              ######
####################################################
class Interpreter:
    def __init__(self, program):
        self.accounts = [] # list of bank account objects
        self.program = program # program to be interpreted

    def interpret(self):
        # goes through the AST to evaluate each node
        for node in self.program.actions:
            # executes function based on node type/class
            if isinstance(node, Deposit): # Deposit node
                self.deposit(node)
            elif isinstance(node, Withdraw): # Withdraw node
                self.withdraw(node)
            elif isinstance(node, Balance): # Balance node
                self.balance(node)
            elif isinstance(node, CreateNew): # Create node
                self.create_new(node)
            else:
                raise Exception(f"INVALID NODE TYPE") # Default print statement

###################################################################
#####      create_new(node) - Creates a new account        ########
###################################################################
    def create_new(self, node):
        account = BankAccount(node.first, node.last) # create new Bank Account object
        BankAccount.allAccounts.append(account) # add new account to the running list
        print(f"NEW MEMBER {account.get_firstName()} {account.get_lastName()} "
              f"\nACCOUNT #{account.get_accountNumber()}"
              f"\nBALANCE ${account.get_balance()}\n")

###################################################################
#####         deposit(node) - Deposits money to account      ######
###################################################################
    def deposit(self, node):
        account = self.find_acct(node.account) # check if there is record of the account
        if account is None:
            print(f"ACCOUNT #{node.account} NOT FOUND.") # does not attempt to deposit if account is not found
        else:
            account.deposit(node.amount) # deposits money to the current account and tells user new balance
            print(f"ACCOUNT {account.get_accountNumber()} ({account.get_firstName()} {account.get_lastName()}) "
                  f"NEW BALANCE: ${account.get_balance()}")

###################################################################
#####       withdraw(node) - Withdraws mone from account     ######
###################################################################
    def withdraw(self, node):
        account = self.find_acct(node.account) # check if the account number is valid
        if account is None:
            print(f"ACCOUNT #{node.account} NOT FOUND.")

        elif node.amount > account.getBalance() : # check if the balance supports withdrawal amount
            print(f"INSUFFICIENT FUNDS")
        else:
            account.withdraw(node.amount) # update balance and tell updated information to user
            print(f"ACCOUNT #{account.__accountNum()} NEW BALANCE: ${account.__balance()}")
###################################################################
#####         balance(node) - Displays account info          ######
###################################################################
    def balance(self, node):

        account = self.find_acct(node.account) # check if account number is valid
        if account is None:
            print("Account not found")
            return
        else: # display account info
            print(f'ACCOUNT #{account.get_accountNumber()}'
                  f'\nACCOUNT HOLDER: {account.get_firstName()} {account.get_lastName()}'
                  f'\nBALANCE : {account.get_balance()}\n')

###################################################################
# find_acct - check for an account number in the current accounts #
###################################################################
    def find_acct(self, account_num):
        account = None
        # loop through account list
        for acct in BankAccount.allAccounts :
            if acct.get_accountNumber() == account_num : # if an object has a matching account number...
                account = acct # the object is stored in the account variable
        return account


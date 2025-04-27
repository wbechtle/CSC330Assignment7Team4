from Parser import Deposit, Withdraw, Balance, CreateNew
from BankAccount import BankAccount

class Interpreter:
    def __init__(self, program):
        self.accounts = [] # list of bank account objects
        self.program = program

    def interpret(self):
        for node in self.program.actions:
            if isinstance(node, Deposit):
                self.deposit(node)
            elif isinstance(node, Withdraw):
                self.withdraw(node)
            elif isinstance(node, Balance):
                self.balance(node)
            elif isinstance(node, CreateNew):
                self.create_new(node)
            else:
                raise Exception(f"INVALID NODE TYPE")

    #
    def create_new(self, node):
        account = BankAccount(node.first, node.last) # create new Bank Account object
        BankAccount.allAccounts.append(account) # add new account to the running list
        print(f"NEW MEMBER {account.get_firstName()} {account.get_lastName()} "
              f"\nACCOUNT #{account.get_accountNumber()}"
              f"\nBALANCE ${account.get_balance()}\n")


    def deposit(self, node):
        account = self.find_acct(node.account)
        if account is None:
            print(f"ACCOUNT #{node.account} NOT FOUND.")
        else:
            account.deposit(node.amount)
            print(f"ACCOUNT {account.get_accountNumber()} ({account.get_firstName()} {account.get_lastName()}) "
                  f"NEW BALANCE: ${account.get_balance()}")

    def withdraw(self, node):
        account = self.find_acct(node.account)
        if account is None:
            print(f"ACCOUNT #{node.account} NOT FOUND.")

        elif node.amount > account.getBalance() :
            print(f"INSUFFICIENT FUNDS")
        else:
            account.withdraw(node.amount)
            print(f"ACCOUNT #{account.__accountNum()} NEW BALANCE: ${account.__balance()}")

    def balance(self, node):

        account = self.find_acct(node.account)
        if account is None:
            print("Account not found")
            return
        else:
            print(f'ACCOUNT #{account.get_accountNumber()}'
                  f'ACCOUNT HOLDER: {account.get_firstName()} {account.get_lastName()}'
                  f'BALANCE : {account.get_balance()}')


    def find_acct(self, account_num):
        account = None
        for acct in BankAccount.allAccounts :
            if acct.get_accountNumber() == account_num :
                account = acct
        return account


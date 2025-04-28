##############################################
# CSC 330 Language Design and Implementation
# Final Project - Banking DSL
##############################################

from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
from BankAccount import BankAccount
import unittest
#import BankAccount

#######################################
###              MAIN              ####
#######################################

def main():
    BankAccount.allAccounts.clear()
    BankAccount.currNum = 100000
    commands = ['CREATE "MICKEY" "MOUSE"',
        'CREATE "CHARLIE" "BROWN"',
        'CREATE "BUGS" "BUNNY"',
        'CREATE "SCOOBY" "DOO"',
        'CREATE "TIMMY" "TURNER"',
        'DEPOSIT 500 *MM100000*',
        'DEPOSIT 500 *CB100001*',
        'DEPOSIT 500 *BB100002*',
        'DEPOSIT 500 *SD100003*',
        'DEPOSIT 500 *TT100004*'
        ]
    token_list = []

    for cmnd in commands:
        run(cmnd)
    print()

    run_shell()

#####################################################################
## run() - attempts to perform all the steps to run a DSL command ###
#####################################################################
def run(text) :
    lexer = Lexer(text)
    tokens = lexer.make_tokens()
    parser = Parser(tokens)
    AST = parser.parse()
    interpreter = Interpreter(AST)
    interpreter.interpret()
#####################################################################
####  run_shell() - Allows for user input in the command line   #####
#####################################################################
def run_shell():
    text = None
    while text != "END":  # program loop continues until user types done
        print('Enter a command:')
        print('CREATE "FIRST" "LAST"')
        print('DEPOSIT AMOUNT *XX000000*')
        print('WITHDRAW AMOUNT *XX000000*')
        print('BALANCE *XX000000*')
        print('RUN TEST')
        text = input('\nBankingDSL > ')  # takes in user input in the shell
        if text == 'RUN TEST':
            specification_tests()
        else:
            try:
                run(text)
            except Exception:
                print("INVALID COMMAND")

def specification_tests():
    class TestBankingDSL(unittest.TestCase):
        def setUp(self):
            # reset DSL state before each test
            BankAccount.allAccounts.clear()
            BankAccount.currNum = 100000

        def test_create_account(self):
            run('CREATE "Test" "User"')
            self.assertEqual(len(BankAccount.allAccounts), 1)
            acct = BankAccount.allAccounts[0]
            self.assertEqual(acct.first_name, "Test")
            self.assertEqual(acct.last_name, "User")

        def test_deposit(self):
            run('CREATE "Test" "User"')
            acct = BankAccount.allAccounts[0]
            run(f'DEPOSIT 123.45 *{acct.account_number.strip("*")}*')
            self.assertAlmostEqual(acct.balance, 123.45)

        def test_withdraw(self):
            run('CREATE "Test" "User"')
            acct = BankAccount.allAccounts[0]
            run(f'DEPOSIT 200 *{acct.account_number.strip("*")}*')
            run(f'WITHDRAW 50 *{acct.account_number.strip("*")}*')
            self.assertAlmostEqual(acct.balance, 150.0)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestBankingDSL)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # print overall summary
    if result.wasSuccessful():
        print("\nAll specification tests passed!")
    else:
        total_failures = len(result.failures) + len(result.errors)
        print(f"\n{total_failures} test(s) failed:")
        for test, tb in result.failures:
            print(f"  FAIL: {test.id()}")
        for test, tb in result.errors:
            print(f"  ERROR: {test.id()}")

if __name__ == '__main__':
    main()


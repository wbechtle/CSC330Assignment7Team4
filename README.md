CSC330 Language Design and Implementation - Banking DSL
Course Information

Course Name: CSC330 Language Design and Implementation
Term: Spring 2025

Team Members

Dominic Stencel
Wyatt Bechtle
Layla Heath

Project Overview
This final project involves developing a Domain-Specific Language (DSL) called "Banking" using Python. Our language implements a banking application with features for account creation, deposits, withdrawals, and balance checking. The project includes a complete language implementation pipeline: grammar definition (EBNF), lexer, parser, Abstract Syntax Tree (AST), and interpreter, along with specification tests.

Class/Module Contributions

Dominic Stencel
Developed the following components:

BankAccount class: Core banking functionality implementation
ASTNode class: Abstract Syntax Tree node representation


Wyatt Bechtle
Developed the following components:
Parser class: Parsing tokenized input into structured format
Token class: Token representation for the language


Layla Heath
Developed the following components:
Lexer class: Tokenization of Banking language inputs
Grammar file: banking.ebnf language definition
Interpreter class: Execution of parsed Banking language commands



Everyone:
Banking file: Everyone added their class to the file and contributed their portion to it






Installation Requirements
Before running this application, ensure you have the following installed:

Python 3.8 or higher
Python unittest module (included in standard library)

No additional external libraries are required for this project.
Installation Instructions

Extract the zip file to your desired location
unzip BankingDSL.zip -d [destination-folder]

Navigate to the project directory
cd [project-directory]

Verify file structure
The project should contain the following files and directories:

banking.py - Main program file
bank_account.py - BankAccount class definition
lexer.py - Lexer implementation
parser.py - Parser implementation
ast_node.py - AST Node implementation
interpreter.py - Interpreter implementation
banking.ebnf - Grammar definition file
tests/ - Directory containing specification tests
sample_accounts.txt - (Optional) Sample account data



Running the Application
Method 1: Running the Banking Program

Run the main application file:
python banking.py

The program will start and display a menu with the following options:

Enter an account ID to access an account
Create a new account
Run specification tests
Exit the program


When accessing an account, you will be presented with options to:

Make a deposit
Make a withdrawal
Check the balance
Log out of the account



Method 2: Running Components Separately
To view the intermediate steps of language processing:

To run just the lexer and see tokens:
python banking.py --lexer-only "deposit 100"

To run the parser and see the AST:
python banking.py --parser-only "deposit 100"

To run specification tests only:
python banking.py --run-tests


Language Features and Usage Examples
Banking DSL Syntax
Our Banking DSL supports the following commands:
Create Account
create account John Doe 123456
This creates a new account with first name "John", last name "Doe", and assigns an account number "JD123456".
Deposit
deposit 500
This deposits $500 into the currently selected account.
Withdraw
withdraw 200
This withdraws $200 from the currently selected account.
Check Balance
balance
This displays the current balance of the selected account.
Using the Interactive Program

When you start the program, you'll see existing account IDs displayed
Enter an account ID to access that account
Choose from the menu options to perform banking operations
To exit an account, select the logout option
To exit the program, type "exit" or "quit" at the main menu

Language Implementation Details
Grammar (EBNF)
Our banking language grammar is defined in banking.ebnf. The grammar describes the syntax rules for all supported commands including account creation, deposits, withdrawals, and balance checks.

Lexer
The lexer (Lexer class) converts input strings into tokens representing command types, identifiers, numbers, and other elements of our language.
Parser

The parser (Parser class) takes tokens from the lexer and builds a structured representation according to our grammar rules.

Abstract Syntax Tree (AST)
The AST (ASTNode class) represents the hierarchical structure of parsed commands, making them easier to interpret.

Interpreter
The interpreter (Interpreter class) processes the AST and executes the corresponding banking operations on BankAccount objects.
Specification Tests

Our program includes specification tests that verify:

Account creation with proper account number formatting
Deposits increasing account balance correctly
Withdrawals decreasing account balance correctly
Balance queries returning accurate values
Error handling for invalid operations (e.g., withdrawing more than available)

To run all specification tests:
python banking.py --run-tests
Troubleshooting
Common Issue 1: Unknown Account ID

Cause: Attempting to access an account that doesn't exist
Solution: Note the account IDs displayed at startup, or create a new account

Common Issue 2: Invalid Withdrawal Amount

Cause: Attempting to withdraw more money than is available in the account
Solution: Check your balance first and withdraw an amount less than or equal to your balance

Common Issue 3: Syntax Errors in DSL Commands

Cause: Incorrectly formatted commands
Solution: Review the command syntax examples provided above

References and Citations

Python Software Foundation. (2023). Python Language Reference, version 3.8. https://docs.python.org/3.8/

Ruslan's Blog. (2019). Let's Build A Simple Interpreter. https://ruslanspivak.com/lsbasi-part1/
YouTube Tutorial: "Create YOUR OWN Programming Language" by CodePulse. https://www.youtube.com/watch?v=Eythq9848Fg

Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). Introduction to Automata Theory, Languages, and Computation (3rd Edition). Pearson.

Video Demonstration
A video demonstration of this project can be found in the submitted files. The video walks through all components of our Banking DSL implementation and shows the program in action.
Additional Notes

All code follows best programming practices as specified in the assignment:

No infinite loops (while True)
No break or continue statements
Single return statement per function
Comprehensive comments throughout


The Banking DSL implements error handling for invalid inputs and operations
Account numbers are generated using the first letter of the first name and last name, followed by 6 digits

# Wyatt Bechtle
# CSC 330 100
# Session 7
# Final Project
# 4/20/25
####################################################
######              ParserTester              ######
####################################################  
# This file is used to develop and test aspects of the
# Parser class and it's associated class (Lexer, ASTNode)
from banking import Lexer
from Parser import Parser
###################################
####         testCommand       ####
################################### 
# Test function which takes commands,
# feeds them to the Lexer, and pass the
# Lexer's output to the Parser to create
# an AST
def testCommand(cmd):
    # Display the original command
    print(f"Command: {cmd}")
    # Try to make tokens via Lexer
    try:
        result = Lexer(cmd).make_tokens()
    except Exception as e:
        print("Lexer exception:", e)
        print("-" * 40)
        return
    # Check if result need to be unpacked because of 
    # potential tuple and check for error
    if isinstance(result, tuple):
        tokens, err = result
        if tokens is None:
            print("Lexer error:", err)
            print("-" * 40)
            return
    else:
        tokens = result
    # Display list of tokens from Lexer
    print("Tokens:", tokens)
    # Try parsing into AST
    try:
        program = Parser(tokens).parse()
        # Display the string representation of the top node (program)
        print(repr(program))
        # Loop through the actions in the program, display their details
        for action in program.actions:
            print(type(action).__name__, vars(action))
    except Exception as e:
        print("Parser error:", e)
    print("-" * 40)
# Run if file loaded as main
if __name__ == '__main__':
    # DSL commands (Test input)
    commands = [
        'CREATE NEW "Alice" "Smith"',
        'DEPOSIT 250.00 *AS123456*',
        'WITHDRAW 75 *AS123456*',
        'BALANCE *AS123456*',
        'END'
    ]
    # for each command, testCommand
    for cmd in commands:
        testCommand(cmd)

# Wyatt Bechtle
# CSC 330 100
# Session 7
# Final Project
# 4/18/25

from Token import Token     
from ASTNode import ASTNode 

####################################################
######                 PROGRAM                ######
####################################################   
class Program(ASTNode):
    # A Program Node in the Banking DSL | Represents the root of the AST
    # 
    # Attributes:
    #    actions -> List of action nodes (Deposit, Withdraw, Balance, CreateNew)
    def __init__(self, actions):
        # List of AST nodes (Deposit, Withdraw, Balance, CreateNew)
        self.actions = actions

    def __repr__(self):
        # For each action node in the program, get the string representation
        # and join it with the other action nodes to form a string to return
        # Prints like (Program <action> <action>)
        actionsString = ' '.join(repr(a) for a in self.actions)
        return f"(Program {actionsString})"

####################################################
######                 DEPOSIT                ######
####################################################   
class Deposit(ASTNode):
    # A Deposit Node in the Banking DSL 
    # 
    # Attributes:
    #    amount -> TT_INT or TT_FLOAT type token 
    #    account -> TT_ACCOUNT_NUMBER type token
    def __init__(self, amount, account):
        self.amount = amount
        self.account = account

    def __repr__(self):
        # Prints like (DEPOSIT <amount> <account>)
        return f"(DEPOSIT {self.amount} {self.account})"

####################################################
######                WITHDRAW                ######
####################################################   
class Withdraw(ASTNode):
    # A Withdraw Node in the Banking DSL 
    # 
    # Attributes:
    #    amount -> TT_INT or TT_FLOAT type token 
    #    account -> TT_ACCOUNT_NUMBER type token
    def __init__(self, amount, account):
        self.amount = amount
        self.account = account

    def __repr__(self):
        # Prints like (WITHDRAW <amount> <account>)
        return f"(WITHDRAW {self.amount} {self.account})"

####################################################
######                 BALANCE                ######
####################################################   
class Balance(ASTNode):
    # A Balance Node in the Banking DSL 
    ###################################
    ####         CONSTRUCTOR       ####
    ###################################   
    # 
    # Attributes:
    #    account -> TT_ACCOUNT_NUMBER type token
    def __init__(self, account):
        self.account = account
    ###################################
    ####   STRING REPRESENTATION   ####
    ################################### 
    def __repr__(self):
        # Prints like (BALANCE <account>)
        return f"(BALANCE {self.account})"

####################################################
######               CREATENEW                ######
####################################################   
class CreateNew(ASTNode):
    # A CreateNew Node in the Banking DSL 
    ###################################
    ####         CONSTRUCTOR       ####
    ################################### 
    # Attributes:
    #    first -> TT_STRING type token 
    #    last -> TT_STRING type token
    def __init__(self, first, last):
        self.first = first
        self.last = last
    ###################################
    ####   STRING REPRESENTATION   ####
    ################################### 
    def __repr__(self):
        # Prints like (CREATE NEW <first> <last>)
        return f"(CREATE NEW {self.first} {self.last})"

####################################################
######                  PARSER                ######
####################################################   
class Parser:
    # The Parser for the Banking DSL 
    ###################################
    ####         CONSTRUCTOR       ####
    ###################################  
    # Attributes:
    #    tokens -> List of Token objects from the Lexer
    def __init__(self, tokens):
        self.tokens = tokens
        # Starting position is index 0
        self.pos = 0
        # Current token is first token in tokens
        # If statement checks that tokens is not empty
        self.current = tokens[0] if tokens else None
    ###################################
    ####           advance         ####
    ###################################
    # Moves to the next token in the list and returns it
    # Increments Parser's posistion and returns new current token 
    def advance(self):
        self.pos += 1
        # Check if position is less than token list length
        if self.pos < len(self.tokens):
            self.current = self.tokens[self.pos]
        else:
            self.current = None
        return self.current
    ###################################
    ####            parse          ####
    ################################### 
    # Parses all tokens until an END token is read
    # Returns the root Program node
    # Calls specified parse methods to haendle each 
    # action
    def parse(self):
        # Initialize empty list to hold actions
        actions = []
        # Keep parsing until TT_END token is read 
        # or tokens runs out of elements 
        while self.current and self.current.type != Token.TT_END:
            # Append new nodes to the actions list
            actions.append(self.parseAction())
        return Program(actions)
    ###################################
    ####         parseAction       ####
    ################################### 
    # Determines the parse method based on the current token type
    def parseAction(self):
        # Check for none (No token)
        if self.current is None:
            raise SyntaxError("Unexpected end of input while expecting action")
        # Get the current Token's type
        tokenType = self.current.type
        # Check for each type of token that represents an action
        # Call that type's associated parse method
        if tokenType == Token.TT_DEPOSIT:
            return self.parseDeposit()
        if tokenType == Token.TT_WITHDRAW:
            return self.parseWithdraw()
        if tokenType == Token.TT_BALANCE:
            return self.parseBalance()
        if tokenType == Token.TT_CREATE:
            return self.parseCreate()
        # Unknown action
        raise SyntaxError(f"Unexpected token {self.current}")
    ###################################
    ####        parseDeposit       ####
    ################################### 
    # Parses a deposit action: DEPOSIT amount accountNumber
    def parseDeposit(self):
        # Consumes DEPOSIT token
        self.advance()  
        # Call expect method to ensure a token of type TT_INT or TT_FLOAT
        amountToken = self.expect(Token.TT_INT, Token.TT_FLOAT)
        # Call expect method to ensure a token of type TT_ACCOUNT_NUMBER
        accountToken = self.expect(Token.TT_ACCOUNT_NUMBER)
        return Deposit(amountToken.value, accountToken.value)
    ###################################
    ####        parseWithdraw      ####
    ################################### 
    # Parses a withdraw action: WITHDRAW amount accountNumber
    def parseWithdraw(self):
        # Consumes WITHDRAW token
        self.advance()  
        # Call expect method to ensure a token of type TT_INT or TT_FLOAT
        amountToken = self.expect(Token.TT_INT, Token.TT_FLOAT)
        # Call expect method to ensure a token of type TT_ACCOUNT_NUMBER
        accountToken = self.expect(Token.TT_ACCOUNT_NUMBER)
        return Withdraw(amountToken.value, accountToken.value)
    ###################################
    ####         parseBalance      ####
    ################################### 
    # Parses a balance action: BALANCE accountNumber
    def parseBalance(self):
        # Consumes BALANCE token
        self.advance()  
        # Call expect method to ensure a token of type TT_ACCOUNT_NUMBER
        accountToken = self.expect(Token.TT_ACCOUNT_NUMBER)
        return Balance(accountToken.value)
    ###################################
    ####         parseCreate       ####
    ################################### 
    # Parses a create new action: CREATE NEW firstName lastName
    def parseCreate(self):
        # Consumes CREATE token
        self.advance()  
        # Consumes NEW token
        # self.advance()
        # Call expect method to ensure tokens of type TT_STRING
        firstName = self.expect(Token.TT_STRING)
        lastName  = self.expect(Token.TT_STRING)
        return CreateNew(firstName.value, lastName.value)
    ###################################
    ####           expect          ####
    ################################### 
    # Checks that the current token is one of the specified types
    # If not, it raises a SyntaxError
    # Otherwise, it will advance past the token and return it
    def expect(self, *types):
        if not self.current or self.current.type not in types:
            raise SyntaxError(f"Expected one of the following types: {types}, got {self.current}")
        tok = self.current
        self.advance()
        return tok

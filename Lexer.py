# Layla Heath
# CSC 330 100
# Session 7
# Final Project - Lexer Class
# 4/27/2025

from Token import Token
#from Error import Error
###################################
#####          LEXER          #####
###################################
class Lexer:

    # Tokens - Changed to match EBNF update - WB
    DIGITS = '0123456789'  # for all numbers
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'  # letters

    TT_INT = 'INT'
    TT_FLOAT = 'FLOAT'
    TT_STRING = 'STRING'
    TT_DEPOSIT = 'DEPOSIT'  # action
    TT_WITHDRAW = 'WITHDRAW'  # action
    TT_BALANCE = 'BALANCE'  # action
    TT_CREATE = 'CREATE'  # action
    TT_ACCOUNT_NUMBER = 'ACCOUNT_NUMBER'
    TT_END = 'END'  # Or TT_EXIT
    def __init__(self, text):
        self.text = text.strip() # leading and trailing whitespace eliminated
        self.pos = -1
        self.current_char = None
        self.advance()  # advances to first value upon initialization

    # Moves to the nexxt character
    def advance(self):
        self.pos += 1 # position is increased by 1
        # assigns current_char to the character at that index
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
        # if index out of range, current_char is assigned none

    def make_tokens(self):
        tokens = [] # list to hold the tokens

        # Once the end of the command is reached, current_char is assigned 'None'
        while self.current_char != None:

            if self.current_char in ' \t':
                self.advance()  # ignores spaces and tabs

            # check for DEPOSIT command if the pos is at index 0
            elif self.text.startswith("DEPOSIT") and self.pos == 0:
                tokens.append(Token(Token.TT_DEPOSIT, "DEPOSIT")) # adds deposit token to list
                # Advances past 'DEPOSIT in the command'
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()

            # check for WITHDRAW command if the pos is at index 0
            elif self.text.startswith("WITHDRAW") and self.pos == 0:
                tokens.append(Token(Token.TT_WITHDRAW, "WITHDRAW"))
                # advances past the 'WITHDRAW'
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()

            # check for CREATE command if the pos is at index 0
            elif self.text.startswith("CREATE") and self.pos == 0:
                tokens.append(Token(Token.TT_CREATE, "CREATE"))
                # Advances past the 'CREATE'
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()

            # check for BALANCE command if the pos is at index 0
            elif self.text.startswith("BALANCE") and self.pos == 0:
                tokens.append(Token(Token.TT_BALANCE))
                # Advances past 'BALANCE'
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()

            # check for END command if the pos is at index 0
            elif self.text.startswith("END") and self.pos == 0:
                tokens.append(Token(Token.TT_END, "END"))
                self.current_char = None

            # if the char is a number...
            elif self.current_char in Token.DIGITS:
                # make_number is called to check if a valid INT or float is created
                tokens.append(self.make_number())

            # * indicates an account number
            elif self.current_char == "*" :
                tokens.append(self.make_account_num())
                # make_account_num() is called to check if the account number is valid

            # " indicates a string
            elif self.current_char == '"':
                tokens.append(self.make_string())
                # make string is called to check if there is a valid string

            else:
                char = self.current_char
                self.advance() # next character
                # error is thrown, because the character does not fall under any token definitions
                return None, Error.IllegalCharError(self.current_char, self.current_char, char)

        return tokens # returns the list of tokens

    def make_number(self):
        num_str = '' # will become the final number
        dot_count = 0 # checks for decimal

        while self.current_char != None and self.current_char in Token.DIGITS + '.':
            if self.current_char == '.':

                if dot_count == 1: self.current_char = None # loop exited if it has more than 1 period
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char # character is added to final string
            self.advance()
        if dot_count == 0: # returns int if there are no decimals
            token = Token.TT_INT
            number = int(num_str)
        else:
            token = Token.TT_FLOAT # returns float if there are decimals
            number = float(num_str)

        return Token(token, number) # Token object returned


    def make_string(self):
        start = self.current_char # start char for Error
        self.advance() # starts at character after the quotation mark
        new_str = ''

        while self.current_char != None and self.current_char != '"': # while end " is not met and there are still chars
            new_str += self.current_char # next char is added to the string
            self.advance() # move to next char

        if self.current_char == '"': # checks for closing quote
            self.advance()
            return Token(Token.TT_STRING, new_str)
        else:
            end = self.current_char
            return None, IllegalCharError(start, end, "Closing quote missing") # informs user of missing quote


    def make_account_num(self):
        self.advance()
        start = self.current_char
        end = None
        act_num = ''

        while self.current_char != None and self.current_char != "*":
            if len(act_num) < 2: # first 2 characters a checked to ensure they are letters
                if self.current_char not in Lexer.LETTERS:
                    end = self.current_char
            else:
                if self.current_char not in Lexer.DIGITS:
                    print(self.current_char)
                    end = self.current_char # assigned if there is an error with the following digits
            act_num += self.current_char
            self.advance()

        self.advance()

        if len(act_num) == 8 and end == None: # returns if it is proper length and the end was not assigned
            return Token(Token.TT_ACCOUNT_NUMBER, act_num)
        return None, IllegalCharError(start, end, "Invalid characters")


#######################################
#######          ERRORS        ########
#######################################
class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start # start position
        self.pos_end = pos_end #end position
        self.error_name = error_name # error name
        self.details = details  # details

    def as_string(self):
        result = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result


# used when lexer comes across an unsupported character;
class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

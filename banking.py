##############################################
# CSC 330 Language Design and Implementation
# Final Project - Banking DSL
##############################################
# LATEST UPDATE 4/19
# When you run the file there are commands in the main function undergoing lexical analysis
# to return tokens


# put into a class later - create a new class or include in another

# Tokens
DIGITS = '0123456789' # for all numbers
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # all caps numbers

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_STRING = 'STRING'
TT_DEPOSIT = 'DEPOSIT' # action
TT_WITHDRAW = 'WITHDRAW' # action
TT_BALANCE = 'BALANCE' # action
TT_CREATE = 'CREATE' # action
TT_ACCOUNT_NUMBER = 'ACCOUNT_NUMBER'
TT_END = 'END'  # Or TT_EXIT

#######################################
# MAIN
#######################################

def main():
    commands = [
        'CREATE "Layla" "Heath"',
        'DEPOSIT 200.00 *LH000000*',
        'WITHDRAW 50 *MH123456*',
        'BALANCE *01234567*',
        'END',
        '"hello ',
        'PRINT',

    ]
    for cmnd in commands:
        lexer = Lexer(cmnd)
        tokens = lexer.make_tokens()
        print(tokens)


#######################################
# BANKING
#######################################
class Banking:  # All
    '''
    Field needed:
    -first name
    -last name
    -account number (an 8-digit code starting with 2 letters)
    -4 actions
        - deposit
        - withdraw
        - balance
        - create new account
    - while loop that runs the program until exit word is entere
    '''


#######################################
# TOKEN
#######################################
class Token:  # Wyatt
    '''
    Finish Later
    '''

    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'


#######################################
# INTERPRETER
#######################################
class Interpreter:  # Dom
    '''
    Finish Later
    '''


#######################################
# ASTNODE
#######################################
class ASTNode:  # Dom
    '''
    finish later
    '''


#######################################
# BANKACCOUNT
#######################################
class BankAccount:  # Dom
    '''
    Finish Later
    '''


#######################################
# PARSER
#######################################
class Parser:  # Wyatt
    '''
    Finish Later
    '''


#######################################
# LEXER
#######################################
# need to work on changing these to have 1 return statement
class Lexer:  # Layla

    #
    def __init__(self, text):
        self.text = text # command being evaluated
        self.pos = -1
        self.current_char = None
        self.advance()  # advances to first value

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
                tokens.append(Token(TT_DEPOSIT)) # adds deposit token to list
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
                tokens.append(Token(TT_WITHDRAW))
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
                tokens.append(Token(TT_CREATE))
                # Advances past the 'CREATE'
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()

            # check for BALANCE command if the pos is at index 0
            elif self.text.startswith("BALANCE") and self.pos == 0:
                tokens.append(Token(TT_BALANCE))
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()

            # check for END command if the pos is at index 0
            elif self.text.startswith("END") and self.pos == 0:
                tokens.append(Token(TT_END))
                self.current_char = None

            # if the char is a number...
            elif self.current_char in DIGITS:
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
                return None, IllegalCharError(self.current_char, self.current_char, char)

        return tokens # returns the list of tokens

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))


    def make_string(self):
        start = self.current_char
        self.advance()
        new_str = ''
        while self.current_char != None and self.current_char != '"':
            new_str += self.current_char
            self.advance()

        if self.current_char == '"':
            self.advance()
            return Token(TT_STRING, new_str)
        else:
            end = self.current_char
            return None, IllegalCharError(start, end, "Closing quote missing")


    def make_account_num(self):
        self.advance()
        start = self.current_char
        end = None
        act_num = ''

        while self.current_char != None and self.current_char != "*":
            if len(act_num) < 2:
                if self.current_char not in LETTERS:
                    end = self.current_char
            else:
                if self.current_char not in DIGITS:
                    print(self.current_char)
                    end = self.current_char
            act_num += self.current_char
            self.advance()

        self.advance()

        if len(act_num) == 8 and end == None:
            return Token(TT_ACCOUNT_NUMBER, act_num)
        return None, IllegalCharError(start, end, "Invalid characters")


#######################################
# ERRORS - NEED TO FIX
#######################################
class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result


# used when lexer comes across an unsupported character;
class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)


if __name__ == '__main__':
    main()
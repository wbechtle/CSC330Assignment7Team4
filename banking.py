class Banking: #All


    content = ""
    with open('test.lang', 'r') as file:
        content = file.read()

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
    - while loop that runs the program until exit word is entered

    '''
DIGITS = '0123456789'

TT_INT = 'TT_INT'  # integers will be used for account nunber
TT_FLOAT = 'TT_FLOAT'  # balance will be a float
TT_STRING = 'TT_STRING'  # used for account info
TT_PLUS = 'TT_PLUS'  # used to deposit
TT_MINUS = 'TT_MINUS'  # used to withdraw

class Token: # Wyatt
    '''
            Finish Later
            '''


    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'


class Interpreter: # Dom
    '''
    Finish Later
    '''

class ASTNode: # Dom
    '''
    finish later
    '''

class BankAccount: #Dom
    '''
    Finish Later
    '''

class Parser: # Wyatt
    '''
    Finish Later
    '''

class Lexer: # Layla
    '''
    Finish Later
    '''


    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance() # ignores spaces and tabs
            elif self.current_char in DIGITS:
                tokens.append(self.make_number)
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + {char}+ "'")



        return tokens

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
#######################################
# ERRORS
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


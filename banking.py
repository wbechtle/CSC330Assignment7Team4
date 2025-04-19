class Banking: #All
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

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_STRING = 'STRING'
TT_DEPOSIT = 'DEPOSIT'
TT_WITHDRAW = 'WITHDRAW'
TT_BALANCE = 'BALANCE'
TT_CREATE = 'CREATE'
TT_ACCOUNT_NUMBER = 'ACCOUNT_NUMBER'
TT_END = 'END'  # Or TT_EXIT


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

   #
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance() # advances so first character is

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance() # ignores spaces and tabs
            elif self.text.startswith("DEPOSIT"):
                tokens.append(Token(TT_DEPOSIT))
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()

            elif self.text.startswith("WITHDRAW"):
                tokens.append(Token(TT_WITHDRAW))
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()

            elif self.text.startswith("CREATE"):
                tokens.append(Token(TT_CREATE))
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()

            elif self.text.startswith("BALANCE"):
                tokens.append(Token(TT_BALANCE))
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                self.advance()

            elif self.text.startswith("END") :
                tokens.append(Token(TT_END))
                self.current_char = None

            elif self.current_char in DIGITS:
                tokens.append(self.make_number())

            elif self.current_char == '"':
                tokens.append(self.make_string())

            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char+ "'")



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

    def make_string(self):

        self.advance()
        new_str = ''
        while self.current_char != None and self.current_char != '"':
            new_str += self.current_char
            self.advance()
        if self.current_char == '"':
            self.advance()
            return Token(TT_STRING, new_str)
        return None, IllegalCharError("Closing quote missing")
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


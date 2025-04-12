import Token
class Lexer:

    '''
    Finish Later
    '''
    TT_INT = 'TT_INT'  # integers will be used for account nunber
    TT_FLOAT = 'TT_FLOAT'  # balance will be a float
    TT_STRING = 'TT_STRING'  # used for account info
    TT_PLUS = 'TT_PLUS'  # used to deposit
    TT_MINUS = 'TT_MINUS'  # used to withdraw
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def get_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance() # ignores spaces and tabs
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            ''' finish later'''

class Token:
    '''
    Finish Later
    '''
    TT_INT = 'TT_INT' # integers will be used for account nunber
    TT_FLOAT = 'TT_FLOAT' # balance will be a float
    TT_STRING = 'TT_STRING' # used for account info
    TT_PLUS = 'TT_PLUS' # used to deposit
    TT_MINUS = 'TT_MINUS' # used to withdraw

    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'

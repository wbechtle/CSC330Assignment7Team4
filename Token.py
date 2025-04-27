# Wyatt Bechtle
# CSC 330 100
# Session 7
# Final Project
# 4/18/25
class Token:

    # A token in the Banking DSL
    # 
    # Attributes:
    #    type  -> One of the TT_* token type constants
    #    value -> The literal value (int, float, or str)
    ####################################################
    ######               CONSTANTS                ######
    ####################################################                                         
    # Tokens - Changed to match EBNF update - WB
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

    ####################################################
    ######               CONSTRUCTOR              ######
    #################################################### 
    # Arguements: 
    #       type_ -> token type
    #       value -> token's value from input
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value

    ####################################################
    ######           STRING REPRESENTATION        ######
    #################################################### 
    def __repr__(self):
        # This if statement evaluates to false for a values of "0" and "0.0"
        #if self.value: return f'{self.type}: {self.value}'
        #return f'{self.type}'

        # Initialize parts list with the first value being the token's type
        parts = [self.type]

        # Check token is present
        if self.value is not None:

            # Add the token value to the parts list
            parts.append(repr(self.value))

        # Return example: "TT_INT: 1"
        return ': '.join(parts)

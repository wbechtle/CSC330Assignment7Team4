# Added import - WB
from ast import AST
class ASTNode(object):
    pass

''' Binary Operator class to represent all four binary operators (add, sub., mult., divide)
Can Combine all four since they all function the same where you have an: 
expression to the left, an operator, and a expression to the right ''' 
class BinOp(ASTNode):
    def __init__(self, leftNode, opNode, rightNode):
        self.leftNode = leftNode
        self.opNode = opNode
        self.rightNode = rightNode

    def __repr__(self):
        return f'{self.token}'
    
# Num Class to represent numbers and their value
class NumNode(ASTNode):
    def __init__(self, token):
        self.token= token
    # Fixed spacing - WB
    def __repr__(self):
        return f'{self.token}'

# Deposit Class to represent the deposit action
class DepositNode(ASTNode):
    def __init__(self, accountNum, amount):
        self.account = accountNum
        self.amount = amount

# Withdraw class to represent the withdraw action
class WithdrawNode(ASTNode):
    def __init__(self, accountNum, amount):
        self.accout = accountNum
        self.amount = amount

# New Account class to represent the create new account action
class NewAccountNode(ASTNode):
    def __init__(self, firstName, lastName, accountNum, balance):
        self.firstName = firstName
        self.lastName = lastName
        self.accountNum = account
        self.balance = balance
    

''' Editing this out
We will handle visiting nodes in the parser class
class NodeVisitor(object):
    def visit(self, node):
        # Fixed spelling - WB
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
        
# Fall back method to raise an exception if it encounters a node isn't recognized 
def generic_visit(self, node):
    # Fixed parenthesis
    raise Exception('No Visit_{} method'. format(type(node.__name__)))
'''

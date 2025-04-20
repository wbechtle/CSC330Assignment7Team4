class ASTNode(object):
    pass

''' Binary Operator class to represent all four binary operators (add, sub., mult., divide)
Can Combine all four since they all function the same where you have an: 
expression to the left, an operator, and a expression to the right ''' 
class BinOp(AST):
    def __init__(self, leftNode, opNode, rightNode):
        self.leftNode = leftNode
        self.opNode = opNode
        self.rightNode = rightNode

    def __repr__(self):
        return f'{self.token}'
    
# Num Class to represent numbers and their value
class NumNode:
    def __init__(self, token):
        self.token= token
        
    def__repr__(self):
        return f'{self.token}'

class NodeVisitor(object):
    def visit(self, node):
        methond_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
        
# Fall back method to raise an exception if it encounters a node isn't recognized 
def generic_visit(self, node):
    raise Exception('No Visit_{} method'. format(type(node.__name__))

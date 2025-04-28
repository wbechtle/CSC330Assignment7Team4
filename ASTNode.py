# Dominic Stencel
# CSC 330 100
# Session 7
# Final Project - AstNode Class
# 4/12/2025

# Added import - WB
from ast import AST

####################################################
######               ASTNode                  ######
####################################################
class ASTNode(object):
    pass

####################################################
######               BinOp                    ######
####################################################
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



####################################################
######               NumNode                  ######
####################################################
# Num Class to represent numbers and their value
class NumNode(ASTNode):
    def __init__(self, token):
        self.token= token
    # Fixed spacing - WB
    def __repr__(self):
        return f'{self.token}'

####################################################
######     Deposit, Withdraw, CreateNew       ######
####################################################
# These nodes will be included in the Parser class

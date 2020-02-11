"""
Inspired from: https://www.mattlayman.com/blog/2018/decipher-python-ast/

Information of each node from here: https://greentreesnakes.readthedocs.io/en/latest/nodes.html
"""

import ast

class Analyzer(ast.NodeVisitor):
    
    def __init__(self):
        """
        """
        self.ifs = []
        self.nums = []

    def visitChildren(self, node):
        """
        This is the command for visiting all children of a node.
            This is a method so it is a centralized call.
        """
        self.generic_visit(node)

    def visit_Num(self, node):
        """
        class Num(n)
            Deprecated since version 3.8: Replaced by Constant

            A number - integer, float, or complex. The n attribute stores the value, already converted to the relevant type.
        """
        self.nums.append(node)
        self.visitChildren(node)

    def visit_If(self, node):
        """
        class If(test, body, orelse)
            An if statement. test holds a single node, such as a Compare node. body and orelse each hold a list of nodes.
            
            elif clauses don’t have a special representation in the AST, but rather appear as extra If nodes within the orelse section of the previous one.
        """
        self.ifs.append(node)
        self.visitChildren(node)

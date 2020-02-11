"""
Inspired from: https://www.mattlayman.com/blog/2018/decipher-python-ast/

Information of each node from here: https://greentreesnakes.readthedocs.io/en/latest/nodes.html
"""

import ast

from pprint import pprint

import visuals.flowchart

class Deconstruct():
    """
    """
    def __init__(self):
        self.initialize()

    def initialize(self):
        """
        """
        ##payload
        self.creation = []
        self.connections = []
        ##counters for connecting nodes
        self.ifs = 0
        self.assigns = 0
        self.numbers = 0

    def ifNode(self, node, endpoint, connection=None):
        """
        3 parts:
            Test: What is being compared, we use this for the label of the box 
            Body: What the if statement contains inside of it, connections below
            OrElse: The else/next if statement
        """
        ##increment
        self.ifs += 1
        ##Test
        name = 'if' + str(self.ifs)
        label = self._comparatorString(node.test)
        visual = visuals.flowchart.node.condition(name, label)
        self.creation.append(visual)
        ##make the connections
        if connection:
            self.connections.append(self._connect(connection, name))
        ##Body
        if isinstance(node.body[0], ast.Assign):
            if node.body[0] == node.body[-1]:
                self.assignNode(node.body[0], connectionstart=name+'(yes)', connectionend=endpoint)
            else:
                self.assignNode(node.body[0], connectionstart=name+'(yes)')
        currentName = None
        for body in node.body[1:]:
            if isinstance(body, ast.Assign):
                if not currentName:
                    currentName = name
                if body == node.body[-1]:
                    currentName = self.assignNode(body, connectionstart=currentName, connectionend=endpoint)
                else:
                    currentName = self.assignNode(body, connectionstart=currentName)

        ##OrElse
        if len(node.orelse) == 0:
            pass
        elif (len(node.orelse)==1) and (isinstance(node.orelse[0], ast.If)):
            self.ifNode(node.orelse[0], endpoint, connection=name+"(no)")
        else:
            if isinstance(node.orelse[0], ast.Assign):
                if node.orelse[0] == node.orelse[-1]:
                    self.assignNode(node.orelse[0], connectionstart=name+'(no)', connectionend=endpoint)
                else:
                    self.assignNode(node.orelse[0], connectionstart=name+'(no)')
            currentName = None
            for body in node.orelse[1:]:
                if isinstance(body, ast.Assign):
                    if not currentName:
                        currentName = name
                    if body == node.orelse[-1]:
                        self.assignNode(body, connectionstart=currentName, connectionend=endpoint)
                    else:
                        self.assignNode(body, connectionstart=currentName)
        

    def assignNode(self, node, connectionstart=None, connectionend=None):
        """
        Assign nodes have two different values we look for:
            Targets: these are all of the names to be assigned
            Value: these are all of the values to be assigned
        """
        ##increment
        self.assigns += 1
        ##
        name = 'assign' + str(self.assigns)
        prefix = []
        for target in node.targets:
            prefix.append(target.id)
        label = ', '.join(prefix) + " = " + str(node.value.n)
        visual = visuals.flowchart.node.operation(name, label)
        ##
        self.creation.append(visual)
        if connectionstart:
            self.connections.append(self._connect(connectionstart, name))
        if connectionend:
            self.connections.append(self._connect(name, connectionend))

    def _connect(self, start, finish):
        """
        Connect two nodes.
        """
        return start + "->" + finish

    def _comparatorString(self, comparator):
        """
        Return a string of the comparator being used so it can be used as a label.
        """
        ##determine the left side 
        if isinstance(comparator.left, ast.Name): 
            text = comparator.left.id
        ##grab each comparator to the right of the first
        for index in range(len(comparator.comparators)):
            ##allocate the values from within
            variable = self._comparatorName(comparator.comparators[index])
            operation = self._comparatorOperation(comparator.ops[index])
            ##add to the text
            text += " " + operation + " " + variable
        ##
        return text

    def _comparatorName(self, node):
        """
        Return a string of the variable name.
        """
        if isinstance(node, ast.Name):
            return node.id
        print("We didn't account for a variable comparator")
        sys.exit(1)

    def _comparatorOperation(self, node):
        """
        Return a string of the operation, i.e. ast.Gt = '>'
        """
        if isinstance(node, ast.Gt):
            return '>'
        elif isinstance(node, ast.Lt):
            return '<'
        elif isinstance(node, ast.Eq):
            return '=='
        elif isinstance(node, ast.LtE):
            return '<='
        elif isinstance(node, ast.GtE):
            return '>='

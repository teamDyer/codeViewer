"""
All nodes will be defined here.
"""

import ast

class Nodes():
    """
    """
    def initialize(self):
        """
        Reset the object and set all initial variables appropriately.
        """
        ##real time variables
        self.counter = 0
        ##massive dictionary that holds every possibility
        self.master = {
            ##literals
            ast.Constant: self.constantNode,
            ast.Num: self.numNode,
            ast.Str: self.strNode,
            ast.FormattedValue: self.formattedvalueNode,
            ast.JoinedStr: self.joinedstrNode,
            ast.Bytes: self.bytesNode,
            ast.List: self.listNode,
            ast.Tuple: self.tupleNode,
            ast.Set: self.setNode,
            ast.Dict: self.dictNode,
            ast.Ellipsis: self.ellipsisNode,
            ast.NameConstant: self.nameconstantNode,
            ##variables
            ast.Name: self.nameNode,
            ast.Load: self.loadNode,
            ast.Store: self.storeNode,
            ast.Del: self.delNode,
            ast.Starred: self.starredNode,
            ##expressions
            ast.Expr: self.exprNode,
            ast.UnaryOp: self.unaryopNode,
            ast.UAdd: self.uaddNode,
            ast.USub: self.usubNode,
            ast.Not: self.notNode,
            ast.Invert: self.invertNode,
            ast.BinOp: self.binopNode,
            ast.Add: self.addNode,
            ast.Sub: self.subNode,
            ast.Mult: self.multNode,
            ast.Div: self.divNode,
            ast.FloorDiv: self.floordivNode,
            ast.Mod: self.modNode,
            ast.Pow: self.powNode,
            ast.LShift: self.lshiftNode,
            ast.RShift: self.rshiftNode,
            ast.BitOr: self.bitorNode,
            ast.BitXor: self.bitxorNode,
            ast.BitAnd: self.bitandNode,
            ast.MatMult: self.matmultNode,
            ast.BoolOp: self.boolopNode,
            ast.And: self.andNode,
            ast.Or: self.orNode,
            ast.Compare: self.compareNode,
            ast.Eq: self.eqNode,
            ast.Lt: self.ltNode,
            ast.LtE: self.lteNode,
            ast.Gt: self.gtNode,
            ast.GtE: self.gteNode,
            ast.Is: self.isNode,
            ast.IsNot: self.isnotNode,
            ast.In: self.inNode,
            ast.NotIn: self.notinNode,
            ast.Call: self.callNode,
            ast.keyword: self.keywordNode,
            ast.IfExp: self.ifexpNode,
            ast.Attribute: self.attributeNode,
            ##Subscripting
            ast.Subscript: self.subscriptNode,
            ast.Index: self.indexNode,
            ast.Slice: self.sliceNode,
            ast.ExtSlice: self.extsliceNode,
            ##Comprehensions
            ast.ListComp: self.listcompNode,
            ast.SetComp: self.setcompNode,
            ast.GeneratorExp: self.generatorexpNode,
            ast.DictComp: self.dictcompNode,
            ast.comprehension: self.comprehensionNode,
            ##Statements
            ast.Assign: self.assignNode,
            ast.AnnAssign: self.annassignNode,
            ast.AugAssign: self.augassignNode,
            #ast.Print: self.printNode, #dne?
            ast.Raise: self.raiseNode,
            ast.Assert: self.assertNode,
            ast.Delete: self.deleteNode,
            ast.Pass: self.passNode,
            ##Imports
            ast.Import: self.importNode,
            ast.ImportFrom: self.importfromNode,
            ast.alias: self.aliasNode,
            ##Control Flow
            ast.If: self.ifNode,
            ast.For: self.forNode,
            ast.While: self.whileNode,
            ast.Break: self.breakNode,
            ast.Continue: self.continueNode,
            ast.Try: self.tryNode,
            #ast.TryFinally: self.tryfinallyNode, #dne?
            #ast.TryExcept: self.tryexceptNode, #dne?
            ast.ExceptHandler: self.excepthandlerNode,
            ast.With: self.withNode,
            ast.withitem: self.withitemNode,
            ##Function and class definitions
            ast.FunctionDef: self.functionNode,
            ast.Lambda: self.lambdaNode,
            ast.arguments: self.argumentsNode,
            ast.arg: self.argNode,
            ast.Return: self.returnNode,
            ast.Yield: self.yieldNode,
            ast.YieldFrom: self.yieldfromNode,
            ast.Global: self.globalNode,
            ast.Nonlocal: self.nonlocalNode,
            ast.ClassDef: self.classNode,
            ##Async and wait
            ast.AsyncFunctionDef: self.asyncfunctionNode,
            ast.Await: self.awaitNode,
            ast.AsyncFor: self.asyncforNode,
            ast.AsyncWith: self.asyncwithNode,
            ##Top level nodes
            ast.Module: self.moduleNode,
            ast.Interactive: self.interactiveNode,
            ast.Expression: self.expressionNode 
        }

    def process(self, node):
        """
        Create a visual from a node, return a completed product.
        """ 

    ##LITERALS
    def constantNode():
        pass
    def numNode():
        pass
    def strNode():
        pass
    def formattedvalueNode():
        pass
    def joinedstrNode():
        pass
    def bytesNode():
        pass
    def listNode():
        pass
    def tupleNode():
        pass
    def setNode():
        pass
    def dictNode():
        pass
    def ellipsisNode():
        pass
    def nameconstantNode():
        pass

    ##VARIABLES
    def nameNode():
        pass
    def loadNode():
        pass
    def storeNode():
        pass
    def delNode():
        pass
    def starredNode():
        pass

    ##EXPRESSIONS
    def exprNode():
        pass
    def unaryopNode():
        pass
    def uaddNode():
        pass
    def usubNode():
        pass
    def notNode():
        pass
    def invertNode():
        pass
    def binopNode():
        pass
    def addNode():
        pass
    def subNode():
        pass
    def multNode():
        pass
    def divNode():
        pass
    def floordivNode():
        pass
    def modNode():
        pass
    def powNode():
        pass
    def lshiftNode():
        pass
    def rshiftNode():
        pass
    def bitorNode():
        pass
    def bitxorNode():
        pass
    def bitandNode():
        pass
    def matmultNode():
        pass
    def boolopNode():
        pass
    def andNode():
        pass
    def orNode():
        pass
    def compareNode():
        pass
    def eqNode():
        pass
    def noteqNode():
        pass
    def ltNode():
        pass
    def lteNode():
        pass
    def gtNode():
        pass
    def gteNode():
        pass
    def isNode():
        pass
    def isnotNode():
        pass
    def inNode():
        pass
    def notinNode():
        pass
    def callNode():
        pass
    def keywordNode():
        pass
    def ifexpNode():
        pass
    def attributeNode():
        pass

    ##SUBSCRIPTING
    def subscriptNode():
        pass
    def indexNode():
        pass
    def sliceNode():
        pass
    def extsliceNode():
        pass

    ##EXPRESSIONS
    def listcompNode():
        pass
    def setcompNode():
        pass
    def generatorexpNode():
        pass
    def dictcompNode():
        pass
    def comprehensionNode():
        pass

    ##STATEMENTS
    def assignNode():
        pass
    def annassignNode():
        pass
    def augassignNode():
        pass
    def printNode():
        pass
    def raiseNode():
        pass
    def assertNode():
        pass
    def deleteNode():
        pass
    def passNode():
        pass

    ##IMPORTS
    def importNode():
        pass
    def importfromNode():
        pass
    def aliasNode():
        pass

    ##CONTROL FLOW
    def ifNode():
        pass
    def forNode():
        pass
    def whileNode():
        pass
    def breakNode():
        pass
    def continueNode():
        pass
    def tryNode():
        pass
    def tryfinallyNode():
        pass
    def tryexceptNode():
        pass
    def excepthandlerNode():
        pass
    def withNode():
        pass
    def withitemNode():
        pass

    ##DEFINITIONS
    def functionNode():
        pass
    def lambdaNode():
        pass
    def argumentsNode():
        pass
    def argNode():
        pass
    def returnNode():
        pass
    def yieldNode():
        pass
    def yieldfromNode():
        pass
    def globalNode():
        pass
    def nonlocalNode():
        pass
    def classNode():
        pass

    ##ASYNC AND WAIT
    def asyncfunctionNode():
        pass
    def awaitNode():
        pass
    def asyncforNode():
        pass
    def asyncwithNode():
        pass

    ##TOP LEVEL NODES
    def moduleNode():
        pass
    def interactiveNode():
        pass
    def expressionNode():
        pass

#######################################################################
nodes = Nodes()

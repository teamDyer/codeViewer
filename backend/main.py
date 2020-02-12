"""
"""

import ast
from pprint import pprint

import engine.analyze
import engine.deconstruct

import visuals.tree

##get the tree
example = 'examples/0001-if/main.py'
with open(example, 'r') as file:
    content = file.read()
tree = ast.parse(content)

##analyze the tree
analyzer = engine.analyze.Analyzer()
analyzer.visit(tree)
#print(analyzer.ifs)

##grab the first if statement's node
node = analyzer.ifs[0]

#pprint(vars(node))

##
deconstructor = engine.deconstruct.Deconstruct()
deconstructor.ifNode(node, 'END', connection="START")

#deconstructor.visit(node)


##make the payload
text = []
blank = ''
#start
text.append('START=>start: START')
text.append('END=>end: END')
#creation
text.append(blank)
for node in deconstructor.creation:
    text.append(node)
#
text.append(blank)
for node in deconstructor.connections:
    text.append(node)

##debug
#for line in text:
#    print(line)

#########################################

nodes = visuals.tree.nodes
nodes.initialize()
print(nodes.master.keys())

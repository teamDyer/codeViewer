"""
Found a really cool flowchart generation tool for javascript from here:
https://github.com/adrai/flowchart.js

Most of the documentation in this file comes from the readme.txt provided in the git repository.

Files will be created with this structure:
    1. Node creation
    2. Node connection
    3. Parallel nodes
    4. Customize
"""

class Node():
    """
    All avaiable node types.
    """
    def start(self):
        return "st=>start: start"

    def end(self):
        return "en=>end: end"

    def operation(self, name, label):
        return name + "=>operation: " + label

    def inputoutput(self):
        return "io=>inputoutput: inputoutput"

    def subroutine(self):
        return "sub1=>subroutine: subroutine"

    def condition(self, name, label):
        return name + "=>condition: " + label

    def parallel(self):
        return "para=>parallel: parallel"

node = Node()

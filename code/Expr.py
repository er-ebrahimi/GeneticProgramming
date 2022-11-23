
import random
import math

oneChildOp = ["sin", "cos"]
allOp = ["+", '-', '*', '/', 'sin', 'cos']
randlimit = (1,10) #generating random num between (1,10)
variable = ['x']
# print(math.cos(math.radians(60)))

class Node:
    """this class has two children
    vars:
        right: Node
        left: Node
        data: char or int
    """
    def __init__(self):
        self._right = None
        self._left = None
        self.data = allOp[random.randint(0, len(allOp) - 1)]
        self._child = None
    def printing(self):
        print(self.data)
    def getChild(self, which):
        """return the child

        Args:
            which (int): which can be 1 or 2 it is bigger than two it works like one

        Returns:
            Node: if input is one func is returned _right
                    if it is two return _left
                    if data can have one child then the return is _child
        """
        if self.data in oneChildOp:
            return self._child
        elif which == 2:
            return self._left
        else:
            return self._right
    def setChild(self, which, input):
        """set to value to childs

        Args:
            which (int): which can be 1 or 2 it is bigger than two it works like one
            input (Node or int or char): your Node or number or variable
        """
        if self.data in oneChildOp:#TODO
            self._child = input
        elif which == 2:
            self._left = input
        else:
            self._right = input
def cal(var1, op, var2):
    if op == '-':
        return var1 - var2
    if op == '*':
        return var1 * var2
    if op == '+':
        return var1 + var2
    if op == '/':
        return var1 / var2
             
    
class Expr:
    def __init__(self):
        self.node = Node()
        self.numCount = 0 #save how many number we should generate
        self.opCount = 1
        self.fitness = 0
        self.possibility = 0
        self.num = 0
    def calculator(self, x, head):#TODO if you wanna add more the one var you should change this function
        """calculate the answer of tree

        Args:
            x (int): your input to function
            head (Node): your head

        Returns:
            int or None: answer of function (division by zero return None)
        """
        try:    
            if type(head) == int:
                return head
            elif head == None:
                return None
            elif head == 'x':
                return x
            elif head.data in allOp:
                if head.data in oneChildOp:
                    value = self.calculator(x, head.getChild(1))#TODO if you wanna add more oneChild operator you should change this condition

                    if head.data == "sin":
                        return math.sin(value)
                    elif head.data == "cos":
                        return math.cos(value)
                else:
                    value1 = self.calculator(x, head.getChild(1))
                    value2 = self.calculator(x, head.getChild(2)) 
                    return cal(value1,head.data,value2)
        except (ZeroDivisionError, TypeError, AttributeError):
            return None

    def printTree(self, node):
        if type(node) != Node:
            return node
        elif node.data in oneChildOp:
            return f'{node.data}({self.printTree(node.getChild(1))})'
        elif node.data in allOp:
            return f'({self.printTree(node.getChild(1))} {node.data} {self.printTree(node.getChild(2))})'
        # while True:
    def insertNum(self,headNode ,var ):
        """It is for inserting Node 
            = [random.randint(1 , self.numCount - self.opCount )]
        Args:
            headNode (Node): root Node
            tree (Expr): your tree
            var (List): it just use firt value of list (just passby value) 
        """
        rand = 0
        if rand == 0:
            rand = random.randint(1,2)
        if type(headNode.getChild(rand)) == Node:
            self.insertNum(headNode.getChild(rand), var)
        elif headNode.getChild(rand) == None and var[0] == 0:
            headNode.setChild(rand,random.randint(randlimit[0],randlimit[1]))
        elif headNode.getChild(rand) == None:
            headNode.setChild(rand,variable[random.randint(0,len(variable) - 1)])
            var[0] -= 1
            
        rand = 2 if rand == 1 else 1 
        if type(headNode.getChild(rand)) == Node:
            self.insertNum(headNode.getChild(rand), var)
        elif headNode.getChild(rand) == None and var[0] == 0:
            headNode.setChild(rand,random.randint(randlimit[0],randlimit[1]))
        elif headNode.getChild(rand) == None:
            headNode.setChild(rand,variable[random.randint(0,len(variable) - 1)])
            var[0] -= 1

def insertNode(headNode ):
    """inserting new node

    Args:
        headNode (Node): the head of your tree (+,-,*,/)
        inputNode (char): your operator you want to add
    """
    inputNode = Node()
    # flag = False
    ran = random.randint(1, 2)

    if headNode.getChild(ran) == None:
        headNode.setChild(ran, inputNode)
    elif type(headNode.getChild(ran)) == Node:
        insertNode(headNode.getChild(ran))


def generateTree(count, tree):
    """Generate new cromosome

    Args:
        count (int): tree will have count+1 operator
        tree (Expr): your tree
    """
    tree.opCount = count + 1
    for i in range(count + 1):
        ran = random.randint(0, len(allOp) - 1)
        if allOp[ran] in oneChildOp:
            tree.numCount += 1
        else:
            tree.numCount += 2
        insertNode(tree.node )
    tree.insertNum(tree.node, [1])#TODO it always in right

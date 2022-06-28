# python code to solve the expression using the Tree data structure
from collections import deque

class Nodes:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = self
        self.data = data


    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def isOperand(self):
        if self.isalpha():
            return True



    def isdigit(self):
        if self.isdigit():
            return True
        else:
            return False





class Tree :


   def __init__ (self,postfix):

       self.Expression = postfix

   def isdigit(self, ch):
       return ch.isdigit()

   def isOperator(self,ch):
       if ch ==  "+" or ch == "+" or ch == "-" or ch == "*" or ch == "^":
           return True

   def ConstructTree(self):

       stack = []
       for i in self.Expression:
           if self.isdigit(i):
               stack.append(i)
               print(i, "pushed to stack")

           elif i == " ":
               pass

           else:

               root = Nodes(i)
               print(f"  {i} is node ")

               root.right = stack.pop()
               print(f" {root.right} append to  right child of {root} ")
               root.left = stack.pop()
               print(f" {root.left} append to  left child of {root} ")
               stack.append(root)

       return stack
   def CalculateExpression(self,tree):

       for node in tree:
           if node is None:
               node = self.root

               # empty tree
           if node is None:
               return 0

               # check if we are at the leaf, it means it is a operand
           if node.isdigit(self):
               node.value = float(node.data)
               val = float(node.data)

               return val

           left_value = self.CalculateExpression(node.left)
           right_value = self.CalculateExpression(node.right)

           # addition
           if node.data == "+":

               return left_value + right_value
           # subtraction
           elif node.data == "-":

               print(f"node value: {node.value}")
               return left_value - right_value
           # division
           elif node.data == "/":
               return left_value / right_value
           # multiplication
           elif node.data == "*":
               return left_value * right_value
           # power
           else:
               return left_value ** right_value



binaryTree = Tree("15+")
d = (binaryTree.ConstructTree())
print(binaryTree.CalculateExpression(d))














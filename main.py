class Nodes:
    def __init__(self, val=" ", operator="X"):
        self.left = None
        self.right = None
        self.operator = operator  # this will hold the operator, if value
        self.parent = None  # this will hold the address of the object that created this node
        self.val = val

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def get_val(self):
        return self.val

    def get_operator(self):
        return self.operator

    def set_val(self, val):
        self.val = val

    def set_operator(self, operator):
        self.operator = operator

    def set_right(self, new_r):
        self.right = new_r

    def set_left(self, new_l):
        self.left = new_l

    def set_parent(self, new_parent):
        self.parent = new_parent

    def isOperand(self):
        if self.isalpha():
            return True

    def isdigit(self):
        if self.isdigit():
            return True
        else:
            return False


from collections import deque


# Stack implementation
class Stack:
    # Constructor of stack class
    def __init__(self):
        self.container = deque()

    # push the number into the stack
    def push(self, val):
        self.container.append(val)

    # remove the top element
    def pop(self):
        if len(self.container) <= 0:
            return "Stack is empty!"
        else:
            return self.container.pop()

    # peek to see the top element
    def peek(self):
        return self.container[-1]

    # to check if the stack empty
    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False

    # returns the size of the stack
    def size(self):
        return len(self.container)

    def isOperand(self, ch):
        return ch.isalpha()

    def isdigit(self, ch):
        return ch.isdigit()

    def notGreater(self, i):
        priority = {
            "-": 1,
            "+": 1,
            "*": 2,
            "/": 2,
            "^": 3
        }
        if self.peek() == '(':
            return False
        a = priority[i]
        b = priority[self.peek()]
        if a <= b:
            return True
        else:
            return False

    def toPostfix(self, exp):

        output = " "

        for i in exp:
            if self.isOperand(i) == True or self.isdigit(i) == True or i == " ":
                print(i, "~ Operand push to string")
                output += i

            elif i == "(":
                self.push(i)
                print(i, "~ Found ( push to stack")

            elif i == ")":
                while (self.is_empty() != True and self.peek() != "("):
                    n = self.pop()
                output += n
                print(n, "~ Operator popped from stack")
                if (self.is_empty() != True and self.peek() != "("):
                    print("---------")
                    return -1
                else:
                    x = self.pop()
                    print(x, "popping and deleting (")

            else:
                while (self.is_empty() != True and self.notGreater(i)):
                    c = self.pop()
                    output += c
                    print(c, "operator popped after checking prority")
                self.push(i)
                print(i, "operator pushed to stack")
        while self.is_empty() != True:
            x = self.pop()
            output += x
            print(x, "pop at last")
        self.exp = output
        print(output.strip())
        return (output.strip())


def Evaluate(exp1):
    print("expression", exp1)
    strp = Stack()
    postfix = strp.toPostfix(exp1)
    res = " "
    for i in postfix:
        res = i + " " + res

    start = Nodes()
    first = True
    for i in res.split():
        # main loop to build the tree
        print(i)
        if first:
            curr = start
            curr.set_operator(i)
            print("here 1")
            first = False
        else:
            if curr.get_right() == None:
                if i == "+" or i == "-" or i == "*" or i == "/":
                    curr.set_right(Nodes(operator = i))
                    next_n = curr.get_right()
                    next_n.set_parent(curr)
                    curr = next_n
                    print("here 2")
                else:
                    curr.set_right(Nodes(val=i))
                    next_n = curr.get_right()
                    next_n.set_parent(curr)
                    print("here 3")

            elif curr.get_left() == None:
                if i == "+" or i == "-" or i == "*" or i == "/":
                    curr.set_left(Nodes(operator = i))
                    next_n = curr.get_left()
                    next_n.set_parent(curr)
                    curr = next_n
                    print("here 4")
                else:
                    curr.set_left(Nodes(val=i))
                    next_n = curr.get_left()
                    next_n.set_parent(curr)
                    print("here 5")
            else:
                while curr.get_left() != None:
                    curr = curr.get_parent()
                if i == "+" or i == "-" or i == "*" or i == "/":
                    curr.set_left(Nodes(operator=i))
                    next_n = curr.get_left()
                    next_n.set_parent(curr)
                    curr = next_n
                    print("here 6")
                else:
                    curr.set_left(Nodes(val=i))
                    next_n = curr.get_left()
                    next_n.set_parent(curr)
                    print("here 7")

    curr = start

    print(start)
    print(start.get_left())
    while start.get_left().get_operator() != "X" or start.get_right().get_operator != "X":
        if curr.get_right().get_operator() != "X":
            print("move right")
            curr = curr.get_right()
            if curr.get_left().get_operator() == "X" and curr.get_right().get_operator() == "X":
                print("Evaluate node")
                op = curr.get_operator()
                if op == "*":
                    res = float(curr.get_left().get_val()) * float(curr.get_right().get_val())
                elif op == "-":
                    res = float(curr.get_left().get_val()) - float(curr.get_right().get_val())
                elif op == "+":
                    res = float(curr.get_left().get_val()) + float(curr.get_right().get_val())
                elif op == "/":
                    res = float(curr.get_left().get_val()) / float(curr.get_right().get_val())

                curr.set_val(str(res))
                curr.set_operator("X")
                temp = curr.get_left()
                del temp
                temp = curr.get_right()
                del temp
                curr.set_left(None)
                curr.set_right(None)
                print("delete the child node and set printer to None")
                curr = curr.get_parent()  # move up one node
            elif curr.get_left().get_operator() != "X":
                cur = curr.get_left()  # move to left node
                print("moved left")
                if curr.get_left().get_operator() == "X" and curr.get_right().get_operator() == "X":
                    print("evaluate node 2")
                    op = curr.get_operator()
                    if op == "*":
                        res = float(curr.get_left().get_val()) * float(curr.get_right().get_val())
                    elif op == "-":
                        res = float(curr.get_left().get_val()) - float(curr.get_right().get_val())
                    elif op == "+":
                        res = float(curr.get_left().get_val()) + float(curr.get_right().get_val())
                    elif op == "/":
                        res = float(curr.get_left().get_val()) / float(curr.get_right().get_val())
                    curr.set_val(str(res))
                    curr.set_operator("X")
                    temp = curr.get_left()
                    del temp
                    temp = curr.get_right()
                    del temp
                    curr.set_left(None)
                    curr.set_right(None)
                    print("delete the child node and set printer to None 2")
                    curr = curr.get_parent()  # move up one node
            else:
                op = curr.get_operator()
                if op == "*":
                    res = float(curr.get_left().get_val()) * float(curr.get_right().get_val())
                elif op == "-":
                    res = float(curr.get_left().get_val()) - float(curr.get_right().get_val())
                elif op == "+":
                    res = float(curr.get_left().get_val()) + float(curr.get_right().get_val())
                elif op == "/":
                    res = float(curr.get_left().get_val()) / float(curr.get_right().get_val())
                curr.set_val(str(res))
                curr.set_operator("X")
                temp = curr.get_left()
                del temp
                temp = curr.get_right()
                del temp
                curr.set_left(None)
                curr.set_right(None)
                print("delete the child node and set printer to None 3")
        op = curr.get_operator()
        if op == "*":
            res = float(curr.get_left().get_val()) * float(curr.get_right().get_val())
        elif op == "-":
            res = float(curr.get_left().get_val()) - float(curr.get_right().get_val())
        elif op == "+":
            res = float(curr.get_left().get_val()) + float(curr.get_right().get_val())
        elif op == "/":
            res = float(curr.get_left().get_val()) / float(curr.get_right().get_val())
        del curr
        print("solution", res)
        return res




root = Stack()
t = root.toPostfix("3*7/4-4")
print(t)
Evaluate(t)















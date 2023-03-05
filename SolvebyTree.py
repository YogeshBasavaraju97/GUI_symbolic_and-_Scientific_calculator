import SolvebyStack as Stack
from datetime import datetime
start_time = datetime.now()

class Nodes:
    def __init__(self, val=" ", operator="X"):
        self.left = None     # left leaf node
        self.right = None    #right leaf node
        self.operator = operator  # node to store the operator
        self.parent = None        # node to parent node address
        self.val = val          # node to store operand

    # function to acces the attributes
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
# Function to build and evaluate the binary Tree
def EvaluateTree(infixExp):
    print("the given expression", infixExp)
    basket = Stack.Stack()
    postfix = basket.toPostfix(infixExp)
    print(postfix)
    exp = " "
    for i in postfix.split():
        exp = i + " " + exp
    root = Nodes()
    enter = True
    for i in exp.split():
        if enter:
            # set root node
            curr = root
            curr.set_operator(i)
            print(curr.get_operator())
            print("Node 1")
            enter = False
        else:
            # right children
            if curr.get_right() == None:
                if i == "+" or i == "-" or i == "*" or i == "/":
                    curr.set_right(Nodes(operator = i))
                    print(i)
                    new_n= curr.get_right()
                    new_n.set_parent(curr)
                    curr = new_n
                    print("Node 2")


                else:
                    curr.set_right(Nodes(val=i))
                    print(i)
                    new_n = curr.get_right()
                    new_n.set_parent(curr)
                    print("node 4")

            elif curr.get_left() == None:
                # left childrem
                if i == "+" or i == "-" or i == "*" or i == "/":
                    curr.set_left(Nodes(operator = i))
                    print(i)
                    new_n = curr.get_left()
                    new_n.set_parent(curr)
                    curr = new_n
                    print("node 3")
                else:
                    curr.set_left(Nodes(val=i))
                    print(i)
                    new_n = curr.get_left()
                    new_n.set_parent(curr)
                    print("node 5")
            else:
                while curr.get_left() != None:
                    curr = curr.get_parent()
                if i == "+" or i == "-" or i == "*" or i == "/":
                    curr.set_left(Nodes(operator=i))
                    print(i)
                    new_n = curr.get_left()
                    new_n.set_parent(curr)
                    curr = new_n
                    print("node 7")
                else:
                    curr.set_left(Nodes(val=i))
                    print(i)
                    new_n = curr.get_left()
                    new_n.set_parent(curr)
                    print("node 9")

    curr = root

    print(root)
    try:
        while root.get_left().get_operator() != "X" or root.get_right().get_operator != "X":


            if curr.get_right().get_operator() != "X":
                print("move towards right ")

                curr = curr.get_right()
                if curr.get_left().get_operator() == "X" and curr.get_right().get_operator() == "X":
                    op = curr.get_operator()
                    if op == "*":
                        res = float(curr.get_left().get_val()) * float(curr.get_right().get_val())
                    elif op == "-":
                        res = float(curr.get_left().get_val()) - float(curr.get_right().get_val())
                    elif op == "+":
                        res = float(curr.get_left().get_val()) + float(curr.get_right().get_val())
                    elif op == "/":
                        res = float(curr.get_left().get_val()) / float(curr.get_right().get_val())
                    elif op == "^":
                        res = res = float(curr.get_right().get_val()) ** float(curr.get_left().get_val())
                    curr.set_val(str(res))
                    curr.set_operator("X")
                    curr.set_left(None)
                    curr.set_right(None)
                    print(res)
                    curr = curr.get_parent()
            elif curr.get_left().get_operator() != "X":
                curr = curr.get_left()
                print("moved towards left")


                if curr.get_left().get_operator() == "X" and curr.get_right().get_operator() == "X":
                    op = curr.get_operator()
                    if op == "*":
                        res = float(curr.get_left().get_val()) * float(curr.get_right().get_val())
                    elif op == "-":
                        res = float(curr.get_left().get_val()) - float(curr.get_right().get_val())
                    elif op == "+":
                        res = float(curr.get_left().get_val()) + float(curr.get_right().get_val())
                    elif op == "/":
                        res = float(curr.get_left().get_val()) / float(curr.get_right().get_val())
                    elif op == "^":
                        res = res = float(curr.get_right().get_val()) ** float(curr.get_left().get_val())
                    curr.set_val(str(res))
                    curr.set_operator("X")
                    curr.set_left(None)
                    curr.set_right(None)
                    print(res)
                    curr = curr.get_parent()  # move up one node
                elif curr.get_right().get_operator() != "X":
                    curr = curr.get_right()


                    if curr.get_right().get_operator() != "X":
                        curr = curr.get_right()
                        op = curr.get_operator()


                        if op == "*":
                            res = float(curr.get_left().get_val()) * float(curr.get_right().get_val())
                        elif op == "-":
                            res = float(curr.get_left().get_val()) - float(curr.get_right().get_val())
                        elif op == "+":
                            res = float(curr.get_left().get_val()) + float(curr.get_right().get_val())
                        elif op == "/":
                            res = float(curr.get_left().get_val()) / float(curr.get_right().get_val())
                        elif op == "^":
                            res = res = float(curr.get_right().get_val()) ** float(curr.get_left().get_val())
                        curr.set_val(str(res))
                        curr.set_operator("X")
                        curr.set_left(None)
                        curr.set_right(None)
                        curr.set_val(str(res))
                        curr = curr.get_parent()
                        # print(res)

                        # print(curr.get_operator)
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
                        elif op == "^":
                            res = res = float(curr.get_right().get_val()) ** float(curr.get_left().get_val())
                        curr.set_val(str(res))
                        curr.set_operator("X")
                        curr.set_left(None)
                        curr.set_right(None)
                        curr.set_val(str(res))
                        curr = curr.get_parent()
                        # print(res)



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
                elif op == "^":
                    res =  res = float(curr.get_right().get_val()) ** float(curr.get_left().get_val())
                print(res)
                curr.set_val(str(res))
                curr.set_operator("X")

                curr.set_left(None)
                curr.set_right(None)
                print(curr.get_parent())
                if curr.get_parent() == None:
                    print("No parent")
                    break
                else:
                    curr = curr.get_parent()
        print(f"The value of the {infixExp} is  {res}")
        return  ("%.2f" %res)
    except AttributeError:
        print("Wrong Entry")
        return "TypoError"
endtime = datetime.now()



if __name__=="__main__":
    print(EvaluateTree("9+7(3*4)/2"))













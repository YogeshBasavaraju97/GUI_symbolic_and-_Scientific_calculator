from datetime import datetime
start_time = datetime.now()
# Stack implementation
class Stack:
    # Constructor of stack class
    def __init__(self):
        self.container = []

    # push the number into the stack
    def push(self, val):
        self.container.append(val)

    # remove the top element
    def pop(self):
        if len(self.container) <= 0:
            return "Stack is empty!"
        else:
            return self.container.pop()

    # to check if the stack empty
    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False

        # peek to see the top element
    def peek(self):
         if len(self.container)==0:
            return False
         else:
             return self.container[-1]


    # returns the size of the stack
    def size(self):
        return len(self.container)


    def isdigit(self, ch):
        return ch.isdigit()

    def isOperator(self, ch):
        if ch == "+"or ch == "-" or ch == "*" or ch == "^" or ch == "/":
            return True
        else:
            return False
    # function to check for precedence
    def precedence(self, i):
        priority = {
            "+": 1,
            "-": 1,
            "/": 2,
            "*": 2,
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
    # function to convert infix expression to postfix expression
    def toPostfix(self, exp):

        output = " "
        skip = 0
        try:

            for i in range(len(exp)):
                if skip >= 1:
                    skip -= 1
                    continue
                num = " "
                if   self.isdigit(exp[i]) == True or exp[i] == " ":
                    num += exp[i]
                    for j in range(i+1, len(exp)):

                        if self.isdigit(exp[j]) == True or exp[j] == ".":
                            num += exp[j]
                            skip += 1

                        else:
                            break
                    output += num+ " "
                    print(num, " ~ pushed to output")

                elif exp[i] == "(":
                    if self.isOperator(exp[i-1]) == True:
                       self.push(exp[i])
                       print(exp[i], "~ Found ( push to stack")

                    elif exp[0] == "(":
                         self.push(exp[0])

                    else:
                        self.push("*")
                        self.push(exp[i])
                        print("*", "~ Found ( push to stack")
                        print(exp[i], "~ Found ( push to stack")

                elif exp[i] == ")":
                    while (self.is_empty() != True and self.peek() != "("):
                        operator = str(self.pop())
                        output += operator + " "
                        print(operator, "~ Operator popped from stack")
                    if (self.is_empty() != True and self.peek() != "("):
                        return -1
                    else:
                        x = str(self.pop())
                        print(x, "popping and deleting (")
                else:
                    while (self.is_empty() != True and self.precedence(exp[i])):
                        opt = str(self.pop())
                        output += opt + " "
                        print(opt, "operator popped after checking prority")
                    self.push(exp[i])
                    print(exp[i], "operator pushed to stack")
            while self.is_empty() != True:
                lastelement =str( self.pop())
                output += lastelement + " "
                print(lastelement, "pop at last")

            # print(output)
            return output
        except KeyError:
            # print ("Error")
            return "error"

    # function to evaluate the expression
    def evalPostfix(self, expression):
        stack = Stack()
        self.exp = stack.toPostfix(expression)

        try:
            for ch in self.exp.split():
                    if self.isOperator(ch) == False:
                        self.push(ch)
                        print(ch, "operator pushed to stack")
                    elif ch == " ":
                        continue
                    else:
                        num1 = self.pop()
                        num2 = self.pop()

                        if ch == "+":
                            res = float(num2) + float(num1)
                            self.push(res)
                            print(res)

                        elif ch == "*":
                            res = float(num2) * float(num1)
                            self.push(res)
                            print(res)
                        elif ch == "/":

                            try:

                                    res = float(num2) / float(num1)
                                    self.push(res)
                                    print(res)
                            except  ZeroDivisionError:
                               print(f"Enter number other than zero in instead of {num1} ")
                               return ("Undefined")
                        elif ch == "^":
                            res = float(num2) ** float(num1)
                            self.push(res)
                            print(res)

                        elif ch == "-":
                            res = float(num2) - float(num1)
                            self.push(res)
                            print(res)

            return ("%.2f" %res)
        except (UnboundLocalError, ValueError):

            return "TypoError"

endtime = datetime.now()




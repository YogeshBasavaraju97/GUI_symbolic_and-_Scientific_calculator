import numpy as np
from collections import deque

# this module performs matrix addition, subtraction and multiplication
#
# class Matrics:
#     def __init__(self, rows ,column):
#         rows = rows
#         columns = column
#
#
#     def get_rows(self):
#         return self.rows
#
#     def set_rows(self, rows):
#          self.rows = rows
#
#     def get_columns(self):
#         return self.columns
#
#     # def set_columns(self, columns):
#         self.columns = columns
# def NumberOfmatrices(n):
#     for i in range(n):
#




# Function to perform matrix addition
def matrixAddition(lst):
    convertToarray=np.array(lst)
    sum =0
    for i in range(len(lst)):
        print(convertToarray[i])
        print()
        print()
        sum+=convertToarray[i]
    return(sum)

# function to perform matirx Subtraction
def matrixSubtraction(lst):
    convertToarray=np.array(lst)
    sub =0
    temp = 0
    for i in range(len(lst)):
        print(convertToarray[i])
        print()
        print()
        temp = convertToarray[0]
        sub = temp-convertToarray[i]
    temp = 0

    print(sub)
    return(sub)

# function to verfiy matric multiplication dimensions
def verify(m,n,j,k):
       if (n==j):
           print("Construct matrix")
           return True
       else:
           return False

# function to perform matrix multiplication
def matrixmultiplication(lst):

    for i in range(len(lst)):
        a = lst[0]
        b = lst[1]
    res=np.dot(a,b)
    print(res)
    return res












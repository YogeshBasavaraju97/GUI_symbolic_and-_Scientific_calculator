#Import the required Library
import Calculus as cal
import Matrix as mat


from datetime import datetime
from tkinter import *

import SolvebyTree as tree
import SolvebyStack as stk
from SolvebyTree import *
Window = Tk()
Window.title("Symbolic and Scientific calculator")
Window.minsize(width = 400, height = 400)
Window.maxsize(width = 400, height = 800)

# Creating the widgets
li = Label(Window, text ="Enter the Expressions", bg ="light blue", fg ="Black", width = 20)
# Entry Box 1: To enter the expression
e1 = Entry(Window, width = 20, bd = 8, font = ("Calibri", 20))
# Label to diaplay the answer
solvebyStack = Label(Window, text ="Using stack",  fg ="white", width = 15, font= ("Courier",12))
displayStack = Label(Window, text ="Solution",  fg ="Green", width = 8, font= ("Courier",20))
displayStacktime = Label(Window, text ="time",  fg ="Green", width = 20, font= ("Courier",10))

solvebyTree = Label(Window, text ="Using binaryTree",  fg ="white", width = 15, font= ("Courier",12))
displayTree = Label(Window, text ="Solution",  fg ="Green", width = 8, font= ("Courier",20))
displayTreetime = Label(Window, text ="time",  fg ="Green", width = 20, font= ("Courier",10))

matrices= Label(Window, text ="Matrix Operations", bg ="light blue", fg ="Black", width = 20)



def button_arithmeticExpression():
    exp = e1.get()
    print(exp)
    starts = datetime.now()
    init = stk.Stack()
    res = init.evalPostfix(exp)
    ends = datetime.now()
    time = ends - starts
    displayStack.config( text= res)
    displayStacktime.config(text= time)

    startT = datetime.now()
    sol = tree.EvaluateTree(exp)
    endT = datetime.now()
    timeT = endT - startT
    print(sol)
    displayTree.config(text=sol)
    displayTreetime.config(text=timeT)

    return exp

def button_function():
    displayStack.config(text = "0.0")

    exp = e1.get()
    cal.plot(exp)

def Maddition_button():

    window_matrix = Toplevel(Window)
    window_matrix.title("Matrix Addition")
    window_matrix.geometry("500x500+160+160")
    window_matrix.maxsize(width=400, height=800)
    Mlabel_numberofMatrices = Label(window_matrix, text = "Number of Matrices to be added")
    Mlabel_rxc = Label(window_matrix, text = "Enter number of rows and column")

    Mentry_numberofMatrices = Entry(window_matrix,width = 8 ,bd=1, font = ("Calibri", 15))
    Mentry_rows= Entry(window_matrix, width= 4,bd=1,  font = ("Calibri", 15) )
    Mentry_column = Entry(window_matrix, width=4, bd=1, font=("Calibri", 15))

    Mlabel_numberofMatrices.grid(column=0, row=0)
    Mentry_numberofMatrices.grid(column = 1, row=0)
    Mlabel_rxc.grid(column=0, row= 1)
    Mentry_rows.grid(column = 1, row = 1)
    Mentry_column.grid(column=2,row=1)



    matrices = []
    def constructMatrixAddition():
        Msubmit = Button(window_matrix, text="submit", command=get_dataAddition)
        Msubmit.grid(column=1, row=3)

        for i in range(int(Mentry_numberofMatrices.get())):

                matrixframe = Frame(window_matrix)
                matrixframe.grid(row=3+i, column=0)
                martrixA= Label(matrixframe, text= f"matrix{1+i}")
                martrixA.grid(row=0,column=0)
                text_var = []
                entries = []

                rows,columns = (int(Mentry_rows.get())),int(Mentry_column.get())
                for i in range(rows):
                    text_var.append([])
                    entries.append([])
                    for j in range(int(columns)):
                        text_var[i].append(StringVar())
                        entries[i].append(Entry(matrixframe, textvariable= text_var[i][j],width=3))
                        entries[i][j].grid(row=1+i,column=1+j)

                matrices.append(text_var)

    def get_dataAddition( ):
        getmat = []
        for i in range(len(matrices)):
           getcol=[]
           for r,row in enumerate(matrices[i]):

                getrow=[]
                for c,entry in enumerate(row):

                    text= (entry.get())
                    getrow.append(float(text))

                getcol.append(getrow)


           getmat.append(getcol)
        print(getmat)
        res = mat.matrixAddition(getmat)
        print(res)
        rows, columns = (int(Mentry_rows.get())), int(Mentry_column.get())
        result=[]
        displaymatrix = Frame(window_matrix)
        displaymatrix.grid(row=4, column=1)
        martrixA = Label(displaymatrix, text=f"result")
        martrixA.grid(row=0, column=0)

        for i in range(rows):

            result.append([])
            for j in range(int(columns)):
                print(res[i][j])

                result[i].append(Label(displaymatrix, text=res[i][j], width=3))
                result[i][j].grid(row=1 + i, column=1 + j)

        Msubmit = Button(window_matrix, text="submit", command=get_dataAddition)
        Msubmit.grid(column=1, row=3)

    Mmartixbutton = Button(window_matrix, text="Construct matrix", command=constructMatrixAddition)
    Mmartixbutton.grid(column=0,row=2)

def Msubtraction_button():

    window_matSub = Toplevel(Window)
    window_matSub.title("Matrix Subtraction")
    window_matSub.geometry("500x500+160+160")
    window_matSub.maxsize(width=400, height=800)
    Mlabel_numberofMatrices = Label(window_matSub, text = "Number of Matrices to be added")
    Mlabel_rxc = Label(window_matSub, text = "Enter number of rows and column")

    Mentry_numberofMatrices = Entry(window_matSub,width = 8 ,bd=1, font = ("Calibri", 15))
    Mentry_rows= Entry(window_matSub, width= 4,bd=1,  font = ("Calibri", 15) )
    Mentry_column = Entry(window_matSub, width=4, bd=1, font=("Calibri", 15))

    Mlabel_numberofMatrices.grid(column=0, row=0)
    Mentry_numberofMatrices.grid(column = 1, row=0)
    Mlabel_rxc.grid(column=0, row= 1)
    Mentry_rows.grid(column = 1, row = 1)
    Mentry_column.grid(column=2,row=1)
    matrices = []

    def constructMatrixAddition():
        Msubmit = Button(window_matSub, text="submit", command=get_dataSubtraction)
        Msubmit.grid(column=1, row=3)

        for i in range(int(Mentry_numberofMatrices.get())):

            matrixframe = Frame(window_matSub)
            matrixframe.grid(row=3 + i, column=0)
            martrixA = Label(matrixframe, text=f"matrix{1 + i}")
            martrixA.grid(row=0, column=0)
            text_var = []
            entries = []

            rows, columns = (int(Mentry_rows.get())), int(Mentry_column.get())
            for i in range(rows):
                text_var.append([])
                entries.append([])
                for j in range(int(columns)):
                    text_var[i].append(StringVar())
                    entries[i].append(Entry(matrixframe, textvariable=text_var[i][j], width=3))
                    entries[i][j].grid(row=1 + i, column=1 + j)

            matrices.append(text_var)

    def get_dataSubtraction():
        getmat = []
        for i in range(len(matrices)):
            getcol = []
            for r, row in enumerate(matrices[i]):

                getrow = []
                for c, entry in enumerate(row):
                    text = (entry.get())
                    getrow.append(float(text))

                getcol.append(getrow)

            getmat.append(getcol)
        print(getmat)
        res = mat.matrixSubtraction(getmat)
        print(res)
        rows, columns = (int(Mentry_rows.get())), int(Mentry_column.get())
        result = []
        displaymatrix = Frame(window_matSub)
        displaymatrix.grid(row=4, column=1)
        martrixA = Label(displaymatrix, text=f"result")
        martrixA.grid(row=0, column=0)

        for i in range(rows):

            result.append([])
            for j in range(int(columns)):
                print(res[i][j])

                result[i].append(Label(displaymatrix, text=res[i][j], width=3))
                result[i][j].grid(row=1 + i, column=1 + j)

        Msubmit = Button(window_matSub, text="submit", command=get_dataSubtraction)
        Msubmit.grid(column=1, row=3)

    Mmartixbutton = Button(window_matSub, text="Construct matrix", command=constructMatrixAddition)
    Mmartixbutton.grid(column=0, row=2)

def Mmultiplication():
    window_matmulti= Toplevel(Window)
    window_matmulti.title("Matrix Multiplication")
    window_matmulti.geometry("500x500+160+160")
    window_matmulti.maxsize(width=400, height=800)
    Mlabel_numberofMatrices = Label(window_matmulti, text="Enter the dimensions of the matrices")
    Mlabel_matA = Label(window_matmulti, text="Matrix 1")
    Mlabel_rows = Label(window_matmulti, text="rows")
    Mlabel_columns = Label(window_matmulti, text="columns")

    Mentry_rowsA = Entry(window_matmulti, width=4, bd=1, font=("Calibri", 15))
    Mentry_columnA = Entry(window_matmulti, width=4, bd=1, font=("Calibri", 15))

    Mlabel_matB = Label(window_matmulti, text="Matrix 2")
    Mentry_rowsB = Entry(window_matmulti, width=4, bd=1, font=("Calibri", 15))
    Mentry_columnB = Entry(window_matmulti, width=4, bd=1, font=("Calibri", 15))
    errorLabel = Label(window_matmulti, text="Error:Number of columns in matrix 1 not \n equall to number of rows in matrix 2")

    Mlabel_numberofMatrices.grid(column=0, row=0)

    Mlabel_rows.grid(column=1, row=1)
    Mlabel_columns.grid(column=2, row=1)
    Mlabel_matA.grid(column=0, row=2)

    Mentry_rowsA.grid(column=1, row=2)
    Mentry_columnA.grid(column=2, row=2)

    Mlabel_matB.grid(column=0, row=3)
    Mentry_rowsB.grid(column=1, row=3)
    Mentry_columnB.grid(column=2, row=3)



    matrices = []
    def ConstructMultiplicatioMatrix():



        if mat.verify(Mentry_rowsA.get(), Mentry_columnA.get(),  Mentry_rowsB.get(),Mentry_columnB.get()):

            dimensions = [
            [Mentry_rowsA.get(), Mentry_columnA.get()],
             [Mentry_rowsB.get(),Mentry_columnB.get()]
            ]


            for i in range(2):
                errorLabel.destroy()

                matrixframe = Frame(window_matmulti)
                matrixframe.grid(row=5 + i, column=0)
                martrixA = Label(matrixframe, text=f"matrix{1 + i}")
                martrixA.grid(row=0, column=0)
                text_var = []
                entries = []

                rows, columns = [i for i in dimensions[i]]
                print(rows,columns)
                for i in range(int(rows)):
                    text_var.append([])
                    entries.append([])
                    for j in range(int(columns)):
                        text_var[i].append(StringVar())
                        entries[i].append(Entry(matrixframe, textvariable=text_var[i][j], width=3))
                        entries[i][j].grid(row=6 + i, column= 0 + j)


                matrices.append(text_var)
                print(matrices)
                Msubmit = Button(window_matmulti, text="submit", command=multiplication_data)
                Msubmit.grid(column=1, row=5)

        else:
            errorLabel.grid(column=0, row=7)
            return "error"



    Mmartixbutton = Button(window_matmulti, text="Construct matrix",command=ConstructMultiplicatioMatrix)
    Mmartixbutton.grid(column=0, row=4)

    def multiplication_data():
        getmat = []
        for i in range(len(matrices)):
            getcol = []
            for r, row in enumerate(matrices[i]):

                getrow = []
                for c, entry in enumerate(row):
                    text = (entry.get())
                    getrow.append(float(text))

                getcol.append(getrow)

            getmat.append(getcol)
        print(getmat)
        res = mat.matrixmultiplication(getmat)
        print(res)
        rows, columns = (int(Mentry_rowsA.get())), int(Mentry_columnB.get())
        result = []
        displaymatrix = Frame(window_matmulti)
        displaymatrix.grid(row=6, column=1)
        martrixA = Label(displaymatrix, text=f"result")
        martrixA.grid(row=0, column=0)

        for i in range(rows):

            result.append([])
            for j in range(int(columns)):
                print(res[i][j])

                result[i].append(Label(displaymatrix, text=res[i][j], width=3))
                result[i][j].grid(row=1 + i, column=1 + j)


def clear():
    e1.delete(0, END)


b1 = Button(Window, text = "Solve Expression", command=button_arithmeticExpression)
plot = Button(Window, text = "plot function", command=button_function)
maddition = Button(Window, text = "Addition", command= Maddition_button)
msubtraction = Button(Window, text="Subtraction", command=Msubtraction_button)
mmultiplication = Button(Window, text = "Mulitplication", command=Mmultiplication)
allClear = Button(Window,text = "AC", command=clear)



# showing it on Screen
li.place(x= 90 ,y=10)
e1.place(x=20,y=40)
allClear.place(x= 310, y=50)
b1.place(x=40,y=100)
solvebyStack.place(x =20, y = 140)
displayStack.place(x = 160, y= 140 )
displayStacktime.place(x=280,y= 140 )


displayTree.place(x =160, y = 180 )
solvebyTree.place(x = 5, y= 180)
displayTreetime.place(x=280, y=180)

plot.place(x= 240, y= 100)

matrices.place(x=40, y = 240)
maddition.place(x=10, y= 270)

msubtraction.place(x=100,y=270)

mmultiplication.place(x=210, y = 270)




Window.mainloop()
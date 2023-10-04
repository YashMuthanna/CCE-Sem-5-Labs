import tkinter
from tkinter import *

expression = ""

def onClick(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalPress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        expression=""
def clear():
    global expression
    equation.set("")
    expression = ""
tk = tkinter.Tk()
tk.geometry("200x300")
tk.title("Calculator")

equation = StringVar()
expression_field = Entry(tk, textvariable=equation)
expression_field.grid(row=1,column=1,rowspan=2,columnspan=3)

button1 = Button(tk, text="1",command=lambda: onClick(1))
button1.grid(row=3,column=1)

button2 = Button(tk, text="2",command=lambda: onClick(2))
button2.grid(row=3,column=2)

button3 = Button(tk, text="3",command=lambda: onClick(3))
button3.grid(row=3,column=3)

button4 = Button(tk, text="4",command=lambda: onClick(4))
button4.grid(row=4,column=1)

button5 = Button(tk, text="5",command=lambda: onClick(5))
button5.grid(row=4,column=2)

button6 = Button(tk, text="6",command=lambda: onClick(6))
button6.grid(row=4,column=3)

button7 = Button(tk, text="7",command=lambda: onClick(7))
button7.grid(row=5,column=1)

button8 = Button(tk, text="8",command=lambda: onClick(8))
button8.grid(row=5,column=2)

button9 = Button(tk, text="9",command=lambda: onClick(9))
button9.grid(row=5,column=3)

button0 = Button(tk, text="0",command=lambda: onClick(0))
button0.grid(row=6,column=2)

buttonequal = Button(tk, text="=", command=equalPress)
buttonequal.grid(row=2,column=4)

buttonplus = Button(tk, text="+", command = lambda: onClick('+'))
buttonplus.grid(row=3,column=4)
buttonminus = Button(tk, text="-", command = lambda: onClick('-'))
buttonminus.grid(row=4,column=4)
buttonmulti = Button(tk, text="*", command = lambda: onClick('*'))
buttonmulti.grid(row=5,column=4)
buttondivide = Button(tk, text="/", command = lambda: onClick('/'))
buttondivide.grid(row=6,column=4)
buttonmod = Button(tk, text="%", command = lambda: onClick('%'))
buttonmod.grid(row=7,column=4)

clearButton = Button(tk, text="Clear", command=clear)
clearButton.grid(row=8,column=2)
tk.mainloop()

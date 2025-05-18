import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=tk.Tk()
root.title("Calculator")
root.geometry("300x415")

operator=""
e1=StringVar()
entry = Entry(root, text=e1, font="Italic 10 bold ",bd=5, bg="gray",fg="black" ,insertwidth=3, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, ipadx=77, ipady=21)

def click(num):
    global operator
    operator+=num
    e1.set(operator)

def equal(x):
    global operator
    try:
        result=eval(operator)
        e1.set(result)
    except:
        messagebox.showinfo("error","Invalid Input")

def clear(undo):
    entry.delete(0,END)
    global operator
    operator=""

Button(root,text="1",font="Times 28 bold",command=lambda:click('1')).place(x=17,y=82)
Button(root,text="4",font="Times 28 bold",command=lambda:click('4')).place(x=17,y=162)
Button(root,text="7",font="Times 28 bold",command=lambda:click('7')).place(x=17,y=242)

Button(root,text="2",font="Times 28 bold",command=lambda:click('2')).place(x=85,y=82)
Button(root,text="5",font="Times 28 bold",command=lambda:click('5')).place(x=85,y=162)
Button(root,text="8",font="Times 28 bold",command=lambda:click('8')).place(x=85,y=242)

Button(root,text="3",font="Times 28 bold",command=lambda:click('3')).place(x=153,y=82)
Button(root,text="6",font="Times 28 bold",command=lambda:click('6')).place(x=153,y=162)
Button(root,text="9",font="Times 28 bold",command=lambda:click('9')).place(x=153,y=242)

Button(root,text="c",font="Times 28 bold",bg="gray",command=lambda:clear('c')).place(x=17,y=327)
Button(root,text=".",font="Times 28 bold",command=lambda:click('.')).place(x=85,y=327)
Button(root,text="=",font="Times 28 bold",bg="gray",command=lambda:equal('=')).place(x=153,y=327)

Button(root,text="+",font="Times 28 bold ",bg="gray",command=lambda:click('+')).place(x=225,y=82)
Button(root,text="-",font="Times 28 bold",bg="gray",command=lambda:click('-')).place(x=225,y=162)
Button(root,text="*",font="Times 28 bold",bg="gray",command=lambda:click('*')).place(x=225,y=242)
Button(root,text="/",font="Times 28 bold",bg="gray",command=lambda:click('/')).place(x=225,y=327)

root.mainloop()
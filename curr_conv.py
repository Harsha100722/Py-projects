from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
c=CurrencyConverter()
root=tk.Tk()
root.title("currency converter")
root.geometry("500x500")

Label(root,text="CURRENCY CONVERTER",font="Times 20 bold",bg="white",fg="red").place(x=70,y=0)
Label(root,text="Enter Your Amount:",font="Times 15 bold",bg="white",fg="black").place(x=40,y=75)
Label(root,text="Enter Currency Type:",font="Times 15 bold",bg="white",fg="black").place(x=40,y=125)
Label(root,text="Enter Target Currency:",font="Times 15 bold",bg="white",fg="black").place(x=40,y=175)

global e1
global e2
global e3

e1=Entry(root,width=22)
e1.place(x=222,y=82)

e2=tk.StringVar()
curr1=ttk.Combobox(root,width=20,text=e2)
curr1['values']=('USD', 'EUR', 'INR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'NZD', 'SGD', 'ZAR', 'BRL', 'RUB', 'MXN', 'SEK', 'NOK', 'DKK', 'HKD', 'KRW', 'MYR', 'THB', 'IDR', 'PHP', 'AED', 'SAR', 'EGP', 'TRY', 'PLN', 'CZK', 'HUF')
curr1.place(x=237,y=130)

e3=tk.StringVar()
curr2=ttk.Combobox(root,width=20,text=e3)
curr2['values']=('USD', 'EUR', 'INR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'NZD', 'SGD', 'ZAR', 'BRL', 'RUB', 'MXN', 'SEK', 'NOK', 'DKK', 'HKD', 'KRW', 'MYR', 'THB', 'IDR', 'PHP', 'AED', 'SAR', 'EGP', 'TRY', 'PLN', 'CZK', 'HUF')
curr2.place(x=252,y=180)

result=None

def conv():
    global result
    a1=e1.get()
    a2=e2.get()
    a3=e3.get()

    try:
        float(a1)
    except ValueError:
        messagebox.showinfo("Failure","please enter amount in values")
        return
    if a2 not in curr1['values']:
        messagebox.showinfo("Failure","Enter only valid currency type or Use drop downlist")
        return
    if a3 not in curr2['values']:
        messagebox.showinfo("Failure", f"Enter only valid currency type or Use drop downlist")
        return
    else:
        cur=round(c.convert(a1,a2,a3),2)
        if result==None:
            result=Label(root,text=(f"{a1} {a2} = {cur} {a3}"),font="Times 13 bold",fg="black")
            result.place(x=145,y=278)
        else:
            result.config(text=(f"{a1} {a2} = {cur} {a3}"))
        return

Button(root,text="CONVERT",command=conv,font="Times 15 bold",bg="white",fg="black").place(x=200,y=225)

root.mainloop()

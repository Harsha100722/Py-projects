import tkinter as tk
from tkinter import messagebox, Text
from tkinter.ttk import Combobox
import openpyxl
from openpyxl import Workbook
import pathlib

# Setup
root = tk.Tk()
root.title("User Registration Form")
root.geometry("800x650+300+60")
root.resizable(False, False)
root.configure(bg="#F0F4FD")  # Soft light blue background

# Excel file setup
file = pathlib.Path("user_data.xlsx")
if not file.exists():
    wb = Workbook()
    sheet = wb.active
    sheet.append(["Full Name", "Phone Number", "Age", "Gender", "Address"])
    wb.save("user_data.xlsx")

# Functions
def submit():
    name = name_var.get()
    contact = contact_var.get()
    age = age_var.get()
    gender = gender_box.get()
    address = address_text.get("1.0", tk.END).strip()

    if name and contact and age and gender and address:
        wb = openpyxl.load_workbook("user_data.xlsx")
        sheet = wb.active
        sheet.append([name, contact, age, gender, address])
        wb.save("user_data.xlsx")
        messagebox.showinfo("Success", "User details saved successfully.")
        reset()
    else:
        messagebox.showwarning("Warning", "Please fill all the fields!")

def reset():
    name_var.set("")
    contact_var.set("")
    age_var.set("")
    gender_box.set("Select")
    address_text.delete("1.0", tk.END)

# Title
tk.Label(root, text="REGISTRATION FORM", font=("Helvetica", 28, "bold"), bg="#F0F4FD", fg="#3E3E3E").pack(pady=20)

# Frame for the form
form_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief="groove")
form_frame.place(x=100, y=100, width=600, height=450)

# Labels & Fields
label_style = {"font": ("Arial", 13, "bold"), "bg": "#FFFFFF", "fg": "#333333"}
entry_style = {"font": ("Arial", 12), "width": 30, "bd": 1, "relief": "solid"}

tk.Label(form_frame, text="Full Name:", **label_style).place(x=50, y=30)
name_var = tk.StringVar()
tk.Entry(form_frame, textvariable=name_var, **entry_style).place(x=200, y=30)

tk.Label(form_frame, text="Phone Number:", **label_style).place(x=50, y=80)
contact_var = tk.StringVar()
tk.Entry(form_frame, textvariable=contact_var, **entry_style).place(x=200, y=80)

tk.Label(form_frame, text="Age:", **label_style).place(x=50, y=130)
age_var = tk.StringVar()
tk.Entry(form_frame, textvariable=age_var, **entry_style).place(x=200, y=130)

tk.Label(form_frame, text="Gender:", **label_style).place(x=50, y=180)
gender_box = Combobox(form_frame, values=["Male", "Female", "Other"], font=("Arial", 12), state="readonly", width=28)
gender_box.place(x=200, y=180)
gender_box.set("Select")

tk.Label(form_frame, text="Address:", **label_style).place(x=50, y=230)
address_text = Text(form_frame, font=("Arial", 12), width=29, height=4, bd=1, relief="solid")
address_text.place(x=200, y=230)

# Buttons
btn_style = {"font": ("Arial", 12, "bold"), "bg": "#5680E9", "fg": "white", "bd": 0, "activebackground": "#F1650E", "cursor": "hand2"}

submit_btn = tk.Button(root, text="Submit", command=submit, **btn_style)
submit_btn.place(x=220, y=580, width=100, height=40)

reset_btn = tk.Button(root, text="Reset", command=reset, **btn_style)
reset_btn.place(x=360, y=580, width=100, height=40)

exit_btn = tk.Button(root, text="Exit", command=root.destroy, **btn_style)
exit_btn.place(x=500, y=580, width=100, height=40)

root.mainloop()

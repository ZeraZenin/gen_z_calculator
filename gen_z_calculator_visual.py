import tkinter as tk 
from tkinter import messagebox

#Funtions

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.config(text=f"Result: {num1 + num2}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers babosa")
def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.config(text=f"Result: {num1 - num2}")
    except ValueError:
        messagebox.showerror("Peeesimo", "Please enter valid numbers.")
def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.config(text=f"Result: {num1 * num2}")
    except ValueError:
        messagebox.showerror("BASTAA", "Enter valid numbers, para eso existe el teclado numerico perra loca")
def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero, no te pases de wey...no mames que pena con eso, neta, te mamaste.")
        else:
            result.config(text=f"Result: {num1 / num2}")
    except ValueError:
        messagebox.showerror("ERROOOR", "Todavia que te saco la chamba y ni los pinches numeros puedes meter bien, stupid bitch Yazmin madafaker")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.config(text="Result:")

# Ventana principal

window = tk.Tk()
window.title("Gen Z Calculator by Zera")
window.geometry("450x500")
window.configure(bg="#e692bd")

# Titulo

title = tk.Label(
    window,
    text="Gen Z Calculator",
    font=("Segoe UI", 20, "bold"),
    fg="white",
    bg="#C8529B"
)
title.pack(pady=20)

# Number 1

label1 = tk.Label(
    window,
    text="First Number",
    font=("Segoe UI", 12),
    fg="white",
    bg="#C8529B"
)
label1.pack()

entry1 = tk.Entry(
    window,
    font=("Segoe UI", 12),
    justify="center"
)
entry1.pack(pady=10)

# Number 2

label2 = tk.Label(
    window,
    text="Second Number",
    font=("Segoe UI", 12),
    fg="white",
    bg="#C8529B"
)
label2.pack()

entry2 = tk.Entry(
    window,
    font=("Segoe UI", 12),
    justify="center"
)
entry2.pack(pady=10)

# Buttons

btn_add = tk.Button(
    window,
    text='Add',
    width=15,
    height=2,
    bg="#C8529B",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=add
)
btn_add.pack(pady=5)

btn_subtract = tk.Button(
    window,
    text="Subtract",
    width=15,
    height=2,
    bg="#C8529B",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=subtract
)
btn_subtract.pack(pady=5)

btn_multiply = tk.Button(
    window,
    text="Multiply",
    width=15,
    height=2,
    bg="#C8529B",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=multiply
)
btn_multiply.pack(pady=5)

btn_divide = tk.Button(
    window,
    text="Divide",
    width=15,
    height=2,
    bg="#C8529B",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=divide
)
btn_divide.pack(pady=5)

btn_clear = tk.Button(
    window,
    text="Clear",
    width=15,
    height=2,
    bg="#C8529B",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=clear
)
btn_clear.pack(pady=10)

# Result

result = tk.Label(
    window,
    text="Result:",
    font=("Segoe UI", 18, "bold"),
    fg="#FFFFFF",
    bg="#DF74C4"
)
result.pack(pady=20)

window.mainloop()
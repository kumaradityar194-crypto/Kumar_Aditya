import tkinter as tk
from tkinter import ttk, messagebox

def calculation():
    result = ""
    try:
        a = float(entry_n1.get())
        b = float(entry_n2.get())
        o = op_var.get()

        match o:
            case "+":
                result = a + b
            case "-":
                result = a - b
            case "*":
                result = a * b
            case "/":
                if b != 0:
                    result = a / b
                else:
                    messagebox.showerror("Error", "b can't be zero")
                    return
            case _:
                messagebox.showerror("Invalid", "Enter valid operator.")
                return

    except ValueError:
        messagebox.showerror("Invalid", "Enter valid numbers.")
        return

    label_result.config(text=f"Answer = {result}")

def clear():
    entry_n1.delete(0, tk.END)
    entry_n2.delete(0, tk.END)
    entry_op.set("+")

root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")

tk.Label(root, text="Enter first number:", font=("Arial", 12, "bold")).pack(pady=5)
entry_n1 = tk.Entry(root)
entry_n1.pack()

tk.Label(root, text="Enter second number:", font=("Arial", 12, "bold")).pack(pady=5)
entry_n2 = tk.Entry(root)
entry_n2.pack()

tk.Label(root, text="Choose operator:", font=("Arial", 12, "bold")).pack(pady=5)
op_var = tk.StringVar()
entry_op = ttk.Combobox(root, textvariable=op_var, values=["+", "-", "*", "/"], state="readonly")
entry_op.set("+")
entry_op.pack(pady=5)

label_result = tk.Label(root, text="Answer = ", bg="lightgreen", font=("Arial", 16, "bold"))
label_result.pack(pady=10)

tk.Button(root, text="Calculate", command=calculation, font=("Arial", 14), bg="lightblue").pack(pady=5)
tk.Button(root, text="Clear", command=clear, font=("Arial", 14), bg="lightcoral").pack(pady=5)

root.mainloop()

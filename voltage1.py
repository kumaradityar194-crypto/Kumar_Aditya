import tkinter as tk
from tkinter import messagebox

def calculation():
    try:
        
        vin=float(entry_vin.get())
        R1=float(entry_R1.get())
        R2=float(entry_R2.get())
        
        if R1+R2==0:
            raise ZeroDivisionError
        
        vout=vin*(R1/(R1+R2))
        label_result.config(text=f"output voltage {vout}v")
        
    except ValueError:
        messagebox.showerror("invalid input inter valid data")
        
    except ZeroDivisionError:
        messagebox.showerror("R1+R2 can't be zero")
        
def process():
    for entry in [entry_vin,entry_R1,entry_R2]:
        entry.delete(0,tk.END)
    label_result.config(text=f"output voltage {vout}v")
    
root=tk.Tk()
root.title("voltage calculator:")
root.geometry("350x250")

tk.Label(root,text="input voltage(vin)").pack(pady=5)
entry_vin=tk.Entry(root)
entry_vin.pack()

tk.Label(root,text="enter R1(ohm)").pack(pady=5)
entry_R1=tk.Entry(root)
entry_R1.pack()

tk.Label(root,text="enter the R2(ohm)").pack(pady=5)
entry_R2=tk.Entry(root)
entry_R2.pack()

tk.Button(root,text="calculation:",command=calculation,bg="yellow").pack(pady=5)
tk.Button(root,text="clear:",command=process,bg="blue").pack(pady=5)

label_result = tk.Label(root, text="Output Voltage (Vout):", font=('box', 12, 'bold'))
label_result.pack(pady=10)

root.mainloop()

           
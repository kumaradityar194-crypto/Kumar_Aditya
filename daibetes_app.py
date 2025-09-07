import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

def predict_diabetes():
    result="Person HAS Diabetes"
    result1="Person does NOT have Diabetes"
    try:
        a = float(entry_preg.get())
        b = float(entry_glucose.get())
        c = float(entry_bp.get())
        d = float(entry_skin.get())
        e = float(entry_insulin.get())
        f = float(entry_bmi.get())
        g = float(entry_dpf.get())
        h = int(entry_age.get())

        user_input = pd.DataFrame([[a,b,c,d,e,f,g,h]], 
                                   columns=["Pregnancies","Glucose","BloodPressure","SkinThickness",
                                            "Insulin","BMI","DiabetesPedigreeFunction","Age"])
        
        user_input_scaled = scaler.transform(user_input)
        prediction = model.predict(user_input_scaled)[0]

        if prediction == 1:
            label_res.config(text=f"Prediction = {result}",bg="white",font=("Arial",20,"bold"))
        else:
            label_res.config(text=f"Prediction = {result1}",bg="yellow",font=("Arial",20,"bold"))
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

def clear():
    entry_preg.delete(0,tk.END)
    entry_glucose.delete(0,tk.END)
    entry_bp.delete(0,tk.END)
    entry_skin.delete(0,tk.END)
    entry_insulin.delete(0,tk.END)
    entry_bmi.delete(0,tk.END)
    entry_dpf.delete(0,tk.END)
    entry_age.delete(0,tk.END)
   

root = tk.Tk()
root.title("Diabetes Prediction")
root.geometry("400x500")


tk.Label(root,text="Ent the_Preg:",font=("Arial",12,"bold")).pack(pady=5)
entry_preg=tk.Entry(root)
entry_preg.pack(pady=5)

tk.Label(root,text="Ent the_GLUCOSE",font=("Arial",12,"bold")).pack(pady=5)
entry_glucose=tk.Entry(root)
entry_glucose.pack(pady=5)

tk.Label(root,text="Ent the_BP",font=("Arial",12,"bold")).pack(pady=5)
entry_bp=tk.Entry(root)
entry_bp.pack(pady=5)

tk.Label(root,text="Enter the_SKin ",font=("Arial",12,"bold")).pack(pady=5)
entry_skin=tk.Entry(root)
entry_skin.pack(pady=5)

tk.Label(root,text="Enter the_Insulin",font=("Arial",12,"bold")).pack(pady=5)
entry_insulin=tk.Entry(root)
entry_insulin.pack(pady=5)

tk.Label(root,text="Enter the_BMI",font=("Arial",12,"bold")).pack(pady=5)
entry_bmi=tk.Entry(root)
entry_bmi.pack(pady=5)


tk.Label(root,text="Enter the_DPF",font=("Arial",12,"bold")).pack(pady=5)
entry_dpf=tk.Entry(root)
entry_dpf.pack(pady=5)


tk.Label(root,text="Enter the_Age",font=("Arial",12,"bold")).pack(pady=5)
entry_age=tk.Entry(root)
entry_age.pack(pady=5)

label_res=tk.Label(root,text="Prediction = ",font=("Arial",12,"bold"))
label_res.pack(pady=5)

tk.Button(root,text="Click_For_Prediction",command=predict_diabetes,bg="green",font=("Arial",12,"bold")).pack(pady=5)
tk.Button(root,text="Clear",command=clear,bg="red",font=("Arial",12,"bold")).pack(pady=5)

root.mainloop()


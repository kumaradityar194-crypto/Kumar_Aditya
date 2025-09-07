import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   
import seaborn as sns

dataset = pd.read_csv(r"c:\Users\kumar\Downloads\raw_student_data.csv")
print(dataset.head(50))

missing=dataset.isnull().sum()
print(missing)
print("Shape",dataset.shape)
print("Mean in age:",dataset["Age"].mean())
print("Mode in Gender:",dataset["Gender"].mode()[0])

dataset["Gender"]=dataset["Gender"].fillna(dataset["Gender"].mode()[0])
dataset["Age"]=dataset["Age"].fillna(dataset["Age"].mean())

print(dataset.head(50))
print(dataset.isnull().sum())




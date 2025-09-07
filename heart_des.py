import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   
import seaborn as sns

dataset=pd.read_csv(r"c:\Users\kumar\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\TempState\770F4D1425F14B0D9936CA688E358872\heart_disease_data.csv")
print(dataset.head(1000))
print("shape")
print(dataset.shape)
missing=dataset.isna().sum()
print(missing)

X=dataset["age"]
Y=dataset["target"]

plt.figure(figsize=(10,4))
sns.scatterplot(x=X,y=Y,data=dataset)
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(dataset.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

print("Value_count:",Y.value_counts())

x=dataset.iloc[:,:-1]
y=dataset["target"]

from imblearn.over_sampling import RandomOverSampler
ra=RandomOverSampler(random_state=42)
ra_x,ra_y=ra.fit_resample(x,y)

print(ra_y.value_counts())

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(ra_x,ra_y,test_size=0.25,random_state=42)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_tr=sc.fit_transform(x_train)  
x_tt=sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
la=LogisticRegression(solver="saga",max_iter=5000)
la.fit(x_tr,y_train)

print("Accuracy:",la.score(x_tt,y_test)*100)

print("\n--- Diabetes Prediction for New Input ---")
a=float(input("Enter age:"))
b=float(input("Enter the sex(male=1/female=0):"))
c=float(input("Enter the cp:"))
d=float(input("Enter the  trestbps:"))
e=float(input("Enter the chol:"))
f=float(input("Enter the fbs:"))
g=float(input("Enter the restecg:"))
h=int(input("Enter the thalach:"))
i=float(input("Enter the exang:"))
j=float(input("Enter the oldpeak"))
k=float(input("enter the slope :"))
l=float(input("enter t5he ca:"))
m=float(input("Enter the thal:"))

input=pd.DataFrame([[a,b,c,d,e,f,g,h,i,j,k,l,m]],columns=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"])

indata=sc.transform(input)
prd=la.predict(indata)
print("")

print("Prediction:",prd[0])

if prd[0]==1:
    print("")
    print("person has_Heart_deasies:")
    print("")
    print("Kumar_Aditya_Raj")
    print("")
else:
    print("") 
    print("Person is fit has not heart deasies:")
    print("")
    print("Kumar_Aditya_Raj")
    print("")




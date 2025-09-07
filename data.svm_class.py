import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   
import seaborn as sns

dataset=pd.read_csv(r"c:\Users\kumar\Downloads\customer_svm_400.csv")
print(dataset.head(500))

missing=dataset.isnull().sum()
print(missing)

print("Mean_Age:",dataset["Age"].mean())
print("Mean_Salary:",dataset["Salary"].mean())
print("Mode_of Purchased",dataset["Purchased"].mode()[0])

dataset.select_dtypes(include="int64").columns
from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy="mean")
ar=si.fit_transform(dataset[["Age","Salary"]])
dataset[["Age","Salary"]]=pd.DataFrame(ar,columns=["Age","Salary"])

dataset.select_dtypes(include="int64").columns
from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy="most_frequent")
ar=si.fit_transform(dataset[["Purchased"]])
dataset[["Purchased"]]=pd.DataFrame(ar,columns=["Purchased"])

missing=dataset.isnull().sum()
print(missing)

plt.figure(figsize=(10,4))
sns.scatterplot(x="Age",y="Salary",data=dataset,hue="Purchased")
plt.show()

x=dataset.iloc[:,:-1]
y=dataset["Purchased"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=40)

from sklearn.svm import SVC
sv=SVC(kernel="linear")
sv.fit(x_train,y_train)
print("Accuracy:",sv.score(x_test,y_test)*100)

from mlxtend.plotting import plot_decision_regions
plt.figure(figsize=(10,4))
plot_decision_regions(x.to_numpy(), y.to_numpy().astype(int), clf=sv)  # 👈 ab y ko numpy int banaya
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Decision Boundary (SVM)")
plt.show()
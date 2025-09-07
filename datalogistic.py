import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   
import seaborn as sns
from sklearn.model_selection import train_test_split


dataset = pd.read_csv("work.txt")
print(dataset.head(100))

mising=dataset.isna().sum()
print("")
print(mising)
dataset.drop(columns=["Salary"],inplace=True)
print(dataset.head(30))

x=dataset[["Age"]]
y=dataset["Purchased"]

n=int(input("Enter the age for prediction:"))
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.35,random_state=50)

from sklearn.linear_model import LogisticRegression
la=LogisticRegression()
la.fit(x_train,y_train)

prd=la.predict(pd.DataFrame([[n]],columns=["Age"]))
print("Prediction Accuarcy:",la.score(x_test,y_test)*100)

if prd==1:
    print("Yes this age people purchaded")
else:
    print("NOt perchaded")

sns.scatterplot(x="Age",y="Purchased",data=dataset)
sns.lineplot(x="Age",y=la.predict(x),data=dataset)
plt.show ()


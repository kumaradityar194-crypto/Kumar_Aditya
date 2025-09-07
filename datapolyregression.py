import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   
import seaborn as sns
from sklearn.model_selection import train_test_split


dataset = pd.read_csv(r"c:\Users\kumar\Downloads\polynomial_age_salary_dataset.csv")
print(dataset.head(100))

mising=dataset.isna().sum()
print("")
print(mising)

x=dataset[["Age"]]
y=dataset["Salary"]
n=float(input("Enter the Age:"))

from sklearn.preprocessing import PolynomialFeatures
la=PolynomialFeatures(degree=2)
la.fit(x)
x=la.transform(x)
test = la.transform(pd.DataFrame([[n]], columns=["Age"]))

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=40)

from sklearn.linear_model import LinearRegression
ar=LinearRegression()
ar.fit(x_train,y_train)

prd=ar.predict(test)
prd1=ar.predict(x)

print(f"🎯 Predicted Salary: ₹{round(prd[0], 2)}")
print(f"📊 Accuracy: {round(ar.score(x_test, y_test) * 100, 2)}%")


plt.figure(figsize=(10,4))
sns.scatterplot(data=dataset,x="Age",y="Salary",label="original_data")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.plot(dataset["Age"],prd1,c="green",label="predicted")
plt.legend(["Original_data","Predicted data"])
plt.savefig("predict.png")
plt.show()
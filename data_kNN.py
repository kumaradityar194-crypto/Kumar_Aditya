import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   
import seaborn as sns

dataset=pd.read_csv(r"c:\Users\kumar\Downloads\customer_data.csv")
print(dataset.head(500))

missing=dataset.isnull().sum()
print(missing)
print("Mean of Age:",dataset["Age"].mean())
print("Mean of salary is:",dataset["Salary"].mean())
print("Mode of_PUrched is:",dataset["Purchased"].mode()[0])

dataset.select_dtypes(include= "int64").columns
from sklearn.impute import SimpleImputer
sc=SimpleImputer(strategy="mean")
ar=sc.fit_transform(dataset[["Age","Salary"]])
dataset[["Age","Salary"]]=pd.DataFrame(ar,columns=["Age","Salary"])

dataset.select_dtypes(include= "int64").columns
from sklearn.impute import SimpleImputer
sc=SimpleImputer(strategy="most_frequent")
ar=sc.fit_transform(dataset[["Purchased"]])
dataset[["Purchased"]]=pd.DataFrame(ar,columns=["Purchased"])

sns.scatterplot(x="Age",y="Salary",data=dataset,hue="Purchased")
plt.show()

missing=dataset.isnull().sum()
print(missing)

print("Value count of Purchased",dataset["Purchased"].value_counts())

x=dataset.iloc[:,:-1]
y=dataset["Purchased"]

from imblearn.over_sampling import RandomOverSampler
ra=RandomOverSampler()
ra_x,ra_y=ra.fit_resample(x,y)

print("Value count of Purchased",ra_y.value_counts())

from sklearn.preprocessing import StandardScaler
st=StandardScaler()
st.fit(ra_x)
ra_x=pd.DataFrame(st.transform(ra_x),columns=x.columns)
print(ra_x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(ra_x,ra_y,test_size=0.25,random_state=40)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
print("Accuracy in test data:",knn.score(x_test,y_test)*100)
print("Accuravy in trening data:",knn.score(x_train,y_train)*100)
print(" By using loop:")
for i in range(1,20):
    knn1=KNeighborsClassifier(n_neighbors=i)
    knn1.fit(x_train,y_train)
    print("Accuracy in test data:(",i,")",knn1.score(x_test,y_test)*100)
    print("Accuravy in trening data:(",i,")",knn1.score(x_train,y_train)*100)
    print("")

ag=int(input("Enter the age:"))
sal=float(input("Enter the salary:"))
print("Prediction:",knn.predict(st.transform(pd.DataFrame([[ag,sal]],columns=["Age","Salary"]))))
if knn.predict(st.transform(pd.DataFrame([[ag,sal]],columns=["Age","Salary"])))==[1]:
    print("Purched")
else:
    print("Not perched")
    
    
    
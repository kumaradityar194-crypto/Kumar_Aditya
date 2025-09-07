import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   
import seaborn as sns

dataset=pd.read_csv(r"c:\Users\kumar\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\TempState\920E9E20C536F5F19CD1943957DBF5A2\diabetes.csv")

print(dataset.head(10))

missing=dataset.isnull().sum()
print(missing)
print(dataset.describe())

value=dataset["Outcome"].value_counts()
print(value)

print("Shape:",dataset.shape)

X=dataset["Age"]
Y=dataset["Outcome"]
# x=dataset["Age" if(dataset["Age"]<=90)]

plt.figure(figsize=(10,4))
plt.title("Graph of_Age v/s daibtise positive:")
sns.scatterplot(x="Age",y="Outcome",data=dataset)
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(dataset.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

x=dataset.iloc[:,:-1]
y=dataset["Outcome"]

from imblearn.over_sampling import RandomOverSampler
ra=RandomOverSampler(random_state=42)
ra_x,ra_y=ra.fit_resample(x,y)
print(ra_y.value_counts())

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(ra_x)
ar=sc.transform(ra_x)
print(ar)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(ar,ra_y,test_size=0.25,random_state=42)

from sklearn.svm import SVC
sv=SVC(kernel="linear")
sv.fit(x_train,y_train)

print("Accuracy_test_data:",sv.score(x_test,y_test)*100)
print("Accuracy_traning_data:",sv.score(x_train,y_train)*100)
print("")

print("\n--- Diabetes Prediction for New Input ---")
a=float(input("Enter the Pregnancies value:"))
b=float(input("Enter the Glucose value:"))
c=float(input("Enter the BloodPressure value:"))
d=float(input("Enter the SkinThickness value:"))
e=float(input("Enter the Insulin value:"))
f=float(input("Enter the BMI value:"))
g=float(input("Enter the DiabetesPedigreeFunction:"))
h=int(input("Enter the Age:"))


user_input = pd.DataFrame([[a,b,c,d,e,f,g,h]],
                          columns=["Pregnancies","Glucose","BloodPressure","SkinThickness",
                                   "Insulin","BMI","DiabetesPedigreeFunction","Age"])


user_input_scaled = sc.transform(user_input)

prd = sv.predict(user_input_scaled)
print("Prediction:", prd)

if prd[0] == 1:
    print("Person Has Diabetes")
else:
    print("Person does NOT have Diabetes")



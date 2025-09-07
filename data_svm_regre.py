import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   
import seaborn as sns
from sklearn.model_selection import train_test_split


dataset = pd.read_csv(r"c:\Users\kumar\Downloads\cgpa_vs_package.csv")
print(dataset.head(100))

x=dataset[["CGPA"]]
y=dataset["Package(LPA)"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=40)

from sklearn.svm import SVR
sv=SVR(kernel='linear')
sv.fit(x_train,y_train)
print("Accuracy:",sv.score(x_test,y_test)*100)

plt.figure(figsize=(10,4))
sns.scatterplot(x="CGPA",y="Package(LPA)",data=dataset)
plt.plot(x,sv.predict(x),color="red")
plt.show()


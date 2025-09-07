import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   
import seaborn as sns

dataset=pd.read_csv(r"c:\Users\kumar\Downloads\iris_500_no_species.csv")
print(dataset.head(5))

missing=dataset.isnull().sum()
print(missing)

from sklearn.cluster import KMeans
wcss=[]
for i in range(2,21):
    km=KMeans(n_clusters=i,init="k-means++")
    km.fit(dataset)
    wcss.append(km.inertia_)

plt.figure(figsize=(10,4))
plt.plot([i for i in range(2,21)],wcss)
plt.xticks([i for i in range(2,21)])
plt.grid(True)
plt.xlabel("no. of cluster:")
plt.ylabel("wcss")
plt.show()

km=KMeans(n_clusters=3)
dataset["predict"]=km.fit_predict(dataset)

print(dataset["predict"])

#plt.figure(figsize=(10,4))
plt.title("Predict_graph")
sns.pairplot(data=dataset,hue="predict")
plt.savefig("Predict.jpg")
plt.show()

org=pd.read_csv(r"c:\Users\kumar\Downloads\iris_500.csv")
print(dataset.head(5))
print("Original_data")
print(org.head(5))

#plt.figure(figsize=(10,4))
plt.title("Oroginal_data_graph")
sns.pairplot(data=org,hue="species")
plt.savefig("org.jpg")
plt.show()







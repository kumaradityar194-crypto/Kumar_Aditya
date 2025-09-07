import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv(r"c:\Users\kumar\Downloads\customer_data.csv")
print(dataset.head(10))

from sklearn.impute import SimpleImputer

imp_mean = SimpleImputer(strategy="mean")
dataset[["Age", "Salary"]] = imp_mean.fit_transform(dataset[["Age", "Salary"]])

imp_mode = SimpleImputer(strategy="most_frequent")
dataset[["Purchased"]] = imp_mode.fit_transform(dataset[["Purchased"]])

print("Missing Values:\n", dataset.isnull().sum())

x = dataset.iloc[:, :-1]
y = dataset["Purchased"]

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x = sc.fit_transform(x)

from imblearn.over_sampling import RandomOverSampler
ra = RandomOverSampler()
x_res, y_res = ra.fit_resample(x, y)

# Train-test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_res, y_res, test_size=0.25, random_state=40)


from sklearn.tree import DecisionTreeClassifier, plot_tree
dtc = DecisionTreeClassifier(random_state=42, criterion="gini", max_depth=5)
dtc.fit(x_train, y_train)

print("Decision Tree Classifier Accuracy:", dtc.score(x_test, y_test) * 100)

plt.figure(figsize=(40,20))
plot_tree(dtc, filled=True, feature_names=dataset.columns[:-1], class_names=["0","1"])
plt.show()

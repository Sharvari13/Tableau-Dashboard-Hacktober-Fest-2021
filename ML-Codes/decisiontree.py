# -*- coding: utf-8 -*-
"""decisiontree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16e-lnzoU4mkd6B8NAALvifZ2EmnIvxE8
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

balance_data = pd.read_csv('ML-Codes/Decision_Tree_ Dataset.csv',sep= ',', header= 0)

print ("Dataset Lenght:: "), len(balance_data)
print ("Dataset Shape:: "), balance_data.shape

print ("Dataset:: ")
balance_data.head()

X = balance_data.values[:, 1:5]
Y = balance_data.values[:,0]

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)

y_pred_en = clf_entropy.predict(X_test)
print(y_pred_en)

print ("Accuracy is "), accuracy_score(y_test,y_pred_en)*100
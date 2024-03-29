# -*- coding: utf-8 -*-
"""MHEALTH Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KXCQ8lW7c6VUwtH6LHmf1z40ReW8ZPLf
"""

import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from google.colab import drive
drive.mount('/content/gdrive')

root_path = 'gdrive/My Drive/MHEALTHDATASET'

! ls

! cd gdrive

! ls

!cd gdrive/My\ Drive

!ls

sub_1 = pd.read_excel('gdrive/My Drive/MHEALTHDATASET/Book1.xlsx', index_col=None, header=None)

def fn(path):
  data = pd.read_excel(path, index_col=None, header=None)
  return data

sub_1 = fn('gdrive/My Drive/MHEALTHDATASET/Book1.xlsx')

# print(sub_1)

sub_1_23 = sub_1[23]

sub_1_23 = sub_1_23.replace(0, 1)

# print(sub_1_23)

sub_1 = sub_1.drop(columns=[23])
print(sub_1)

sub_1_new = pd.concat([sub_1, sub_1_23], axis = 1)

print(sub_1_new)

def rename_labels(case, i):
  case_23 = case[23]
  case_23 = case_23.replace(0, i)
  case = case.drop(columns=[23])
  data_2 = pd.concat([case, case_23], axis = 1)
  return data_2

sub_2 = fn('gdrive/My Drive/MHEALTHDATASET/Book2.xlsx')

sub_2_new = rename_labels(sub_2, 2)

print(sub_2_new)

sub_3 = fn('gdrive/My Drive/MHEALTHDATASET/Book3.xlsx')

sub_3_new = rename_labels(sub_3, 3)

print(sub_3_new)

sub_4 = fn('gdrive/My Drive/MHEALTHDATASET/Book4.xlsx')

sub_4_new = rename_labels(sub_4, 4)

sub_5 = fn('gdrive/My Drive/MHEALTHDATASET/Book5.xlsx')

sub_5_new =  rename_labels(sub_5, 5)

sub_6 = fn('gdrive/My Drive/MHEALTHDATASET/Book6.xlsx')

sub_6_new =  rename_labels(sub_6, 6)

sub_7 = fn('gdrive/My Drive/MHEALTHDATASET/Book7.xlsx')

sub_7_new =  rename_labels(sub_7, 7)

sub_8 = fn('gdrive/My Drive/MHEALTHDATASET/Book8.xlsx')

sub_8_new =  rename_labels(sub_8, 8)

sub_9 = fn('gdrive/My Drive/MHEALTHDATASET/Book9.xlsx')

sub_9_new =  rename_labels(sub_9, 9)

sub_10 = fn('gdrive/My Drive/MHEALTHDATASET/Book10.xlsx')

sub_10_new =  rename_labels(sub_10, 10)

print(sub_10_new)

frames = [sub_1_new, sub_2_new, sub_3_new, sub_4_new, sub_5_new, sub_6_new, sub_7_new, sub_8_new, sub_9_new, sub_10_new]
result = pd.concat(frames)
print(result)

result_shuffle = result.sample(frac=1).reset_index(drop=True)

print(result_shuffle)

lines = result_shuffle.plot.line()

len(result_shuffle)

df = pd.DataFrame({'Volunteers':['sub_1', 'sub_2', 'sub_3', 'sub_4', 'sub_5', 'sub_6', 'sub_7', 'sub_8', 'sub_9', 'sub_10'],
                    'val':[len(sub_1), len(sub_2), len(sub_3), len(sub_4), len(sub_5), len(sub_6), len(sub_7), len(sub_8), len(sub_9), len(sub_10)]})
 axis = df.plot.bar(x='Volunteers', y='val', rot=0)

data_3 = result_shuffle.drop(columns=[23])

print(data_3)

normalized_df=(data_3-data_3.min())/(data_3.max()-data_3.min())

print(normalized_df)

X = normalized_df 
y = result_shuffle[23]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

clf = RandomForestClassifier(n_estimators=400, max_depth=23, random_state=42)

clf.fit(X_train, y_train)

pred = clf.predict(X_test)

accuracy_score(y_test, pred)

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, pred)

corr_matrix = result_shuffle.corr()
k = corr_matrix[23].sort_values(ascending=False)
print(k)


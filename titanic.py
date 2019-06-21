# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:55:05 2019

@author: Lenovo
"""


import pandas as pd
 
df = pd.read_csv("training_titanic.csv")
df.info()  


df['Survived'].value_counts(normalize = True)
df.loc[df['Survived'] == 1 ]['Survived'].count()
df.loc[df['Survived'] == 0 ]['Survived'].count()

df["Survived"][(df['Survived'] == 1) & (df ['Sex'] == 'female')].count()

df["Survived"][(df['Survived'] == 1) & (df ['Sex'] == 'male')].count()


df["child"] = df["Age"].map(lambda x: 1 if x < 18 else 0 )

df["child"].value_counts()
df['child']


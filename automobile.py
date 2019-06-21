# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:08:52 2019

@author: Lenovo
"""

import pandas as pd
import numpy as np
df = pd.read_csv("Automobile.csv")
df['price'] = df['price'].replace(0, np.NaN)
df.info()

nd_arr = np.array( df['price'].tolist()) 

df[df['price'].isnull()]
df['price'].min()
df['price'].max()
df['price'].sum() / df['price'].count()
df['price'].std()

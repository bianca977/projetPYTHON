#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:40:36 2021

@author: bianca
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('2year.csv',sep=",",header=66,names=['Attr1','Attr2','Attr3','Attr4','Attr5','Attr6','Attr7','Attr8','Attr9','Attr10','Attr11','Attr12','Attr13','Attr14','Attr15','Attr16','Attr17','Attr18','Attr19','Attr20','Attr21','Attr22','Attr23','Attr24','Attr25','Attr26','Attr27','Attr28','Attr29','Attr30','Attr31','Attr32','Attr33','Attr34','Attr35','Attr36','Attr37','Attr38','Attr39','Attr40','Attr41','Attr42','Attr43','Attr44','Attr45','Attr46','Attr47','Attr48','Attr49','Attr50','Attr51','Attr52','Attr53','Attr54','Attr55','Attr56','Attr57','Attr58','Attr59','Attr60','Attr61','Attr62','Attr63','Attr64','result'])

dataset[:].replace('?', np.nan, inplace=True)
dataset=dataset.dropna()
X = dataset.iloc[:, :64]

newDataset=['Attr13','Attr19','Attr20','Attr23','Attr30','Attr31','Attr39','Attr42','Attr43','Attr44','Attr49','Attr55','Attr56','Attr58','Attr62','result']
dataset=pd.DataFrame(dataset.loc[:,newDataset].values)
dataset.columns = ['Attr13','Attr19','Attr20','Attr23','Attr30','Attr31','Attr39','Attr42','Attr43','Attr44','Attr49','Attr55','Attr56','Attr58','Attr62','result']
newFeatures=['Attr13','Attr19','Attr20','Attr23','Attr30','Attr31','Attr39','Attr42','Attr43','Attr44','Attr49','Attr55','Attr56','Attr58','Attr62']
X= dataset.loc[:, newFeatures].values
X=pd.DataFrame(X)


y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

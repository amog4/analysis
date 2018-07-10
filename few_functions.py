# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 22:30:09 2018

@author: amogh
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def change(x,y):
    change = []
    for i,c in zip(x,y):
        if i != 0:
            change.append(((c-i)/i))
        else:
            change.append((c-i))
    return change



def univariate(d):
    
    for i in d.columns:
    
        
        
        x = d[i].value_counts()
        
        
        sns.color_palette("deep", 10)
        fig = plt.figure(figsize=(8,5))
        pat = sns.barplot(x.index,x.values,color="#34495e")
        plt.xlabel(i)
        plt.ylabel('count of the variable')
        plt.title(i)
        
        rects = pat.patches
        labels =x.values
        for rect, label in zip(rects, labels):
            height = rect.get_height()
            pat.text(rect.get_x() + rect.get_width()/2, height + 0.2, label, ha='center', va='bottom')

    
    return plt.show()



from sklearn.metrics import mutual_info_score
def info(x,y):
    mutual_info_score1 = []
    for i in x:
        mutual_info_score1.append(mutual_info_score(y['growth'],y[i]))
        
    return mutual_info_score1











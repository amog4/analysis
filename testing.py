# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 22:33:18 2018

@author: amogh
"""

import untitled_testing

# --- change --- 
def change_test(x,y):
    
    total = untitled_testing.change(x,y)
    
    return total
    

change_test(x = [0,2],y = [1,3])
    
# ----bar plot ----

new = [1,2,3,3,4,4,4,1,2,2,2,2,2]

data = untitled_testing.pd.DataFrame({'new':new})  


def univariate_analysis(data):
    
    plot =  untitled_testing.univariate(data)
    
    return plot
    
univariate_analysis(data)

#------- score-------

compare = [0,1,1,1,1,0,0,0,0,0,1,1,1]
data = untitled_testing.pd.DataFrame({'new':new,'growth':compare})

names =  [col for col in data.columns if col not in ['growth']]


def info_score(x,y):
    
    score = untitled_testing.info(x,y)
    
    return score

x = info_score(names,data)






















    
    
    
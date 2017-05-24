# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:55:28 2017

@author: rohankoodli
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import os

def goodline(x):
    #return 15 - 2*x
    return 3 + 1.5*x

def badline(x):
    return 15 - x

def horizline(x):
    return 7

x = [1,2,3,4,5,6,7,1.5]
y = [3,5,7,8,9,10,10.5,3.5]
ybar = np.mean(y)
print ybar
devs_y = []
for i in y:
    a = ((i-ybar))
    b = math.pow(a,2)
    devs_y.append(b)

sum_squares = sum(devs_y)

resids = []
for i in range(len(x)):
    exp = horizline(x[i])
    obs = y[i]
    resid = math.pow((obs-exp),2)
    resids.append(resid)
    
sum_sq_resids = sum(resids)

plt.scatter(x,y)
#plt.plot([0,8],[3,15])
#plt.plot([0,8],[15,7])
plt.plot([0,8],[7,7])
plt.xlim([-1,10])
plt.ylim([2,16])

r2 = 1 - (sum_sq_resids/sum_squares)
print r2
print sum_sq_resids
print sum_squares
plt.savefig(os.getcwd()+'/horizline.png')

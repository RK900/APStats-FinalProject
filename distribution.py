# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:00:08 2017

@author: rohankoodli
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
import seaborn; seaborn.set()
import math

n = 40 # sample size
pHat = 0.5
qHat = 1 - pHat
se = math.sqrt((pHat*qHat)/n)
delta = 0.01
error = 1+1e-4
normal = []
compared = []
ind1,ind2 = 0,0

pval = delta

while pval + delta <= error:
    p_o = delta
    val_pval = 0
    
    while p_o + delta <= error:
        sd = math.sqrt((p_o*(1-p_o))/n)
        p0xdeltaz = (p_o + delta - pHat)/se
        p0xz = (p_o - pHat)/se
        prob_p0 = stats.norm.cdf(p0xdeltaz) - stats.norm.cdf(p0xz)
        
        median = p_o + delta/2
        pvaldeltaz = (pval+delta-median)/sd
        pvalz = (pval-median)/sd
        probabilityboth = (stats.norm.cdf(pvaldeltaz)-stats.norm.cdf(pvalz))*prob_p0
        
        val_pval += probabilityboth
        
        p_o+=delta
        
    #compared[ind1] = val_pval
    compared.append(val_pval)
    ind1+=1
    pval+=delta
    
n_n = n/2
se_n = math.sqrt((pHat*qHat)/n_n)
initial = delta

while (initial + delta <= error):
    high = (initial+delta-pHat)/se_n
    low = (initial-pHat)/se_n
    prob = (stats.norm.cdf(high)-stats.norm.cdf(low))
    
    #normal[ind2] = prob
    normal.append(prob)
    ind2+=1
    initial += delta
'''  
for i in range(99):
    print i+1,normal[i],compared[i],
'''

x_axis = np.arange(-20, 100, 0.001)
x = np.arange(-0.05,0.05,0.001)
plt.plot(x_axis, stats.norm.pdf(x_axis,0,2))

print compared

plt.plot(np.array(compared))

prop = .50
std = math.sqrt((.50*.50)/20)
pdf = stats.norm.pdf(prop, std)
plt.plot(np.array(pdf))
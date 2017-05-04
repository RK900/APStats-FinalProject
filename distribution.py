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
qHat = 1 - p
se = math.sqrt((pHat*qHat)/n)

x_axis = np.arange(-7, 7, 0.001)

plt.plot(x_axis, stats.norm.pdf(x_axis,0,2))
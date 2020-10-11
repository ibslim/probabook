# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:51:55 2020

@author: Me
"""
import numpy as np
from numpy.random import poisson
import matplotlib.pyplot as plt

N=10
z = poisson(4, size=N)
print(z)
proba=[(z==i).sum()/N for i in range(N)]

plt.bar(range(0,10), proba[:10], color='black', linewidth=4,label=str(N))
plt.legend()
plt.xlabel('i')
plt.ylabel('Probability')
plt.show()

# z=exponential(1/5,10000)
# print(z.mean())






    
    
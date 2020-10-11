# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:33:57 2020

@author: Me
"""
import numpy as np
from numpy.random import exponential


#Poisson process Example
# question1
lmda=3

dixieme=[]
dixOnze=[]
for j in range(100000):
    suivant=[exponential(1/lmda)]
    for i in range(20):
        inter_arr=exponential(1/lmda)
        if(i==9):
            dixOnze.append(inter_arr)
        suivant.append(suivant[-1]+inter_arr)
        if(i==8):
            dixieme.append(suivant[-1])

print("Le temps moyen jusqu'a la dixieme arrivee obtenu empiriquement:",np.array(dixieme).mean())    
print()
#question2
plusdunjour=[1 if i>1 else 0 for i in dixOnze]
print("La probabilite que le temps entre la dixieme et la onzieme personne depasse un jour obtenu empiriquement:",np.array(plusdunjour).sum()/len(plusdunjour))    

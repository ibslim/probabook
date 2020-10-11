# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 08:48:44 2020

@author: Me
"""
import pykov
import numpy as np
import random

#EXEMPLE METEO
dic = {   ('s1','s1'):0.7,('s1','s2'):0.1,('s1','s3'):0.2,
          ('s2','s1'):0.5,('s2','s2'):0.25,('s2','s3'):0.25,
          ('s3','s1'):0.4,('s3','s2'):0.3,('s3','s3'):0.3}

CM = pykov.Chain(dic)  

#AVEC PYKOV
print(CM.steady())

#AVEC SYSTEME D'EQUATIONS
S=CM.states()
A=np.matrix(np.zeros((len(S)+1,len(S))))
B=np.matrix(np.zeros((len(S)+1,1)))

#Construire A
i=0
for s1 in S:
    j=0
    for s2 in S:
        if(s1==s2):
            A[i,j]=CM.succ(s2)[s1]-1
        else:
            A[i,j]=CM.succ(s2)[s1]
        j+=1
    i+=1
    
#Derniere equation
for j in range(len(S)):
    A[i,j]=1
B[len(S),0]=1

print("SSSSSSSSSSSSSS:",S)
print("AAAAAAAAAAAAAA:",A)
print("BBBBBBBBBBBBBB:",B)
steady=A.I*B
print(steady)
        
    
#EMPIRIQUEMENT
N=10000
cs=random.choice(list(S)) #current state
walk=[cs]
for i in range(N):
    cs=CM.move(cs)
    walk.append(cs)

steady=[walk.count(i)/N for i in S]
print(steady)
    
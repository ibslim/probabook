# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:07:18 2020

@author: Me
"""
import pykov
import numpy as np
import random
import math

#EXEMPLE CTMC 
dic = {   ('s1','s2'):1,
          ('s2','s3'):1,
          ('s3','s1'):0.5,('s3','s2'):0.5}

CM = pykov.Chain(dic)
lamda={"s1":2,"s2":1,"s3":3}
S=CM.states()
G=np.matrix(np.zeros((len(S),len(S))))
#ANALYTIQUEMENT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
i=0
for s1 in S:
    j=0
    for s2 in S:
        if(s1==s2):
            G[i,j]=-lamda[s1]
        else:
            G[i,j]=lamda[s1]*CM.succ(s1)[s2]
        j+=1
    i+=1
print(S)
print(G)

A=np.matrix(np.zeros((len(S)+1,len(S))))
B=np.matrix(np.zeros((len(S)+1,1)))
i=0
for s1 in S:
    j=0
    for s2 in S:
        A[i,j]=G[j,i]
        j+=1
    i+=1
#Derniere equation
for j in range(len(S)):
    A[i,j]=1
B[len(S),0]=1

steady=A.I*B
print("Analytiquement les probabilites a l'etat stationnaire sont:",steady)

#EMPIRIQUEMENT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
N=100000
cs=random.choice(list(S))
print(cs)
temps_Sejour={s:0 for s in S}
for i in range(N):
    ind_cs=list(S).index(cs)
    mintime=math.inf
    for succ in CM.succ(cs):
        ind_succ=list(S).index(succ)
        rate=G[ind_cs,ind_succ]
        if(rate==0):
            time=math.inf
        else:
            time=random.expovariate(rate)
        if (mintime>time):
            mintime=time
            nextS=succ
    temps_Sejour[cs]+=mintime
    cs=nextS
    
temps_Sejour_Moyen={s:temps_Sejour[s]/sum(temps_Sejour.values()) for s in S}
print("Empiriquement les probabilites a l'etat stationnaire sont:",temps_Sejour_Moyen)
    
    
    

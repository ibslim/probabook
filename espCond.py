import numpy as np
import random
from statistics import mean
from random import choices

def tirage(N,elmnts,prob):
    bn=[]
    for i in range(N):
        resultat=[choices(elmnts,prob)[0] for _ in range(3)]
        bn.append((resultat.count(1),resultat.count(2)))
    return bn

    
N=1000000
elmnts=[1,2,3]
prob=[5/30,10/30,15/30]
bn=tirage(N,elmnts,prob)    
noir={0:0,1:0,2:0,3:0} 
for (b,n) in bn:
    if(b==0):
        noir[n]+=1
B=sum([v for k,v in noir.items()])
esperance=sum([k*v for k,v in noir.items()])/B
print(esperance)        
        






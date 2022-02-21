# Code 706.py

from itertools import accumulate
from random import random
import sys;sys.path.append('../chap4')
from CMTD import CMTD

def simulateCM(P,S,steps,cs):
    CM = CMTD(P,S)  
    ls = []
    indices = range(len(CM.S))    
    for i in range(steps):
        ls.append(CM.S[cs])
        prob = list(accumulate(P[cs]))
        cs=transformation_inverse(prob,indices)
    return (CM, "".join(ls))
    
def transformation_inverse(prob,indices):
    u = random()
    for i in range(len(prob)):
        if(u<prob[i]): return indices[i]
    return indices[-1]

def compareToSteadyState(P,S,n,s0):
    res = simulateCM(P,S,n,s0)
    ana_p = res[0].steady_prob();           print("Analytical prob : ", ana_p)
    emp_p = [res[1].count(s)/n for s in S]; print("Empirical prob  : ", emp_p)
    
# Test
n = 10000
print('Ergodic')
P = [[1/3, 1/3, 1/3],
     [3/5, 0.0, 2/5],
     [3/4, 1/8, 1/8]]
S = ['R','N','S']

compareToSteadyState(P,S,n,1)
n = 50
print("CMTD1: ",simulateCM(P,S,n,1)[1])

print('Not ergodic')
P = [[1.0, 0.0, 0.0],
     [3/5, 0.0, 2/5],
     [3/4, 1/8, 1/8]]
print("CMTD2: ",simulateCM(P,S,n,1)[1])

#______________________________   Output  ______________________________________
# Ergodic
# Analytical prob :  [0.50769231 0.20512821 0.28717949]
# Empirical prob  :  [0.5065, 0.2072, 0.2863]
# CMTD1:  NRNRSRSRNSRRRNRSRNRNRSRRSNRRNRSRRSRNSNRSSRRNRSRNRR
# Not ergodic
# CMTD2:  NRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
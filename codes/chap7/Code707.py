# Code 707.py

from itertools import accumulate
from random import random
import math
import sys;sys.path.append('../chap4')
from CMTC import CMTC
 
expo = lambda lamda : (-1/lamda)*math.log(random())

def transformation_inverse(prob,indices):
    U = random()
    for i in range(len(prob)):
        if(U < prob[i]): return indices[i]
    return indices[-1]

def simulateCM(P,lamdas,S,T_max,cs):
    CM = CMTC(P,lamdas,S)  
    indices = range(len(CM.S))
    ls, tc = [], 0
    while tc < T_max:
        tps = expo(lamdas[cs])
        ls.append((CM.S[cs], round(tps,2)))
        tc = tc + tps
        prob = list(accumulate(P[cs]))
        cs = transformation_inverse(prob,indices)
    return (CM , ls)

def compareToSteadyState(res,T):
    ana_p = [ round(p,2) for p in res[0].steady_prob()]
    print("Analytical prob : ", ana_p)
    emp_p = [ round(sum(map(lambda r: r[1], filter(lambda r: r[0]==s, res[1])))/T,2) for s in S]
    print("Empirical prob  : ", emp_p)
    
S = ['R','N','S']    
P = [[0.0, 2/3, 1/3],
     [3/5, 0.0, 2/5],
     [3/4, 1/4, 0.0]]
lamdas = [4, 5, 6]
T_max = 500

res = simulateCM(P,lamdas, S,T_max,1)
compareToSteadyState(res, T_max)
print("CMTC : ",simulateCM(P,lamdas,S,5,1)[1])

#______________________________   Output  ______________________________________
# Analytical prob :  [0.47, 0.32, 0.21]
# Empirical prob  :  [0.46, 0.33, 0.22]
# CMTC : [('N', 0.05), ('R', 0.0), ('S', 0.03),..., ('S', 0.09), ('R', 0.19)]
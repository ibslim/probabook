#Code304.py

import numpy as np
from numpy.random import exponential

# Example3.6
N, lamda, dixieme, dixOnze =10000, 3, [], []
for j in range(N):    
    T_n = exponential(1/lamda)
    for i in range(12):
        S_n = exponential(1/lamda)         
        T_n += S_n 
        if(i==9): dixOnze.append(S_n)
        if(i==8): dixieme.append(T_n)  

# question1
avg = np.array(dixieme).mean()
print("Average time until 10th arrival:",np.round(avg,3),"\n")    

# question2
plusdunjour=[1 if i>1 else 0 for i in dixOnze]
proba = np.array(plusdunjour).sum()/len(plusdunjour)
print("Probability more than a day:",np.round(proba,3))    

#______________________________   Output  ______________________________________
# Average time until 10th arrival: 3.325 
# Probability more than a day: 0.053
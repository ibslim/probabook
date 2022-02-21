#Code212,py

import numpy as np
from sympy.stats import FiniteRV
from sympy.stats import E,variance
import math

XDensity,YDensity = {0:13/24,1:11/24},{0:7/24,1:5/12,2:7/24}
X, Y = FiniteRV('X',XDensity ), FiniteRV('Y',YDensity )

JDensity = {(0,0):1/6,(0,1):1/4,(0,2):1/8,(1,0):1/8,(1,1):1/6,(1,2):1/6}

ZDensity = {(k[0]-E(X))*(k[1]-E(Y)):v for k,v in JDensity.items()}
cov = np.dot(list(ZDensity.keys()),list(ZDensity.values()))

print("E(X)=",E(X),"   E(Y)=",E(Y))
print("V(X)=",variance(X),"   V(Y)=",variance(Y))
print("Cov(X,Y)=",cov)
print("Correlation Coefficient=",cov/(math.sqrt(variance(X))*math.sqrt(variance(Y))))       

#______________________________   Output  ______________________________________  
# E(X)= 0.458333333333333    E(Y)= 1.00000000000000
# V(X)= 0.248263888888889    V(Y)= 0.583333333333333
# Cov(X,Y)= 0.0416666666666667
# Correlation Coefficient= 0.109489780290272
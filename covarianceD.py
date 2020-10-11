import numpy as np
from sympy.stats import FiniteRV
from sympy.stats import E,variance
import math


XDensity={0:13/24,1:11/24}
X=FiniteRV('X', XDensity)

YDensity={0:7/24,1:5/12,2:7/24}
Y=FiniteRV('Y', YDensity)

JDensity={(0,0):1/6,(0,1):1/4,(0,2):1/8,(1,0):1/8,(1,1):1/6,(1,2):1/6}

ZDensity={(i-E(X))*(j-E(Y)):JDensity[(i,j)] for i in XDensity.keys() for j in YDensity.keys()}
cov=np.array([k*v for k,v in ZDensity.items()]).sum()

print("E(X)=",E(X),"   E(Y)=",E(Y))
print("V(X)=",variance(X),"   V(Y)=",variance(Y))
print("Cov(X,Y)=",cov)
print("Coefficient de correlation=",cov/(math.sqrt(variance(X))*math.sqrt(variance(Y))))       

#..........................  OUTPUT  ..........................   
  
# E(X)= 0.458333333333333    E(Y)= 1.00000000000000
# V(X)= 0.248263888888889    V(Y)= 0.583333333333333
# Cov(X,Y)= 0.0416666666666667
# Coefficient de correlation= 0.109489780290272
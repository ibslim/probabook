#Code215.py

import numpy as np
from sympy import *
from sympy.stats import Poisson, Binomial, E
from sympy import Symbol 


p, n, mu = Symbol("p"), Symbol("n"), Symbol("mu")
Y = Binomial("Y",n,1-p);  XgivenY = Poisson("X",mu*Y)
print('E(Y)   = ', E(Y)) 
print('E(X|Y) = ', E(XgivenY)) 
print('E(X)   = ', E(E(XgivenY)))

p0, mu0, n0 = 0.3, 100, 60
print('Symbolic Result :')
print("Expectation of Y        : ", E(Y).subs([(n,n0),(p,p0)]).doit())
print("Expectation of X|Y      : ", E(E(XgivenY)).subs([(n,n0),(p,p0),(mu,mu0)]).doit())

N        = 1000
Ye       = np.random.binomial(n0 ,1-p0, N)
XgivenYe = np.random.poisson(mu0*Ye, (N, len(Ye)))

print('Empirical result :')
print("Expectation of Ye       : ", Ye.mean())
print("Expectation of X|Ye     : ", XgivenYe.mean())

#______________________________   Output  ______________________________________
# E(Y)   =  Sum(Piecewise((_k*p**(-_k + n)*(1 - p)**_k*binomial(n, _k), (_k >= 0) & (_k <= n)), (0, True)), (_k, 0, n))
# E(X|Y) =  mu*Y
# E(X)   =  Sum(Piecewise((_k*mu*p**(-_k + n)*(1 - p)**_k*binomial(n, _k), (_k >= 0) & (_k <= n)), (0, True)), (_k, 0, n))
# Symbolic Result :
# Expectation of Y        :  41.99
# Expectation of X|Y      :  4199.99
# Empirical result :
# Expectation of Ye       :  41.83
# Expectation of X|Ye     :  4183.97
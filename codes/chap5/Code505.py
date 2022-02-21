#Code505.py

from Code501 import Queueing
from math import factorial

#
fsum = lambda rho,s, n : 1 if n == 0 else fsum(rho,s, n-1) + (s**n/factorial(n))*rho**n    

# p0
def getP0(**p):
    rho, s, k = p['rho1'], p['s'], p['k']
    return 1/( fsum(rho,s , s-1) + ((s**s/factorial(s)) * rho**s * (1/(1 - rho))) * (1 - rho**(k-s+1)))
 
# Lq
def getLq(**p):
    rho, s, k, p0 = p['rho1'], p['s'], p['k'], p['p0']
    return (s**s /factorial(s)) * rho**(s+1) * p0 * ((1 + (k-s)*rho**(k-s+1) - (k-s+1)*rho**(k-s))/(1 - rho)**2)

#
laws ={ 'MMSK' : { 'p0' : getP0, 'Lq' : getLq}}

#=========================================================================
# Tests
def getMMSK(mu, lamda, S, K):
    qs = Queueing(
            model = 'MMSK', 
            A ={'D':'Pois' , 'params': { 'lambda': lamda}},
            B ={'D':'Expo' , 'params': { 'mu': mu}},
            C = S,
            K = K,
            laws=laws)
    qs.test()

if __name__ == "__main__": getMMSK(4, 5, 2, 15)  

# ==================MMSK =======================
# p0* :0.23092
# p1* :0.28865
# Lq  :0.79
# L   :2.04
# W   :0.41
# Wq  :0.16
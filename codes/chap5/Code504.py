#Code504.py

from Code501 import Queueing
from math import factorial
# 
fsum01 = lambda rho,s, n : 1 if n == 0 else fsum01(rho,s, n-1) + (s**n/factorial(n))*rho**n    

# p0 : 
def getP0(**p):
    rho,s = p['rho1'], p['s']
    return 1/( fsum01(rho,s , s-1) + (s**s/factorial(s)) * rho**s * (1/(1 - rho)))
    
# Lq
def getLq(**p):
    rho, s, p0 = p['rho1'], p['s'], p['p0']
    return (s**s /factorial(s)) * p0 * rho**(s+1)/(1-rho)**2 
    
#
laws ={ 'MMS' : { 'p0' : getP0,  'Lq' : getLq }}

#=========================================================================
# Tests
def getMMS(mu, lamda, S):
    qs = Queueing(
            model = 'MMS', 
            A ={'D':'Pois' , 'params': { 'lambda': lamda}},
            B ={'D':'Expo' , 'params': { 'mu': mu}},
            C = S, 
            laws=laws)
    qs.test()

if __name__ == "__main__":  getMMS(5,10,4)
# ==================MMS =======================
# p0* :0.13043
# p1* :0.26087
# Lq  :0.17
# L   :2.17
# W   :0.22
# Wq  :0.02
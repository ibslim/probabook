#Code503.py

from Code501 import Queueing

# p0
def getP0(**p):
    rho, k = p['rho1'], p['k']
    return (1 - rho)/(1 - rho**(k+1))
    
# Lq
def getLq(**p):
    rho, k, p0 = p['rho1'], p['k'], p['p0']    #
    return rho/(1-rho) * ( 1 - p0 * (k*rho**k + 1))

#
laws ={ 'MM1K' : { 'p0' : getP0, 'Lq' : getLq, }}

#=========================================================================
# Tests
def getMM1K(mu, lamda, K):
    qs = Queueing(
            model = 'MM1K', 
            A ={'D':'Pois' , 'params': { 'lambda': lamda}},
            B ={'D':'Expo' , 'params': { 'mu': mu}},
            C = 1,
            K =  K,
            laws=laws)
    qs.test()

if __name__ == "__main__": getMM1K(10, 5, 12)   
# ==================MMS =======================
# p0* :0.50006
# p1* :0.25003
# Lq  :0.50
# L   :1.00
# W   :0.20
# Wq  :0.10
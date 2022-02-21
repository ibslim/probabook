# Code705.py

from scipy.stats import expon
import matplotlib.pyplot as plt

def generatePoissonSP(lamda=1, T=1):
    t, N, tim = expon.rvs(scale=1/lamda), 0, []
    while (t<T): 
        tim.append(t)
        N, t = N+1, t+expon.rvs(scale=1/lamda)
    return N,tim

def plotPP(lamda):  
    n,tim = generatePoissonSP(lamda,20)
    return plt.step(tim,range(n))
    
lamdas = [0.25,0.5,1,2]
plt.legend([plotPP(l)[0] for l in lamdas],["lambda="+str(l) for l in lamdas])
plt.xlabel('Time'); plt.ylabel('arrivals number')
plt.show()



import numpy as np
from numpy.random import geometric
import matplotlib.pyplot as plt
import math

k,p,N=1000,1/12,100000
mu,sigma=1/p,math.sqrt((1-p)/(p**2))

def generate():
    z = geometric(p, size=k)
    s=(np.sum(z)-(k*mu))/(sigma*math.sqrt(k))
    return s

result=[generate() for _ in range(N)]

M=max(np.abs(result))
ls=np.linspace(start=-M, stop=+M,num=50 + 1, endpoint=True)
plt.hist(result,bins=ls,density=1,histtype='step',label="Histogramme")
plt.show()



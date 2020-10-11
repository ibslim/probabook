import numpy as np
from numpy.random import geometric
import matplotlib.pyplot as plt
import math
import scipy.stats as sps
from fractions import Fraction

N=100000 # Le nombre de v.a generees
M=3000 # La limite du rang 
prob=[1/70,1/30,1/12,1/2,3/4]

def generate():
    f=[]
    for i in range(len(prob)):
        z= geometric(prob[i], size=N)
        somme=np.array([(z==k).sum() for k in range(M)])/N
        f.append(somme)
    return f

freqs = generate()
esps =[f*range(M) for f in freqs ]

for i in range(len(prob)):
    plt.plot(range(1,199), freqs[i][1:199], color='green', linewidth=1,label="P="+str(Fraction(prob[i]).limit_denominator())+" E="+str(round(np.sum(esps[i]),2)))
    plt.legend()
    plt.xlabel('i')
    plt.ylabel('Frequence')
    plt.show()
    

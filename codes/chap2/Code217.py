#Code217.py

import numpy as np
from numpy.random import geometric
import matplotlib.pyplot as plt
from fractions import Fraction
from scipy.stats import geom

N, M = 100000, 3000 # N: number of generated r.v,  M: the limit 
parameters=[1/70,1/30,1/12,1/2]

# generate: generates N geometric r.v samples for different parameters
# and returns their frequencies
def generate():
    f=[]
    for i in range(len(parameters)):
        z= geometric(parameters[i], size=N)
        somme=np.array([(z==k).sum() for k in range(M)])/N
        f.append(somme)
    return f

freqs = generate()
esps =[f*range(M) for f in freqs ]

for i in range(len(parameters)):
    plt.plot(range(1,199), freqs[i][1:199], color='green', linewidth=1,label="P="
             +str(Fraction(parameters[i]).limit_denominator())+" E="+str(round(np.sum(esps[i]),2)))
    plt.legend(); plt.xlabel('i'); plt.ylabel('Frequence')
    plt.plot(range(1,199), geom.pmf(range(1,199), parameters[i]),linewidth=0.7, color='r')
    plt.show()
    

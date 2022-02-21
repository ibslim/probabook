#Code216.py

import numpy as np
from numpy.random import geometric, binomial

# Large number law for s.r.v
def generate(law, args, k):
    return np.sum([i*(law(*args)==i).sum() for i in range(100)])/k

def plotter(E):
    import matplotlib.pyplot as plt
    
    plt.plot(range(N), E, linewidth=0.5,label=str(N))
    plt.xlabel('N')
    plt.ylabel('Empirical expectation')
    plt.show()

p, N, n = 1/12, 1000, 100

E1 = [generate(geometric, [p,k*10], k*10)       for k in range(N)] ;plotter(E1)
E2 = [generate(binomial , [n,p, k*10 ], k*10) for k in range(N)] ;plotter(E2)

print('Theoretical Expectation - Binomial(np)= ', n*p , ', - Geometric  (1/p)= ', 1/p)

#______________________________   Output  ______________________________________
#Theoretical Expectation - Binomial(np)=  8.333333333333332 , - Geometric  (1/p)=  12.0

import numpy as np
from numpy.random import geometric
import matplotlib.pyplot as plt

#Loi des grand nombre pour une suite de v.a independantes qui suivent la distribution geometrique(Geo(p)) E(X)=1/p. p est la probabilite du succes
p,N=1/12,1000
# repeter l'experience du Coin N sequences et a chaque sequence on note
# le numero de l'iteration ou le premier succes est obtenu.

def generate(k):
    z = geometric(p, k)
    somme =[i*(z==i).sum() for i in range(100)]
    return np.sum(somme)/k
    
E=[generate(k*10) for k in range(N)]

plt.plot(range(N), E, color='black', linewidth=1,label=str(N))
plt.xlabel('N')
plt.ylabel('Esperance empirique')
plt.show()



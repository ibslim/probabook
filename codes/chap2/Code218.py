#Code218.py

import numpy as np
from numpy.random import geometric
import matplotlib.pyplot as plt
import math
from scipy.stats import norm

def generate(p,k,mu,sigma):
    z = geometric(p, size=k)
    s = (np.sum(z)-(k*mu))/(sigma*math.sqrt(k))
    return s

def plotter(result):
    # Central limit theorem using sampling as histogram
    M = max(np.abs(result))
    ls = np.linspace(start=-M, stop=+M,num=50 + 1, endpoint=True)
    plt.hist(result,bins=ls,density=1,histtype='step',label="Histogramme")
    
    # Central limit theorem using theoretic approximation (Normal distribution)
    mu, variance = 0, 1
    sigma = math.sqrt(variance)
    x = np.linspace(mu - 5*sigma, mu + 5*sigma, 100)   
    plt.plot(x, norm.pdf(x, mu, sigma),linewidth=0.7, color='r')
    plt.show()

def TCL(N):
    k, p = 1000, 1/12
    mu, sigma = 1/p, math.sqrt((1-p)/(p**2))
    result = [generate(p,k,mu,sigma) for _ in range(N)]
    plotter(result)

TCL(100000)
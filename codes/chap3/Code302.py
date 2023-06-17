#Code302.py
#Test
import numpy as np    
import random
import matplotlib.pyplot as plt
import sys;sys.path.append('../lib')
from utils import generate_SP,plotSP

# plotter: plots SP realisations and E and V functions
def plotter(rgN, gen_SP, fE, fV):
    n = rgN
    plt.step(n, fE(n)          , color='red')
    plt.step(n, fE(n) + fV(n)/2, color='black')
    plt.step(n, fE(n) - fV(n)/2, color='black')
    plotSP(gen_SP, 5, N)

N, p = 30, 0.5;  rgN = np.arange(0,N)
fYBer = lambda : random.randint(0, 1)  
fnEBer = lambda n: n*p
fnVBer = lambda n: n*p*(1-p)
def generate_SP_Ber(): return generate_SP(fYBer)

plotter(rgN, generate_SP_Ber, fnEBer, fnVBer)



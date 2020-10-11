import random; import matplotlib.pyplot as plt
import numpy as np

def generateSP_BerTrialsSum01():
    spX = [0]   ; X_n = 0
    for i in range(1000):
        Y = 1 if random.randint(0, 1) else 0
        X_n = X_n + Y
        spX.append(X_n)
    return spX

    #
def plotSP_BerTrialsSum01(N=100, nbSP=5) :
    for i in range(nbSP):
        spX = generateSP_BerTrialsSum01();
        plt.plot(spX[:N])
    
#test
N = 100;  rgN = np.arange(0,N)
plt.plot(rgN,rgN * 0.5,'r') #plot m(n)
plt.plot(rgN,rgN * 0.75,'b') #plot m(n) + v(n)
plt.plot(rgN,rgN * 0.25,'b') #plot m(n) + v(n)

plotSP_BerTrialsSum01(N)

import time
time.sleep(100)  
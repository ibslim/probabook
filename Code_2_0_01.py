    
import random; import matplotlib.pyplot as plt
    
def generateSP_BerTrialsSum():
    spX = [0]   #stochastic process X* one sample Path for T[0..999]
    X_n = 0   #random variable X_n 
    for i in range(1000):
        Y = 1 if random.randint(0, 1) else -1 #r.v follow Ber(0.5) on +1/-1
        X_n = X_n + Y  #current r.v X_n+1
        spX.append(X_n)    #newt step in SP X* 
    return spX

    
def plotSP_BerTrialsSum(nbSP=5) :
    for i in range(nbSP):
        spX = generateSP_BerTrialsSum(); #ith sample path
        plt.plot(spX[:100])
    
 #test
plotSP_BerTrialsSum()

import time
time.sleep(100)      
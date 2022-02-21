# utils.py (Continuation)

# generate_SP: generates a stochastic process X* one sample Path for T[0..999]
def generate_SP(rvY, N=1000):
    spX, X_n = [0], 0   #stochastic process, random variable X_n  
    for i in range(N):
        X_n = X_n + rvY()    #current r.v X_n+1
        spX.append(X_n)    #newt step in SP X* 
    return spX

# plotSP: plots the SP's sample paths
def plotSP(generate_SP1, nbSP=5, N=100) :
    for i in range(nbSP):
        spX = generate_SP1(); #ith sample path
        plt.plot(spX[:N])
 

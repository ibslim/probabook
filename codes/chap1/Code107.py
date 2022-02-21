#Code107.py

# function prod of numpy is used to compute the product of the vector's elements
def get_birth(n, L):
    import numpy as np
    
    F = lambda n : 1 - np.prod([(365-i)/365 for i in range(n)])
    E = [F(i) for i in range(n)]   
    for i in L :print("F(",i,"):",F(i))
    return E

# plotter: plots the function associated with the birthday probability example
def plotter(n,E):
    import matplotlib.pyplot as plt
    
    plt.plot(range(n), E, linewidth=1)
    xpos = [23, 30, 41, 57]
    for xc in xpos: plt.axvline(x=xc, color='r', linewidth=1, linestyle='--')

    ypos = [0.5, 0.7, 0.9, 0.99]
    for yc in ypos: plt.hlines(y=yc, xmin=0, xmax=100, linewidth=1, color='r',
                               linestyle='--')

    plt.xlabel('$n$'); 	plt.ylabel(r'$F(n)$'); plt.title('Birth day problem')    
    plt.show()

n = 100
L = [23,30,41,57]
plotter(n,get_birth(n,L))
#______________________________   Output  ______________________________________
# F(23): 0.5072972343239857
# F(30): 0.7063162427192688
# F(41): 0.9031516114817354
# F(57): 0.9901224593411699
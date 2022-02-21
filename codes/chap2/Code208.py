#Code208.py 

from sympy.stats import Binomial
from sympy import S
from sympy.stats import density

# sum2Bin: creates two binomial r.v X,Y with parameters (n,p) and (m,p) as well  
# as their sum Z. W is binomial r.v with parameters (n+m, p)   
def sum2Bin(n, m, p):
    X, Y, W = Binomial('X', n, p), Binomial('Y', m, p), Binomial('X', n+m, p)
    Z = X + Y
    return [{ 'dic': density(X).dict, 'legend': 'X ~ Bin('+str(n)+',1/2)'},
            { 'dic': density(Y).dict, 'legend': 'Y ~ Bin('+str(m)+',1/2)'},
            { 'dic': density(Z).dict, 'legend': 'Z = X+Y'},
            { 'dic': density(W).dict, 'legend': 'W  ~ Bin('+str(n+m)+',1/2)'}]

# plotter: plots X,Y,Z and W 
def plotter(rv_infos):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 8))    
    for i in range(len(rv_infos)):
        plt.subplot(221 + i).set_title(rv_infos[i]['legend'])        
        plt.bar(list(rv_infos[i]['dic'].keys()), rv_infos[i]['dic'].values())  
    plt.show()
#
s2b=sum2Bin(10, 20, S.Half)

#  prints associated distribution of X,Y,Z and W.
for i in range(len(s2b)):
    print("Pmf de " + s2b[i]['legend'][0] + ' : ', s2b[i]['dic'])
plotter(s2b)
#______________________________   Output  _____________________________________
# Pmf de X :  {0: 1/1024, 1: 5/512, 2: 45/1024,..., 10: 1/1024}
# Pmf de Y :  {0: 1/1048576, 1: 5/262144, ..., 20: 1/1048576}
# Pmf de Z :  {0: 1/1073741824, 1: 15/536870912, ..., 30: 1/1073741824}
# Pmf de W :  {0: 1/1073741824, 1: 15/536870912, ..., 30: 1/1073741824}



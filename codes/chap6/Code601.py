# Code601.py

from functools import partial

# number of generated values
N=200

# plot the random number points in a grid
def plotRNG(x,y, title):
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(1, 2, constrained_layout=True, figsize=(10,5))
    axs[0].scatter(x, y)
    axs[1].plot(range(N-1),x)
    fig.suptitle(title, fontsize=16)    
    
# Congruential Generator
# conGen is a Python generator that yields a random number each time next() is called
def congGen(rng_function, seed, m, **params):
    x_n = seed
    while True:
        yield x_n[0]
        s = rng_function(x_n, **params) % m
        x_n = x_n[1:]; x_n.append(s)

# a_1 x_n-1 + a_2 x_n-2 + .... + a_k x_n-k + c
def sumRNG(x, **p):
    s = 0 
    for i in range(p['k']): s += p['a' + str(i)] * x[i]
    return s + p['c']  

# partial congruential generator    
pcg = partial(congGen, lambda x, **p : sumRNG(x,**p)) 

# test RNG
def test(smas):
    for sma in smas:
        seed,m , abc = sma[0], sma[1], sma[2]
        cgi = pcg(seed, m, **abc); rs = [ next(cgi) for _ in range(N)] 
        plotRNG(rs[:-1],rs[1:], sma[3])

# Random number generators
test([ 
      [[1], 2**10, {'k':1,'a0':99, 'c':0}, 'Congruentiel Lineaire'],
      [[1], 2**10, {'k':1,'a0':99, 'c':1}, 'Congruentiel Mixte'],
      [[1,2,3], 2**10, {'k':3,'a0':99, 'a1':2, 'a2':3,  'c':1}, 'Congruentiel Recursif'],

      [[1], 2**10, {'k':1,'a0':95, 'c':0}, 'Congruentiel Lineaire'],
      [[1], 2**10, {'k':1,'a0':95, 'c':1}, 'Congruentiel Mixte'],
      [[1,2,3], 2**10, {'k':3,'a0':95, 'a1':2, 'a2':3,  'c':1}, 'Congruentiel Recursif']
      ])

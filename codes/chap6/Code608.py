#Code609.py

from sympy import diff, simplify
import random
import numpy as np
from sympy.solvers import solve
from Code607 import inverse, plot_fc, x, y

#
def reject(h, g, c):
    nb_iter = 0
    while True:
        v = inverse(g).subs(y,random.random()) 
        u = random.random()
        nb_iter += 1
        if u <= h.subs(x,v)/c: return v,nb_iter

#
def generate_reject(f,g,h,c,N=1000):
    res = [reject(h,g,c)  for _ in range(N)]
    freq = sum([v[1] for v in res])/N    ;print("average iterations number",freq)
    r = np.sort([v[0] for v in res])
    p = [ f.subs(x,u) for u in r]
    return {'x':r, 'y':p}

#symbols
f = (3/4)*x**2*(2-x) 
g = (1/2)*x         
h = f/g               
hp = simplify(diff(h));  print("derivative:",hp)
sols = solve(hp); print("solutions:",sols)
c = h.subs(x,sols[0]); print("C:",c)

plot_fc(**generate_reject(f,g,h,c))

#______________________________   Output  ______________________________________
# derivative: 3.0 - 3.0*x
# solutions: [1.00000000000000]
# C: 1.50000000000000
# average iterations number 1.53
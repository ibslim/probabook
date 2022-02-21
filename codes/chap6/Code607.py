#Code607.py

from sympy import symbols, solveset,S
from sympy.functions import exp
import random
import matplotlib.pyplot as plt
import numpy as np

#
def plot_fc(x,y):
    plt.plot(x,y)
    plt.show()

# to find the inverse of f we solve the equation y =f(x) using  solveset of sympy
def inverse(f):
    expr1 = solveset(f-y,x, domain=S.Reals)
    return(expr1.args[1].args[0])

#
def generate_inverse(f,l,N=1000):
    fc = inverse(f).subs(lamda,l)
    p = np.sort([random.random()  for _ in range(N)]) 
    r = [ fc.subs(y,u) for u in p]
    return {'x':r, 'y':p}

# symbols
x ,y ,lamda  = symbols('x ,y ,lamda')
if __name__== '__main__':
    f = 1-exp(-lamda*x)
    plot_fc(**generate_inverse(f,1))

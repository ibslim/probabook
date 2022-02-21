#Code210,py

from sympy.stats import E,variance, Normal,density
from sympy import Symbol
from sympy.plotting import plot

def processNormalRV(rv_Name, rv_X):
    print('E(',rv_Name,')= ',E(rv_X),'   V(',rv_Name,')= ',variance(rv_X))
    z = Symbol('z')
    plot(density(rv_X)(z), (z, -10, 20))

processNormalRV('X', Normal('X',0,1))
processNormalRV('Y', 3*Normal('X',0,1)+5)

#______________________________   Output  ______________________________________
# E( X )=  0    V( X )=  1
# E( Y )=  5    V( Y )=  9
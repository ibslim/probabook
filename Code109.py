from sympy.stats import E,variance, Normal,density
from sympy import Symbol
from sympy.plotting import plot

def processNormalRV(rv_Name, rv_X):
    print('E(',rv_Name,')= ',E(rv_X),'   V(',rv_Name,')= ',variance(rv_X))
    z = Symbol('z')
    pdf_RV = density(rv_X)
    plot(pdf_RV(z), (z, -10, 20))

    #test
processNormalRV('X', Normal('X',0,1))
processNormalRV('Y', 3*Normal('X',0,1)+5)

#..........................  OUTPUT  ..........................     

# E( X )=  0    V( X )=  1
# E( Y )=  5    V( Y )=  9
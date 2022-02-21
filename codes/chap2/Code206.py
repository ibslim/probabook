#Code206.py

# Symbol is a class that allows creating algebric expressions
# integrate(f,D) function calculates the integral of f over domain D 
from sympy import Symbol, oo, Piecewise, integrate 
from sympy.plotting import plot
from sympy.stats import ContinuousRV, density, E, variance,cdf

# symbols
x,t = Symbol('x'), Symbol('t')  
    
# function f: checks if it is density, its integral has cdf properties
f    = Piecewise((4/x**5, x >= 1), (0, True))   ;print("f(x) = ",f)
val  = integrate(f,(x,-oo,+oo))                 ;print("f is normed ? surface = ", val)
F    = integrate(f,(x,-oo,t))                   ;print("F(t) = ", F)
print("Lim x->-oo F(x)= ", F.subs(t,-oo),"Lim x->+oo F(x)= ", F.subs(t,+oo))

# create RV X with f as PDF
X     = ContinuousRV(symbol=x, density= f)      ;print("PDF_X = ",density(X)(t))
cdf_X = cdf(X)(t)                               ;print("CDF_X = ",cdf_X)

EX2   = integrate(x**2 * f)
print("E(X)=",E(X), ",E(X^2)=",EX2, "=", E(X**2),",Var(X)=", variance(X))

# plot f and F
plot(f, adaptive=False, nb_of_points=400)                 
plot(F, adaptive=False, nb_of_points=400)

#______________________________   Output  ______________________________________
# f(x) =  Piecewise((4/x**5, x >= 1), (0, True))
# F(t) =  Min(1, t)**(-4) - 1/t**4
# Lim x->-oo F(x)=  0 Lim x->+oo F(x)=  1
# f is normed ? surface =  1
# PDF_X =  Piecewise((Piecewise((4/z**5, z >= 1), (0, True)), (z >= -oo) & (z < oo)), (0, True))
# CDF_X =  Min(1, z)**(-4) - 1/z**4
# E(X)= 4/3 ,E(X^2)= Piecewise((0, x <= 1), (2 - 2/x**2, True)) = 2 ,Var(X)= 2/9
from sympy import Symbol, oo, Piecewise, integrate #Interval
from sympy.plotting import plot
from sympy.stats import ContinuousRV, density, E, variance,cdf
from math import sqrt


#symbols
x = Symbol('x'); y = Symbol('y')
    
jointe=3*x    
fx=integrate(jointe,(y,0,x))
fy=integrate(jointe,(x,y,1))
print("marginal de X:",fx)
print("marginal de Y:",fy)

Ex=integrate(x*fx,(x,0,1))
Ey=integrate(y*fy,(y,0,1))
print("E(X)=",Ex,"   E(Y)=",Ey)

Exy=integrate(integrate(x*y*jointe,(y,0,x)),(x,0,1))
print("E(X*Y)=",Exy)
cov=Exy-Ex*Ey
print("Cov(X,y)=",cov)

Ex2=integrate((x**2)*fx,(x,0,1))
Ey2=integrate((y**2)*fy,(y,0,1))
vx=Ex2-Ex**2
vy=Ey2-Ey**2
print("V(X)=",vx)
print("V(Y)=",vy)

cor=cov/(sqrt(vx)*sqrt(vy))
print("Coefficient de correlation:",cor)

#..........................  OUTPUT  ..........................     

# marginal de X: 3*x**2
# marginal de Y: 3/2 - 3*y**2/2
# E(X)= 3/4    E(Y)= 3/8
# E(X*Y)= 3/10
# Cov(X,y)= 3/160
# V(X)= 3/80
# V(Y)= 19/320
# Coefficient de correlation: 0.397359707119513


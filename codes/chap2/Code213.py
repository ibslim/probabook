#Code213.py

from sympy import Symbol, integrate, Interval 
from sympy.stats import density, E, variance as V
from math import sqrt

x = Symbol('x'); y = Symbol('y')
    
fxy = 3*x    
fx = integrate(fxy,(y,0,x)) ; print("marginal of X:",fx)
fy = integrate(fxy,(x,y,1)) ; print("marginal of Y:",fy)

# Direct method
Ex , Ey = integrate(x*fx,(x,0,1)) , integrate(y*fy,(y,0,1))
print("E(X)=",Ex,"   E(Y)=",Ey)

Exy = integrate(integrate(x*y*fxy,(y,0,x)),(x,0,1)) ; print("E(X*Y)=",Exy)
cov = Exy-Ex*Ey ; print("Cov(X,y)=",cov)

Ex2 , Ey2 = integrate((x**2)*fx,(x,0,1)) , integrate((y**2)*fy,(y,0,1)) 
vx , vy = Ex2-Ex**2 , Ey2-Ey**2
print("V(X)=",vx) ; print("V(Y)=",vy)

cor = cov/(sqrt(vx)*sqrt(vy)) ; print("Correlation coefficient:",cor)
    
# ContinuousRV
from sympy.stats import ContinuousRV

X     = ContinuousRV(symbol=x, density= fx, set=Interval(0, 1))   
Y     = ContinuousRV(symbol=y, density= fy, set=Interval(0, 1))  
print("E(X)=",E(X), ",E(X^2)=", E(X**2),",Var(X)=", V(X))
print("E(Y)=",E(Y), ",E(Y^2)=", E(Y**2),",Var(Y)=", V(Y))

cov = Exy-E(X)*E(Y) ; print("Cov(X,y)=",cov)

cor = cov/(sqrt(V(X))*sqrt(V(Y))) ; print("Correlation coefficient:",cor)

#______________________________   Output  ______________________________________  
# marginal of X: 3*x**2
# marginal of Y: 3/2 - 3*y**2/2
# E(X)= 3/4    E(Y)= 3/8
# E(X*Y)= 3/10
# Cov(X,y)= 3/160
# V(X)= 3/80
# V(Y)= 19/320
# Correlation coefficient: 0.397359707119513

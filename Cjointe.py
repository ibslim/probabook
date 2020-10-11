from sympy import Symbol, oo, Piecewise, integrate #Interval
from sympy.plotting import plot
from sympy.stats import ContinuousRV, density, E, variance,cdf
from math import sqrt


class Cjointe(object):   
    def __init__(self,X,Y,pdf):
        self.X=X
        self.Y=Y
        if(!ispdf(pdf)):
            print("Should integrate to 1")
            exit(0)
        self.jointe=pdf
    
    def !ispdf(pdf):
        if(1!=integrate(integrate(x*y*jointe,(y,-oo,+oo),(x,-oo,+oo)))):
            return False
        return True
            
    def marginal(self):
        x,y = Symbol('x'),Symbol('y')
        self.fX=integrate(self.jointe,(x,-oo,+oo))
        self.fY=integrate(self.jointe,(y,-oo,+oo))
        
    def E(self):
        self.Ex=integrate(x*self.fx,(x,-oo,+oo))
        self.Ey=integrate(y*self.fy,(y,-oo,+oo))

    def cov(self):        
        Exy=integrate(integrate(x*y*jointe,(y,0,x)),(x,0,1))
        self.cov=Exy-self.Ex*self.Ey
    
    def V(self):
        Ex2=integrate((x**2)*fx,(x,-oo,+oo))
        Ey2=integrate((y**2)*fy,(y,-oo,+oo))
        self.vx=Ex2-self.Ex**2
        self.vy=Ey2-self.Ey**2

    def corr(self):
        self.corr=self.cov/(sqrt(self.vx)*sqrt(self.vy))


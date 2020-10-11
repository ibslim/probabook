# Symbol est une classe qui permet de creer des objets qui seront manopulees comme des
#symboles dans les expressions algebriques
#La fonction integrate(f,D) permet de calculer l'integral de la fonction f 
#sur le domaine D 

from sympy import Symbol, oo, Piecewise, integrate #Interval
from sympy.plotting import plot
from sympy.stats import ContinuousRV, density, E, variance,cdf


#symbols
x    = Symbol('x')   ;t = Symbol('t')   ;y = Symbol('y')   ;z = Symbol('z')
    
#function f: check if it is density, its integral has cdf properties
f    = Piecewise((3/x**4, x >= 1), (0, True))     
print("f(x) = ",f)

F    = integrate(f,(x,-oo,t))                     
print("F(t) = ", F)
print("Lim x->-oo F(x)= ", F.subs(t,-oo),"Lim x->+oo F(x)= ", F.subs(t,+oo))

#propreties of f
val  = integrate(f,(x,-oo,+oo))          
print("f is normed ? surface = ", val)

#plot f and F
plot(f, adaptive=False, nb_of_points=400)                 
plot(F, adaptive=False, nb_of_points=400)

#plot(f, x>=1, adaptive=False, nb_of_points=400)                 
#plot(F, t>=1, adaptive=False, nb_of_points=400)

#create RV X with f as PDF
Y     = ContinuousRV(symbol=x, density= f) 
pdf_Y = density(Y)(z)                            
print("PDF_X = ",pdf_Y)

cdf_Y = cdf(Y)(z)                                
print("CDF_X = ",cdf_Y)

Ex2   = integrate(x**2 * f)
print("E(X)=",E(Y), ",E(X^2)=",Ex2, "=", E(Y**2),",Var(X)=", variance(Y))
    #-------------------------------------------------------------------------
    # f(x) =  Piecewise((2/x**3, x >= 1), (0, True))
    # F(t) =  Piecewise((1 - 1/t**2, t >= 1), (0, True))
    # Lim x -> -oo F(x) =  0
    # Lim x -> +oo F(x) =  1
    # f is normed ? surface =  1
    # PDF_X =  Piecewise((2/z**3, z >= 1), (0, True))
    # CDF_X =  Min(1, z)**(-2) - 1/z**2
    # E(X)= 2, IE(X**2) = Piecewise((2*log(x), x >= 1),(0, True))=oo, Var(X)=oo
    
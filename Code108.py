# La fonction subs permet de substituer les parametes de la loi par des valeurs
# La  fonction simplify permet de simplifier une expression algebrique.
# Heaviside est la fonction indicatrice de R+
from sympy.stats import Exponential, density, cdf, E, variance, given, P
from sympy import Symbol, simplify, And

l = Symbol("lambda", positive=True)
z = Symbol("z")

X = Exponential("x", l)
pdf_X = density(X)(z)       #lambda*exp(-lambda*z)
cdf_X = cdf(X)(z)           #Piecewise((1 - exp(-lambda*z), z >= 0), (0, True))
E_X = E(X)                  #1/lambda
V_X = variance(X)           #lambda**(-2)
print('RV X. \n pdf:',pdf_X,'\n cdf:',cdf_X,'\n E:',E_X,'\n V:',V_X)

Z = X.subs(l,1/10)
pdf_Z = density(Z)(z)  ;cdf_Z = cdf(Z)(z) ;E_Z = E(Z) ;V_Z = variance(Z)
print('RV Z. \n pdf:', pdf_Z,'\n cdf:', cdf_Z,'\n E:',E_Z,'\n V:',V_Z)

Y = given(X - 3, X > 3)          #a=3
pdf_Y = simplify(density(Y)(z))
P_Y5  = P(Y < 5).subs(l, 1/10) 
P_Y10 = P(Y > 10).subs(l, 1/10) 
P_Y510 = P(And(Y > 5,Y < 10)).subs(l, 1/10) 
print('RV Y. \n pdf:', pdf_Y,'\n P(Y<5):',P_Y5,'\n P(Y<10):',P_Y10,'\n P(Y>5,Y<10):',P_Y510)

#..........................  OUTPUT  ..........................     

# RV X. 
#  pdf: lambda*exp(-lambda*z) 
#  cdf: Piecewise((1 - exp(-lambda*z), z >= 0), (0, True)) 
#  E: 1/lambda 
#  V: lambda**(-2)
# RV Z. 
#  pdf: 0.1*exp(-0.1*z) 
#  cdf: Piecewise((1 - exp(-0.1*z), z >= 0), (0, True)) 
#  E: 10.0000000000000 
#  V: 100.000000000000
# RV Y. 
#  pdf: -lambda*(Heaviside(-z) - 1)*exp(-lambda*z) 
#  P(Y<5): 0.393469340287367 
#  P(Y<10): 0.367879441171442 
#  P(Y>5,Y<10): 0.238651218541191
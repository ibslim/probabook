
from sympy.stats import FiniteRV, density, cdf, E, variance 
from itertools import accumulate
import numpy as np
from utils import getCDF,sortPDF,plot_Pdf_Cdf
   
pmf = {1:0.66,2:0.34}
rv_X = FiniteRV('X',pmf)               #type : sympy.stats.rv.RandomSymbol
rng_X = set(pmf.keys())                  
print('RV Range : ',rng_X)

pdf_X = density(rv_X).dict               
print('pdf_X : ',pdf_X)

cdf_X = cdf(rv_X) 
cdf_X={k:round(float(v),2) for k,v in cdf_X.items()}                       
print('cdf_X : ',cdf_X)

spdf_X, cdf_X = getCDF(pdf_X) 
cdf_X={k:round(float(v),2) for k,v in cdf_X.items()}                                 
print('Cdf of X      : ',cdf_X)

E_X, V_X = E(rv_X), variance(rv_X)       
print('E(X) : ', round(E_X,2), '  , V_X : ', round(V_X,2))
    
plot_Pdf_Cdf(spdf_X, cdf_X)

#..........................  OUTPUT  ..........................     

# RV Range :  {1, 2}
# pdf_X :  {1: 0.66, 2: 0.34}
# cdf_X :  {1: 0.66, 2: 1.0}
# Cdf of X      :  {1: 0.66, 2: 1.0}
# E(X) :  1.34   , V_X :  0.22
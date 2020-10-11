from sympy.stats import FiniteRV, density, cdf
from itertools import accumulate
from utils import getCDF,sortPDF,plot_Pdf_Cdf

#Test Using builtin functions FiniteRV, cdf
   
pmf = {0:.1,1:0.2,2:.3,3:.4}
rv_X = FiniteRV('X',pmf)               #type : sympy.stats.rv.RandomSymbol
rng_X = set(pmf.keys())                  
print('RV Range : ',rng_X)

pdf_X = density(rv_X).dict  
pdf_X={k:round(float(v),2) for k,v in pdf_X.items()}                                                        
print('pdf_X    : ',pdf_X)

cdf_X = cdf(rv_X) 
cdf_X={k:round(float(v),2) for k,v in cdf_X.items()}                                                                    
print('cdf_X    : ',cdf_X )

spdf_X, cdf_X = getCDF(pdf_X) 
cdf_X={k:round(float(v),2) for k,v in cdf_X.items()}                                                        
print('Cdf of X : ',cdf_X)
        
plot_Pdf_Cdf(spdf_X, cdf_X)

#..........................  OUTPUT  ..........................     

# RV Range :  {0, 1, 2, 3}
# pdf_X    :  {0: 0.1, 1: 0.2, 2: 0.3, 3: 0.4}
# cdf_X    :  {0: 0.1, 1: 0.3, 2: 0.6, 3: 1.0}
# Cdf of X :  {0: 0.1, 1: 0.3, 2: 0.6, 3: 1.0}    
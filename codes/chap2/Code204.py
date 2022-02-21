#Code204,py

from sympy.stats import FiniteRV, density, cdf, E, variance 
import sys;sys.path.append('../lib')
from utils import get_CDF,plot_Pdf_Cdf, get_round_dic,plt
   
pmf = {1:0.66,2:0.34}

rv_X = FiniteRV('X',pmf)            ;print('RV Range : ',set(pmf.keys()) )
pdf_X = density(rv_X).dict          ;print('pdf_X    : ',pdf_X)
cdf_X = get_round_dic(cdf(rv_X))    ;print('cdf_X    : ',cdf_X)
spdf_X, cdf_X = get_CDF(pdf_X)      ;print('Cdf of X : ',get_round_dic(cdf_X))
E_X, V_X = E(rv_X), variance(rv_X)  ;print('E(X)     : ',round(E_X,2), ', V_X : ', round(V_X,2))
    
plot_Pdf_Cdf(spdf_X, cdf_X, E_X)

#______________________________   Output  ______________________________________
# RV Range :  {1, 2}
# pdf_X    :  {1: 0.66, 2: 0.34}
# cdf_X    :  {1: 0.66, 2: 1.0}
# Cdf of X :  {1: 0.66, 2: 1.0}
# E(X)     :  1.34 , V_X :  0.22
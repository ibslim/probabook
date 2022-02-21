#Code203,py

from sympy.stats import FiniteRV, density, cdf
import sys;sys.path.append('../lib')
from utils import get_CDF,plot_Pdf_Cdf, get_round_dic

# distribution of r.v X
pmf = {0:.1,1:0.2,2:.3,3:.4}

rv_X = FiniteRV('X',pmf)                    ;print('RV Range : ',set(pmf.keys()))
pdf_X = get_round_dic(density(rv_X).dict)   ;print('pdf_X    : ',pdf_X)
cdf_X = get_round_dic(cdf(rv_X))            ;print('cdf_X    : ',cdf_X )
spdf_X, cdf_X = get_CDF(pdf_X)              ;print('Cdf of X : ',get_round_dic(cdf_X))
        
plot_Pdf_Cdf(spdf_X, cdf_X)

#______________________________   Output  ______________________________________
# RV Range :  {0, 1, 2, 3}
# pdf_X    :  {0: 0.1, 1: 0.2, 2: 0.3, 3: 0.4}
# cdf_X    :  {0: 0.1, 1: 0.3, 2: 0.6, 3: 1.0}
# Cdf of X :  {0: 0.1, 1: 0.3, 2: 0.6, 3: 1.0}    
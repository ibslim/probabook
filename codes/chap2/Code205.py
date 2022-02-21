#Code205,py

from sympy.stats import FiniteRV, density, cdf, E, variance
from sympy.functions import Abs
import sys;sys.path.append('../lib')
from utils import get_CDF,plot_Pdf_Cdf, get_round_dic

# RV X
pmf = {-1:0.2,0:0.2,1:0.2,2:0.2,3:0.2}
rv_X = FiniteRV('X',pmf)               
    
# RV Y=2|X|
rv_Y = 2 * Abs(rv_X)
pdf_Y = get_round_dic(density(rv_Y).dict)  ;print('pdf_Y   : ',pdf_Y)
rng_Y = set(pdf_Y.keys())                  ;print('Range_Y : ',rng_Y)
cdf_Y =get_round_dic(cdf(rv_Y))            ;print('cdf_Y   : ',cdf_Y )
spdf_Y, cdf_Y = get_CDF(pdf_Y)             ;print('cdf_Y   : ',get_round_dic(cdf_Y))
E_Y = round(E(rv_Y),2)
V_Y =  round(variance(rv_Y),2)             ;print('E(Y)    : ', E_Y, ', V(Y):', V_Y)    
    
plot_Pdf_Cdf(spdf_Y, cdf_Y, E_Y)

#______________________________   Output  ______________________________________
# pdf_Y   :  {2: 0.4, 0: 0.2, 4: 0.2, 6: 0.2}
# Range_Y :  {0, 2, 4, 6}
# cdf_Y   :  {0: 0.2, 2: 0.6, 4: 0.8, 6: 1.0}
# cdf_Y   :  {0: 0.2, 2: 0.6, 4: 0.8, 6: 1.0}
# E(Y)    :  2.80 , V(Y): 4.16
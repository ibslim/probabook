from sympy.stats import FiniteRV, density, cdf, E, variance
from sympy.functions import Abs
from itertools import accumulate
from utils import getCDF,sortPDF,plot_Pdf_Cdf

#RV X
pmf = {-1:0.2,0:0.2,1:0.2,2:0.2,3:0.2}
rv_X = FiniteRV('X',pmf)               #type : sympy.stats.rv.RandomSymbol
    
#RV Y
rv_Y = 2 * Abs(rv_X)
pdf_Y = density(rv_Y).dict               
pdf_Y={k:round(float(v),2) for k,v in pdf_Y.items()}                       
print('pdf_Y   : ',pdf_Y)


rng_Y = set(pdf_Y.keys())                
print('Range_Y : ',rng_Y)


cdf_Y = cdf(rv_Y)  
cdf_Y={k:round(float(v),2) for k,v in cdf_Y.items()}                                             
print('cdf_Y   : ',cdf_Y )

spdf_Y, cdf_Y = getCDF(pdf_Y)  
cdf_Y={k:round(float(v),2) for k,v in cdf_Y.items()}                                                       
print('cdf_Y   : ',cdf_Y)


E_Y, V_Y = round(E(rv_Y),2), round(variance(rv_Y),2)       
print('E(Y)    : ', E_Y, ', V(Y):', V_Y)    
    
plot_Pdf_Cdf(spdf_Y, cdf_Y)

#..........................  OUTPUT  ..........................     

# pdf_Y   :  {2: 0.4, 0: 0.2, 4: 0.2, 6: 0.2}
# Range_Y :  {0, 2, 4, 6}
# cdf_Y   :  {0: 0.2, 2: 0.6, 4: 0.8, 6: 1.0}
# cdf_Y   :  {0: 0.2, 2: 0.6, 4: 0.8, 6: 1.0}
# E(Y)    :  2.80 , V(Y): 4.16
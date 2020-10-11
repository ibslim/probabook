from itertools import accumulate
from utils import getCDF,sortPDF,plot_Pdf_Cdf

rv_X  = dict({'o1':1,'o2':2,'o3':3 })        
print('RV map        : ',rv_X)

rng_X = set(rv_X.values())                   
print('RV Range      : ',rng_X)

pdf_X = dict({1:0.5,2:0.33,3:0.17 })   
pdf_X={k:round(float(v),2) for k,v in pdf_X.items()}                                                                          
print('P_X RVProbLaw : ',pdf_X)

spdf_X, cdf_X = getCDF(pdf_X)    
cdf_X={k:round(float(v),2) for k,v in cdf_X.items()}                                                                                
print('Cdf of X      : ',cdf_X)
        
plot_Pdf_Cdf(spdf_X, cdf_X)

#..........................  OUTPUT  ..........................     

# RV map        :  {'o1': 1, 'o2': 2, 'o3': 3}
# RV Range      :  {1, 2, 3}
# P_X RVProbLaw :  {1: 0.5, 2: 0.33, 3: 0.17}
# Cdf of X      :  {1: 0.5, 2: 0.83, 3: 1.0}
    
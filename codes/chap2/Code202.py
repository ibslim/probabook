#Code202.py

import sys;sys.path.append('../lib')
from utils import get_CDF, plot_Pdf_Cdf, get_round_dic 

#dic1: defines a r.v on Omega={o1.o2.o3}, dic2: defines the associated probabilities
dic1,dic2={'o1':1,'o2':2,'o3':3 }, {1:0.5,2:0.33,3:0.17 }

rv_X  = dict(dic1)                      ;print('RV map        : ',rv_X)
rng_X = set(rv_X.values())              ;print('RV Range      : ',rng_X)
pdf_X = get_round_dic(dict(dic2))       ;print('P_X RVProbLaw : ',pdf_X)
pdf_X, cdf_X = get_CDF(pdf_X)           ;print('Cdf of X      : ',get_round_dic(cdf_X))
      
plot_Pdf_Cdf(pdf_X, cdf_X)

#______________________________   Output  ______________________________________
# RV map        :  {'o1': 1, 'o2': 2, 'o3': 3}
# RV Range      :  {1, 2, 3}
# P_X RVProbLaw :  {1: 0.5, 2: 0.33, 3: 0.17}
# Cdf of X      :  {1: 0.5, 2: 0.83, 3: 1.0}
    
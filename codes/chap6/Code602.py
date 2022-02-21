#Code602.py

from scipy import stats
from scipy.stats import ksone

# stats.kstest: returns the calculeted KS statistic
# ksone.ppf: returns the KS table value correspondent to alpha and n
def testKS(data,alpha,F,p):
    n = len(data)
    DKS = stats.kstest(data, lambda x: F(x,**p))[0];  print('DKS    :', DKS)
    DA = ksone.ppf(1-alpha/2, n);                     print('Dalpha :', DA)
    return(DKS<DA)

# Test, loc is the sequence average and scale is its standard deviation
x = [4,5,5,1,1,3,2,2,4,10,7,5,5,4,8,9,7,6]
alpha = 0.05
print('H0     : ',testKS(x, alpha, stats.norm.cdf, {'loc':4.88,'scale':2.60}))

#______________________________   Output  ______________________________________
# DKS    : 0.14826048100509914
# Dalpha : 0.30936031179258944
# H0     : True


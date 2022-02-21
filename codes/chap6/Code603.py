#Code 603.py

from scipy.stats import chisquare
from scipy.stats import chi2

# chisquare: returns the calculeted Chi2 statistic
# chi2.ppf: returns the chi2 table value correspondent to alpha and df
def testChi2(data_obs, data_expected=None, alpha=0.05):
    df = len(data_obs) - 1
    Dc2 = chisquare(data_obs, data_expected) if data_expected else chisquare(data_obs)
    print('DChi2  :', Dc2[0])
    DA = chi2.ppf(1-alpha, df);                     print('Dalpha :', DA)
    return(Dc2[0]<DA)

# Test, loc is the sequence average and scale is its standard deviation
x = [8,12,13,14,9,6,8,7,14,9]
alpha = 0.05
print('H0     : ',testChi2(x))

#______________________________   Output  ______________________________________
# DChi2  : 8.0
# Dalpha : 16.918977604620448
# H0     :  True


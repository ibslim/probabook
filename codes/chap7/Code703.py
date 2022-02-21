#Code703.py

from symbulate import BoxModel, RV, Normal, exp

# 5 Bernoulli trials and successes number
P = BoxModel([0,1],size=5); X = RV(P,sum)
tab = (X>3).sim(10000).tabulate()
print("Tabulate without normalization: ",tab)
tab = (X>3).sim(10000).tabulate(normalize=True)
print("Tabulate with normalization: ",tab)
X.sim(10000).plot()

# function of rv
X = RV(Normal(mean=0, var=1)); Y = exp(X) # could be replaces with: X.apply(exp)
Y.sim(10000).plot()

#______________________________   Output  ______________________________________
# Tabulate without normalization:  {True: 1826, False: 8174}
# Tabulate awith normalization:  {True: 0.1842, False: 0.8158}



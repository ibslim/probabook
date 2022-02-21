#Code704.py

from symbulate import RV, Normal, Exponential

X = RV(Exponential(rate=1/4))
simX = X.sim(10000)
print("Expected value:", simX.mean())
print("Variance:", simX.var())
print("Standard deviation:", simX.sd())

#Normalization
X = RV(Normal(mean=3,sd=2))
simX = X.sim(10000)
print("Before normalization. mean and sd:", round(simX.mean(),2), round(simX.sd(),2))
simX.plot()

z = simX.standardize()
print("After normalization. mean and sd:", round(z.mean(),2), round(z.sd(),2))
z.plot()

#______________________________   Output  ______________________________________
# Expected value: 3.9628993353781383
# Variance: 15.587130335771537
# Standard deviation: 3.9480539935228265
# Before normalization. mean and sd: 3.03 2.0
# After normalization. mean and sd: -0.0 1.0
import random
import math
from scipy.stats import expon,kstest

def inv(lamda):
    u=random.random()
    return (-1/lamda)*math.log(u)

N=1000
lamda=5
generated=[]
for i in range(N):
    gen=inv(lamda)
    generated.append(gen)
    
print(kstest(generated,expon.cdf,(lamda)))
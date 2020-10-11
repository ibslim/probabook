import random
from itertools import accumulate
from functools import reduce
import operator
from operator import itemgetter
import numpy as np

prob=[0.2,0.15,0.25,0.4]
indices, prob = zip(*sorted(enumerate(prob), key=itemgetter(1),reverse=True))
prob=list(accumulate(prob))

def scroll(u,prob,indices):
    for i in range(len(prob)):
        if(u<prob[i]):
            return indices[i]
    return indices[-1]

N=100000
freq={1:0,2:0,3:0,4:0}
for i in range(N):
    u=random.random()
    gen=scroll(u,prob,indices)
    freq[gen+1]+=1

freq={k:v/N for k,v in freq.items()}
print(freq)

#sumProb=list(map(lambda x:reduce(operator.add, x),[prob[:i] for i in range(1,len(prob)+1)]))
#print(sumProb)


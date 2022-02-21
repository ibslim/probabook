#Code 605.py

import random
from itertools import accumulate
from operator import itemgetter
#
def transformation_inverse(prob,indices):
    u = random.random()
    for i in range(len(prob)):
        if(u<prob[i]): return indices[i]
    return indices[-1]

# returns the frequencies in N generated rv
def generate(prob, N=100000):
    indices, prob = zip(*sorted(enumerate(prob), key=itemgetter(1),reverse=True))
    prob = list(accumulate(prob))
    freq = {k:0  for k in range(len(prob))}    
    for _ in range(N):
        gen = transformation_inverse(prob,indices)
        freq[gen] += 1
    return {k:v/N for k,v in freq.items()}

# test
prob = [0.2,0.15,0.25,0.4]
print(generate(prob))

#______________________________   Output  ______________________________________
#{1: 0.19671, 2: 0.1498, 3: 0.25018, 4: 0.40331}


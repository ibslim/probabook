#Code606.py

import random

# acceptance-rejection method
def acceptationRejet(pj, qj, genY, **p):
    c = max([pj[k]/qj[k] for k in pj.keys()])
    while (True):
        y = genY(qj, **p)
        u = random.random()
        if(u < pj[y]/(qj[y]*c)): return y
    return -1
#
def generate(pj,qj,N=100000):      
    freq = {k:0  for k in pj.keys()}    
    for _ in range(N):
        gen = acceptationRejet(pj, qj, lambda qi : int(random.random()*10)+1 , **{})
        freq[gen] += 1
    return {k:v/N for k,v in freq.items()}

# test
pj = {1:0.11,2:0.12,3:0.09,4:0.08,5:0.12,6:0.10,7:0.09,8:0.09,9:0.05,10:0.15}
qj = {1:0.1 ,2:0.1,3:0.1,4:0.1,5:0.1,6:0.1,7:0.1,8:0.1,9:0.1,10:0.1}
print(generate(pj,qj))

#______________________________   Output  ______________________________________
#{1: 0.10696, 2: 0.1202,  3: 0.09187, 4: 0.07928, 5: 0.11926, 6: 0.09927, 
# 7: 0.09127, 8: 0.09055, 9: 0.0494, 10: 0.15194}
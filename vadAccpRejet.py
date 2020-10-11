import random

prob=[0.11,0.12,0.09,0.08,0.12,0.10,0.09,0.09,0.1,0.1]

def accRej(prob):
    while (True):
        u1=random.random()
        y=int(u1*10)+1
        u2=random.random()
        if(u2<prob[y-1]/0.12):
            return y

N=100000
freq={i+1:0 for i in range(10)}
for i in range(N):
    u=random.random()
    gen=accRej(prob)
    freq[gen]+=1

freq={k:v/N for k,v in freq.items()}
print(freq)
import random

def composition():
    u1=random.random()
    u2=random.random()
    if(u1<0.5):
        return int(10*u2)+1
    else:
        return int(5*u2)+6

N=100000
freq={i+1:0 for i in range(10)}
for i in range(N):
    gen=composition()
    freq[gen]+=1

freq={k:v/N for k,v in freq.items()}
print(freq)
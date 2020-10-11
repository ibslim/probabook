import random
from scipy.stats import beta,kstest

def rejet():
    cpt=1
    while(True):
        u1=random.random()
        u2=random.random()
        if(u2<=(256/27)*u1*pow(1-u1,3)):
            return cpt,u1
        else:
            cpt+=1


N=1000
sumcpt=0
generated=[]
for i in range(N):
    cpt,gen=rejet()
    generated.append(gen)
    sumcpt+=cpt
print(sumcpt/N)

#Ajouter test K-S pour verifier qu'elle suit la distribution donnee
print(kstest(generated,beta.cdf,(2,4),alternative="greater"))
#Don’t reject equal distribution against alternative hypothesis: greater
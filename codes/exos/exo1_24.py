#exo1_24.py

from itertools import product
import copy


def prob_urne_boule(u,i):
    return u[i[2]][i[3]]/(u[i[2]]['B'] + u[i[2]]['N'])

u0={ 'F':{'B':2,'N':7}, 'P':{ 'B':5, 'N':6}}
omega=list(product(['F','P'],['B','N'],['F','P'],['B','N']))
PB = 0; PBFP=0
for i in omega:
    u = copy.deepcopy(u0)
    i0c = 'F' if i[0] == 'P' else 'P'
    
    # tirage et transfert de boule
    u[i[0]][i[1]] = u[i[0]][i[1]] - 1; u[i0c ][i[1]] = u[i0c ][i[1]] + 1
    
    P1 = prob_urne_boule(u0, (None,None, i[0],i[1]))
    P = 0.25 * P1 * prob_urne_boule(u,i) 

    if i[3] == 'B': PB = PB + P
    if i[0] == 'F' and i[2]=='P' and i[3]=='B': PBFP += P
    print(i[0],"   ",i[1],"   %0.2f" %P, ' \t ', u)
    
print('P(B) = %0.2f '%PB, ' \t P(F,P,B) = %0.2f' % PBFP, ' \t P(FP|B) = %0.2f' % (PBFP/PB) )

#______________________________   Output  ______________________________________
# F     B    0.01  	  {'F': {'B': 1, 'N': 7}, 'P': {'B': 6, 'N': 6}}
# F     B    0.05  	  {'F': {'B': 1, 'N': 7}, 'P': {'B': 6, 'N': 6}}
# .....
# P     N    0.07  	  {'F': {'B': 2, 'N': 8}, 'P': {'B': 5, 'N': 5}}
# P     N    0.07  	  {'F': {'B': 2, 'N': 8}, 'P': {'B': 5, 'N': 5}}
# P(B) = 0.34   	 P(F,P,B) = 0.11  	 P(FP|B) = 0.32
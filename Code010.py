
from sympy.stats import DiscreteUniform, density, P
from sympy import symbols
from sympy.logic.boolalg import And, Or, Not  
	
R = { 'r1' , 'r2', 'r3',  'r4' }
B = { 'b1', 'b2', 'b3', 'b4', 'b5', 'b6' }
U =  R | B 
codage = { 'rr':100, 'rb':200, 'br':300, 'bb':400 }      

Omega = set([codage[i[0][0]+i[1][0]]+ int(i[0][1])*10+int(i[1][1]) for  i in itArr(U,2)])
print('Omega : ', Omega,',\n   Length :  ', len(Omega))

X = DiscreteUniform('X', Omega)                     
A = X < 301                      ;print('P(A) =',P(A))          #1st red
B = Or(X<201, And(299<X, X<401)) ;print('P(B) =',P(B))          #2nd red
AB = X < 201                     ;print('P(AB)=',P(AB)) #1st & 2nd red
B_gv_A = given(B, A)             ;print('P(B|A)=',   P(B_gv_A)) # B given A

#########################################################
##############           OUTPUT           ###############
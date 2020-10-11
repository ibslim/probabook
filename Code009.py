from fractions import Fraction
from itertools import product

Omega = set(product(range(1,7),repeat=2))   #Omega of throwing dice twice

filterSet=lambda predicate, S : set(filter(predicate,S))
prob_gv_Event =lambda event, gv_Event : Fraction(len(event & gv_Event),len(gv_Event))
prob_Event=lambda event,omega:Fraction(len(event),len(omega)) 

F= filterSet(lambda a: a[0] == 4,Omega)           
print("F given Event : ", F, ", P(F)=", prob_Event(F,Omega))

E= filterSet(lambda a : a[0] + a[1] == 6,Omega)   
print("E event : ",E, ", P(E)=", prob_Event(E,Omega))  
   
EF = E & F                                    
print("E and F event : ",EF, ", P(E & F)=", prob_Event(EF,Omega))     

p_given_F = prob_gv_Event(E,F)                
print("Prob of E given F : ", p_given_F) 

#..........................  OUTPUT  ..........................     

# F given Event :  {(4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1)} , P(F)= 1/6
# E event :  {(5, 1), (3, 3), (1, 5), (4, 2), (2, 4)} , P(E)= 5/36
# E and F event :  {(4, 2)} , P(E & F)= 1/36
# Prob of E given F :  1/6
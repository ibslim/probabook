#Code002.py
from sympy.stats import Coin, Die, density   	
print("Events manipulation (operations)")

abc_Omega = {1,2,3,4,5,6}    ;print("Univers Omega         : ",abc_Omega)
A = {2,5}                    ;print("Event A               : ", A)
B = {3,4,5}                  ;print("Event B               : ",B)
isEvent = A < abc_Omega      ;print("is A event of Omega   : ", isEvent)
a_bar = abc_Omega - A        ;print("Complement of A       : ", a_bar)
C = A & B                    ;print("Union of A & B        : ", C)
D = A | B                    ;print("Intersection of A & B : ", D)
E = A - B                    ;print("Difference of A & B   : ", C)
F = A & B                    ;print("Symetric Diff A & B   : ", C)

"""predicate to check if a number is even
Ce code utilise Lambda expression qui retourne une fonction qui indique si le
nombre donne en argument est pair.
La fonction filter selectionne les elements de l'ensemble donne en argument 
satisfaisants la condition exprimee par l'expression lambda (premier argument).
"""
isEvenNumber = lambda nb : nb % 2 == 0

#Die
die = Die('Die')
die_omega = set(density(die).dict.keys()) 
evenNb = set(filter(isEvenNumber,die_omega))
print("Event A even numbers  : ", evenNb) 

evenNbComplement = set(die_omega) - set(evenNb)
print("Event Complement of A : ", evenNbComplement)

#______________________________   Output  ______________________________________
# Events manipulation (operations)
# Univers Omega         :  {1, 2, 3, 4, 5, 6}
# Event A               :  {2, 5}
# Event B               :  {3, 4, 5}
# is A event of Omega   :  True
# Complement of A       :  {1, 3, 4, 6}
# Union of A & B        :  {5}
# Intersection of A & B :  {2, 3, 4, 5}
# Difference of A & B   :  {5}
# Symetric Diff A & B   :  {5}
# Event A even numbers  :  {2, 4, 6}
# Event Complement of A :  {1, 3, 5}


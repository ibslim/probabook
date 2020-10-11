
from symbulate import *

die = [1, 2, 3, 4, 5, 6]#cette ligne peut etre remplacee par:list(range(1, 6+1))
roll = BoxModel(die)
print(roll.draw())
print(BoxModel(['D', 'R', 'I'], probs=[0.32, 0.27, 0.41], size=5).draw())
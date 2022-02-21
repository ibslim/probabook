#code701.py

from symbulate import BoxModel

# Die sampling
# this line could be replaced by :list(range(1, 6+1))
die = [1, 2, 3, 4, 5, 6]
roll = BoxModel(die)
print(roll.draw())

# draws 10 samples from ['A', 'B', 'C', 'D'] with probabilities [0.22, 0.27, 0.41, 0.10]
print(''.join(list(BoxModel(['A', 'B', 'C', 'D'], probs=[0.22, 0.27, 0.41, 0.10], size=10).draw())))

#______________________________   Output  ______________________________________
# 2
# CACCCCBAAB
#Code402.py
from CMTD import CMTD

# Figurine example
P = [[0.25, 0.75, 0.00, 0.00],
     [0.00, 0.50, 0.50, 0.00],
     [0.00, 0.00, 0.75, 0.25],
     [0.00, 0.00, 0.00, 1.00]]

print(CMTD(P).nSteps(3))

#______________________________   Output  ____________________________________
#[0.015625 0.328125 0.5625   0.09375 ]

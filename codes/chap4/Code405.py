#Code405.py

from CMTD import CMTD

P = [[1.0, 0.0, 0.0, 0.0],
     [1/3, 0.0, 2/3, 0.0],
     [0.0, 1/2, 0.0, 1/2],
     [0.0, 0.0, 0.0, 1.0]] 

print(CMTD(P).absorbing_proba(1))
#______________________________   Output  ______________________________________
#[1.   0.5  0.25 0.  ]

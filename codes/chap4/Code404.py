#Code404.py

from CMTD import CMTD

P = [[0.5, 0.5, 0.0],
     [0.0, 1/3, 2/3],
     [0.5, 0.5, 0.0]]

print(CMTD(P).hitting_time(3))
print(CMTD(P).return_time(1))

#______________________________   Output  ______________________________________
# [3.5 1.5 0. ]
# 3.499999999999999

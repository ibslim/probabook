#Code403.py

from CMTD import CMTD

# Classification example
P = [[0.00, 1/2 , 1/2 , 0.00, 0.00, 0.00, 0.00, 0.00],
     [1/3 , 2/3 , 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
     [0.00, 0.00, 0.00, 1/4 , 0.00, 0.00, 0.00, 3/4 ],
     [0.00, 0.00, 1/2 , 0.00, 1/2 , 0.00, 0.00, 0.00],
     [0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 0.00],
     [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00],
     [0.00, 0.00, 0.00, 0.00, 0.00, 2/3 , 0.00, 1/3 ],
     [0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 0.00]]

print(CMTD(P).classify())
print(CMTD(P).is_irreducible())
#______________________________   Output  ______________________________________
#{'transitoire': [{5}, {3, 4}, {1, 2}], 'reccurente': [{8, 6, 7}]}


#code702.py

from symbulate import BoxModel, ProbabilitySpace, Poisson, Exponential

#1 probabaility space with user defined function 
def gender_hobbies_sim():
    gender = BoxModel(["male", "female"], probs=[.2, .8]).draw()
    if gender == "male":
        hobbies = BoxModel(["science", "art", "sport"], probs=[.3, .3, .4]).draw()
    else:
        hobbies = BoxModel(["science", "art", "sport"], probs=[.2, .5, .3]).draw()
    return gender, hobbies
P = ProbabilitySpace(gender_hobbies_sim)
print(P.draw())

#2 independants probability spaces
die6, die4 = list(range(1,7,1)), list((1,5,1))
lancers = BoxModel(die6)*BoxModel(die4)
print(lancers.draw())

#3 independants probability spaces
three = BoxModel(['P','F'])*Poisson(lam=3)*Exponential(rate=4)
print(three.draw())

#______________________________   Output  ______________________________________
#('female', 'art')
#(5, 1)
#(F, 1, 0.029286540827854368)
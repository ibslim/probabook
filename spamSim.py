from symbulate import *

def spam_sim():
    email_type = BoxModel(["spam", "not spam"], probs=[.1, .9]).draw()
    if email_type == "spam":
        has_money = BoxModel(["money", "no money"], probs=[.3, .7]).draw()
    else:
        has_money = BoxModel(["money", "no money"], probs=[.02, .98]).draw()
    return email_type, has_money
P = ProbabilitySpace(spam_sim)
print(P.draw())

print(Binomial(n=10, p=0.5).draw())  #Loi binomiale
print(Normal(mean=0, sd=1).draw())  #Loi normale

# 2 espaces de probabilites independants
die6 = list(range(1, 6+1, 1))
die4 = list(range(1, 4+1, 1))
rolls = BoxModel(die6) * BoxModel(die4)
print(rolls.draw())
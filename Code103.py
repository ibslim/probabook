#symbolic computation APIs
from sympy import S , Symbol, symbols, Rational, simplify 
    
# Basic Probability routines APIS
from sympy.stats import density, cdf
from sympy.stats import P, E, variance as V

# Random Var APIs
from sympy.stats import FiniteRV, Die, Coin, DiscreteUniform,  Bernoulli, Binomial, Geometric, Poisson, Hypergeometric       

# I- Finite Random Var List
myDensity = {0: .1, 1: .2, 2: .3, 3: .4}  
p  = S.One / 5
finiteRVs = {
        "Finite R.V       :":FiniteRV('X', myDensity),       # Defined FRV with density {0:.1, 1:.2, 2:.3, 3:.4}        
        "Die6             :":Die('D6', 6),                   # Standard Die with 6 faces
        "Die4             :":Die('D4', 4),                   # Die with 4 faces
        "Coin Half        :":Coin('C'),                      # Bernouli p=1/2 representing Toss Coin
        "Coin3/5          :":Coin('C2', Rational(3, 5)),     # Bernouli p=3/5 representing Toss Coin    
        "Discrete Uniform3:":DiscreteUniform('X', symbols('a b c')),   # Discrete Uniform over {a,b,c}
        "Discrete Uniform5:":DiscreteUniform('Y', list(range(5))),     # over {0,1,2,3,4}    
        "Bernoulli3/4     :":Bernoulli('X', S(3)/4),                   # Bernouli p=3/4
        "Bernoulli Half   :":Bernoulli('X', S.Half, 'Heads', 'Tails'), # Bernouli p=1/2
        "Binomial Half 4  :":Binomial('X', 4, S.Half),                 # Binomial (n=4,p1/2)    
        "Hypergeometric   :":Hypergeometric('X', 10, 5, 3) 
    }

# Print density, Expectation and Variance of each FRV in list above.
for k,X in finiteRVs.items() : 
    Pdf, Ex, Vx = density(X).dict,  E(X), V(X)          
    print(k,' \t ', Pdf, ' \t ', Ex, ' \t ', Vx)  #{a: 1/3, b: 1/3, c: 1/3}

print("-------------------------------------------------------------")    
# II- Discrete (infinite) RV List
k     = Symbol("k")
lamda = Symbol("Lambda", positive=True)            # rate = lamda

discreteRVs = {
        "Geometric:":Geometric("X", p),                        # Geometric(p=1/5)
        "Poisson  :":Poisson("X", lamda)                       # Poisson(lambda)
    }
print("-----------------------------------------------------------")
for key,X in discreteRVs.items() : 
    Pdf, Cdf,  Ex, Vx = density(X)(k), cdf(X)(k),  E(X), V(X)  #simplify(V(X))
    print(key,' \t ',Pdf, ' \t ', Cdf, ' \t ', Ex, ' \t ', Vx)

#..........................        OUTPUT       ..........................     

# Finite R.V       :  	  {0: 0.1, 1: 0.2, 2: 0.3, 3: 0.4}  	  2.00000000000000  	  1.00000000000000
# Die6             :  	  {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}  	  7/2  	  35/12
# Die4             :  	  {1: 1/4, 2: 1/4, 3: 1/4, 4: 1/4}  	  5/2  	  5/4
# Coin Half        :  	  {H: 1/2, T: 1/2}  	  H/2 + T/2  	  (-H/2 + T/2)**2/2 + (H/2 - T/2)**2/2
# Coin3/5          :  	  {H: 3/5, T: 2/5}  	  3*H/5 + 2*T/5  	  2*(-3*H/5 + 3*T/5)**2/5 + 3*(2*H/5 - 2*T/5)**2/5
# Discrete Uniform3:  	  {b: 1/3, c: 1/3, a: 1/3}  	  a/3 + b/3 + c/3  	  (-a/3 - b/3 + 2*c/3)**2/3 + (-a/3 + 2*b/3 - c/3)**2/3 + (2*a/3 - b/3 - c/3)**2/3
# Discrete Uniform5:  	  {0: 1/5, 1: 1/5, 2: 1/5, 3: 1/5, 4: 1/5}  	  2  	  2
# Bernoulli3/4     :  	  {0: 1/4, 1: 3/4}  	  3/4  	  3/16
# Bernoulli Half   :  	  {Tails: 1/2, Heads: 1/2}  	  Heads/2 + Tails/2  	  (-Heads/2 + Tails/2)**2/2 + (Heads/2 - Tails/2)**2/2
# Binomial Half 4  :  	  {0: 1/16, 1: 1/4, 2: 3/8, 3: 1/4, 4: 1/16}  	  2  	  1
# Hypergeometric   :  	  {0: 1/12, 1: 5/12, 2: 5/12, 3: 1/12}  	  3/2  	  7/12
# --------------------------------------------------------------------------------------
# Geometric:  	  (4/5)**(k - 1)/5  	  Piecewise((1 - 5*(4/5)**(k + 1)/4, k >= 1), (0, True))  	  5  	  20
# Poisson  :  	  Lambda**k*exp(-Lambda)/factorial(k)  	  Piecewise(((-Lambda**(-k - 1)*Lambda**(k + 1)*(k + 1)*exp(Lambda)*lowergamma(k + 1, Lambda)/factorial(k + 1) + exp(Lambda))*exp(-Lambda), k >= 0), (0, True))  	  Lambda  	  Lambda

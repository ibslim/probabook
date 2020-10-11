
    """
        Module : sympy.stats.
        Class : Probability
    
        Symbolic expression for the probability.
    """

    # Examples
    from sympy.stats import Probability, Normal
    from sympy import Integral
    
    X = Normal("X", 0, 1)
    prob = Probability(X > 1)
    print(prob)       # Probability(X > 1)

    #Integral representation:
    print(prob.rewrite(Integral))  #Integral(sqrt(2)*exp(-_z**2/2)/(2*sqrt(pi)), (_z, 1, oo))

    #Evaluation of the integral:
    print(prob.evaluate_integral())  #sqrt(2)*(-sqrt(2)*sqrt(pi)*erf(sqrt(2)/2) + sqrt(2)*sqrt(pi))/
    .
    
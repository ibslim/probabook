
    """
        Module   :  sympy.stats.
        Function :  density(    expr, 
                                condition=None, 
                                evaluate=True, 
                                numsamples=None, 
                                **kwargs)

        Probability density of a random expression, optionally given a second condition.
        This density will take on different forms for different types of probability spaces. Discrete variables produce Dicts. Continuous variables produce Lambdas.

        Parameters:	
        - expr : Expr containing RandomSymbols : The expression of which you want to compute the density value

        - condition : Relational containing RandomSymbols : A conditional expression. density(X > 1, X > 0) is density of X > 1 given X > 0

        - numsamples : int : Enables sampling and approximates the density with this many samples
    """

    # Examples
    from sympy.stats import density, Die, Normal
    from sympy import Symbol

    x = Symbol('x')
    D = Die('D', 6)
    X = Normal(x, 0, 1)

    d1 = density(D).dict   ;print(d1)  #{1:1/6, 2:1/6, 3:1/6, 4:1/6, 5:1/6, 6:1/6}
    d2 = density(2*D).dict ;print(d2)  #{2:1/6,4:1/6,6:1/6,8:1/6,10:1/6,12:1/6}
    dn = density(X)(x)     ;print(dn)  #sqrt(2)*exp(-x**2/2)/(2*sqrt(pi))
    .
    


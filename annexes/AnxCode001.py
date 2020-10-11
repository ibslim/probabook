    
    """
        Module   : sympy.stats
        Class    : P (  condition, 
                        given_condition=None, 
                        numsamples=None, 
                        evaluate=True, **kwargs)

        Probability that a condition is true, optionally given a second condition

        Parameters:	
        - condition : Combination of Relationals containing RandomSymbols, The condition of which you want to compute the probability.

        - given_condition : Combination of Relationals containing RandomSymbols A conditional expression. P(X>1, X>0) is expectation of X>1 given X>0.

        - numsamples : int , Enables sampling and approximates the probability with this many samples.

        - evaluate : Bool (defaults to True), In case of continuous systems return unevaluated integral.
    """

    # Examples
    from sympy.stats import P, Die
    from sympy import Eq

    X, Y = Die('X', 6), Die('Y', 6)
    print(P(X > 3))             #1/2
    print(P(Eq(X, 5), X > 2))   # Proba that X == 5 given that X > 2  = 1/4
    print(P(X > Y))             # 5/12
    .
    
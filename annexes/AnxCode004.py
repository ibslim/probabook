
    """"
        Module   : sympy.stats.
        Function : given(expr, condition=None, **kwargs)

        Conditional Random Expression From a random expression and a condition on that expression creates a new probability space from the condition and returns the same expression on that conditional probability space.
    """
    # Examples
    from sympy.stats import given, density, Die
    X  = Die('X', 6)
    Y  = given(X, X > 3)
    d0 = density(Y).dict    ;print(d0)     #{4: 1/3, 5: 1/3, 6: 1/3}

    #Convention, if the condition is a random symbol then that symbol is considered fixed.
    from sympy.stats import Normal
    from sympy import pprint
    from sympy.abc import z
    X = Normal('X', 0, 1)
    Y = Normal('Y', 0, 1)
    pprint(density(X + Y, Y)(z), use_unicode=False)
    .
    

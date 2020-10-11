
    """
    Module : sympy.stats
    Function : Coin(name, p=1/2)[source]
    Create a Finite Random Variable representing a Coin toss.

    Probability p is the chance of gettings 'Heads.' Half by default, Returns a RandomSymbol.
    """
    #   Examples
    from sympy.stats import Coin, density
    from sympy import Rational

    C = Coin('C') # A fair coin toss
    d0 = density(C).dict        ;print(d0)   #{H: 1/2, T: 1/2}

    C2 = Coin('C2', Rational(3, 5)) # An unfair coin
    d1 = density(C2).dict       ;print(d1)   #{H: 3/5, T: 2/5}
    .

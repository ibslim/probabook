
    """
    sympy.stats.
    DiscreteUniform(name, items)

    Create a Finite Random Variable representing a uniform distribution over the input set. Returns a RandomSymbol.
    """
    #    Examples

    from sympy.stats import DiscreteUniform, density
    from sympy import symbols
    X = DiscreteUniform('X', symbols('a b c')) # equally likely over a, b, c
    dx = density(X).dict    ;print(dx)  #{a: 1/3, b: 1/3, c: 1/3}
    Y = DiscreteUniform('Y', list(range(5)))   # distribution over a range
    dy = density(Y).dict    ;print(dy)  #{0: 1/5, 1: 1/5, 2: 1/5, 3: 1/5, 4: 1/5}
    .


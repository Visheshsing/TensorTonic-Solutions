import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value

    """
    if len(x) != len(p):
        raise ValueError("Shapes of x and p must match")

    if abs(sum(p) - 1) > 1e-6:
        raise ValueError("Probabilities must sum to 1")
    return sum(x*p for x,p in zip(x,p))
        

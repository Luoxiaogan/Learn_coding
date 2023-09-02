import operator
def reduce1(f, s, initial):
    """ COmbine elements of a pairwise using f, starting with initial """
    for x in s:
        initial = f(initial, x)
    return initial

def reduce2(f, s, initial):
    """ COmbine elements of a pairwise using f, starting with initial """
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce2(f, rest, f(initial,first))
    
def divide_all(n,ds):
    try:
        return reduce1(operator.truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')
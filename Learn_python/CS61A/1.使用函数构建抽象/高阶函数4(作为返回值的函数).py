def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

#Example：牛顿法
def improve(update, close, guess=1):
    while not close(guess):
        guess=update(guess)
    return guess

def approx_eq(x, y, tol=1e-3):
    return abs(x-y) < tol

def newton_update(f, df):
    def update(x):
        return x-f(x)/df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x),0)
    return improve(newton_update(f, df), near_zero)
    
def compose1(f, g):
    """ lambda              x         :              f(g(x))
        "A function that    takes x   and returns    f(g(x))"
    """
    return lambda x:f(g(x))

""" 
等价于：
compose1=lambda f,g : lambda x: f(g(x))
"""

#函数装饰器：decorator
def trace(fn):
    """ 定义了一个高阶函数 trace，它返回一个函数，该函数在调用其参数前先输出一个打印语句来显示该参数
    """
    def wrapped(x):
        print('->',fn,'(',x,')')
        return fn(x)
    return wrapped

@trace #注解：annotation
def triple(x):
    return 3*x

""" 等价于：
def triple(x):
    return 3*x
triple=trace(triple)
"""

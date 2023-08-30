#Curring：使用高阶函数将一个接受多个参数的函数转换为一个函数链，每个函数接受一个参数
def pow(x, y):
    """ x的y次方
    """
    i=1
    total=x
    while i<y:
        total, i = total*x, i+1
    return total

def curried_pow(x):
    def h(y):
        return pow(x,y)
    return h

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start=start+1
#可以构建函数来打印出x的前n次方的所有数：
def f(x,n):
    return map_to_range(1, n, curried_pow(x))

#可以构造函数来进行自动柯里化，以及逆柯里化
def curry2(f):
    """ 返回给定的双参数函数的柯里化版本
    """
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

def uncurry2(g):
    """ 返回给定的柯里化函数的双参数版本
    """
    def f(x,y):
        return g(x)(y)
    return f

""" curry2 函数接受一个双参数函数 f 并返回一个单参数函数 g。当 g 应用于参数 x 时，它返回一个单参数函数 h。当 h 应用于参数 y 时，它调用 f(x, y)。因此，curry2(f)(x)(y) 等价于 f(x, y) 。uncurry2 函数反转了柯里化变换，因此 uncurry2(curry2(f)) 等价于 f。 """
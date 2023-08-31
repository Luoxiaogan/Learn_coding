import operator
import fractions
#Example：有理数
def gcd(x,y):
    if x>=y:
        pre=y
        now=x
    else:
        pre=x
        now=y
    while(now!=0):
        pre,now=now,pre%now
    return pre

def rational(n,d):
    """ 返回具有分子n,分母d的有理数
    """
    g=gcd(n,d)
    return [n//g,d//g]

def numer(x):
    """ 返回有理数x的分子
    """
    return x[0]

def denmo(x):
    """ 返回有理数x的分母
    """
    return x[1]

###假设已经得到这三个函数之后，我们就可以进行加法，乘法，打印，测试相等的函数设计
#一个强大的程序设计策略：一厢情愿（wishful thinking）
def add_rationals(x,y):
    nx,dx=numer(x),denmo(x)
    ny,dy=numer(y),denmo(y)
    return rational(nx*dy+ny*dx,dx*dy)

def mul_rationals(x,y):
    return rational(numer(x)*numer(y),denmo(x)*denmo(y))

def print_rational(x):
    print(numer(x),'/',denmo(x))

def rational_are_equal(x,y):
    return numer(x)*denmo(y)==numer(y)*denmo(x)

#使用list复合结构来完成三个函数的构造

#抽象障碍：Abstraction Barries:不同级别的函数分开使用而不是混用，这样可以再后面有修改需求的时候方便很多
"""通常，我们可以使用选择器和构造器的集合以及一些行为条件来表达抽象数据。只要满足行为条件（比如上面的除法属性），选择器和构造器就构成了一种数据的有效表示。抽象屏障下的实现细节可能会改变，但只要行为没有改变，那么数据抽象就仍然有效，并且使用该数据抽象编写的任何程序都将保持正确。
"""

""" 我们实际上并不一定需要 list 类型来创建对，作为替代，我们可以用两个函数 pair 和 select 来实现这个描述以及一个二元列表。 """
def pair(x,y):
    """ Return a function that represents a pair. """
    def get(index):
        if index==0:
            return x
        elif index==1:
            return y
    return get

def select(p,i):
    """ Return the emelent of index i of pair p """
    return p(i)
#Assert
def fact(n):
    assert isinstance(n,int)
    assert n>=0
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def half_fact(n):
    return fact(n/2)

#Testing
""" Have confidence in the correctness of subcomponents """
""" Doctest : python -m doctest file.py"""

#Print debugging
def fact1(n):
    print("Debug n=",n)
    if n==0:
        return 1
    else:
        return n*fact1(n-1)

def half_fact1(n):
    return fact1(n/2)

#Interactive Debugging

#Error Types
###SyntexError——typo
###IndentationError——wrong text editor, wrong space, tab and spaces
###TypeError——wrong call

#Traceback——error, line,...

#Exceptions: AssertionError
""" assert False, 'Error' """ #可以在不同的Assertion报错的时候，设置报错的注释

""" TypeError, NameError, KeyError, RuntimeError """
""" raise TypeError('Bad argument') """

#Try Statement——handle exceptions
try:
    x=1/0
except ZeroDivisionError as e:
    print('handing a', type(e))
    x=0#Set a default value

def invert(x):
    y=1/x
    print('Never printed if x is 0')
    return y

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('handled',e)
        return 0
    
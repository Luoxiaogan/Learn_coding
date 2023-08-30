import math
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total

def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
    return total

#1.抽象为高阶函数——函数作为参数
def summation(n,term):
    total, k=0,1
    while k<=n:
        total, k = total + term(k), k+1
    return total

def identity(x):
    return x
def cubes(x):
    return x*x*x
def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))
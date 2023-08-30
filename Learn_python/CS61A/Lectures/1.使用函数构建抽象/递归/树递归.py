#tree recursion
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1)+fib(n-2)

#Example:分割数(Partition fuction)
""" 求正整数 n 的分割数,最大部分为 m,即 n 可以分割为不大于 m 的正整数的和，并且按递增顺序排列 
"""
def count_partitions(n,m):
    """ 使用最大数为 m 的整数分割 n 的方式的数量等于:
        使用最大数为 m 的整数分割 n-m 的方式的数量(至少包含一个m的分割)，加上
        使用最大数为 m-1 的整数分割 n 的方式的数量(不包含m的分割)
    """
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m==0:
        return 0
    else:
        return count_partitions(n-m,m)+count_partitions(n,m-1)
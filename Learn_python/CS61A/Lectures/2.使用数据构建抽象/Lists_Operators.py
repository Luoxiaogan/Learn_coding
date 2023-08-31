#序列遍历
def count(s,value):
    """ 统计序列s中value出现的次数 """
    total,index=0,0
    while index<len(s):
        if s[index]==value:
            total+=1
        index+=1
    return total

def count2(s,value):
    total=0
    for element in s:
        if element==value:
            total+=1
    return total

#序列解包:绑定多个名称到固定长度序列中的多个值的模式称为序列解包；这与赋值语句中将多个名称绑定到多个值的模式类似。
pairs=[[1,2],[2,2],[2,3],[4,4]]
same_count=0
for x,y in pairs:
    if x==y:
        same_count+=1
print(same_count)

#序列处理

#列表推导式：List Comprehension
odds=[1,3,5,7,9]
#[<map expression> for <name> in <sequence expression> if <filter expression>

#聚合： Aggregation

def divisors(n):
    """ 所有比n小的因子 """
    return [1]+[x for x in range(2,n) if n%x==0]

"""
>>> [n for n in range(1, 1000) if sum(divisors(n)) == n]
[6, 28, 496]
"""
#Question:在给定面积的情况下找到具有整数边长的矩形的最小周长。
#当然由条件可以导出面积一定是整数
def width(area,height):
    """ 给定面积和高度,计算宽度 """
    assert area%height==0
    return area//height
def perimeter(width,height):
    """ 给定高度和宽度，计算周长 """
    return 2*(width+height)
def minimum_perimeter(area):
    """ 计算给定面积下的满足条件的最小周长 """
    heights=divisors(area)#所有可能的高度
    perimeters = [perimeter(width(area,h),h) for h in heights]#所有可能的面积
    return min(perimeters)
#有对于list的三个操作：add,max,min
from operator import __mul__
#高阶函数：High-Order Functions
def apply_to_all(map_fn,s):
    return [map_fn(x) for x in s]
def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]
def reduce(reduce_fn, s, initial):
    """
    >>> reduce(mul, [2,3,8],1)
    48
    """
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    divides_n = lambda x: n%x==0
    return [1]+keep_if(divides_n,range(2,n))

from operator import __add__
def sum_of_divisors(n):
    return reduce(__add__,divisors_of(n),0)
def perfect(n):
    return sum_of_divisors(n)==n

#约定的名字：Comventional Names
#apply_to_all ——> map
#keep_if ——> filter
#在 Python 中，内置的  map  和  filter  是这些不返回列表的函数的归纳

""" apply_to_all= lambda map_fn , s : list(map(map_fn, s))
keep_if = lambda filter_fn, s : list(filter(filter_fn,s)) """

import functools
from operator import __mul__
def product(s):
    return functools.reduce(__mul__,s)
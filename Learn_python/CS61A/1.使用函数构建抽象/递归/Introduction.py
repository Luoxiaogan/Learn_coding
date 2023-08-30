def sum_digits(n):
    """ 返回正整数n的所有数字位之和 """
    if n<10:
        return n
    else:
        all_but_last, last = n//10, n%10
        return sum_digits(all_but_last)+last
    
#计算n的阶乘
#迭代方法：
def fact_iter(n):
    total=1
    i=1
    while(i<=n):
        total=total*i
        i=i+1
    return total
#递归方法
def fact(n):
    if n==1:
        return 1
    else:
        return fact(n-1)*n

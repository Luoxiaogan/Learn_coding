HW_SOURCE_FILE=__file__


def composer(func=lambda x: x):
    """
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """
    def func_adder(g):
        "*** YOUR CODE HERE ***"
        h = lambda x:func(g(x))
        return composer(h)
    return func, func_adder

""" Remark:
composer():返回函数f(x)=x和函数func_adder
而func_adder(g)返回的是g和新的func_adder(不妨记为func_adder1)
而func_adder1(h)返回g(h)这个函数和新的func_adder(记为func_adder2)
而func_adder2(w)返回g(h(w))这个函数和新的func_adder...s
"""


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> # ban recursion
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    else:
        i=4
        temp=0
        a1,a2,a3=1,2,3
        while i<=n:
            if i%3==1:
                temp=3*a1+2*a2+a3
                a1=temp
            elif i%3==2:
                temp=3*a2+2*a3+a1
                a2=temp
            else:
                temp=3*a3+2*a1+a2
                a3=temp
            i=i+1
        return temp



def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    #必须使用递归来做(recursive method)
    #思路：从最后一项n%10开始往下减
    if n<10:
        return 0
    else:
        if n%10==(n//10)%10:
            return 0+missing_digits(n//10)
        else:
            return n%10-(n//10)%10-1+missing_digits(n//10)


def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(n, m):#来自学长的答案！！！
        if n == 0:#组合完毕
            return 1
        elif n < (1 << m):#超出了，不能组合了
            return 0
        else:
            return helper(n, m + 1) + helper(n - (1 << m), m)
    return helper(total, 0)#实际上需要减去1，只不过示例里面没有2的次幂

#1<<m 表示1的二进制向左移动m位，其实就是快速计算2^m的方法
#我想复杂了!
    

def biggest_coin(n):#小于等于n的最大硬币面值(可以等于n),用于测试
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            a=2
            while(a<=n):
                a=a*2
            return a//2
        

def count_change_advance(total,a):#Test
        """ 计算count_change(total)
        并且:
            1.之后减的数要大于等于a(保证升序)
            2.减出来剩下的数也要大于a(防止4——>4=1+3——>1+1+2=1+2+1的重复)
            3.包含(total-a)+0
        """
        #递归终止情况
        if total==0:
            return 0
        elif total==1:
            return 1
        elif total==a:#即4=4+0
            return 1
        if total-a<a:#比如:3-2<1(1+2+1=1+1+2),2=1+1不会有问题的
            return 0#舍去这种情况
        biggest=biggest_coin(total)
        #得到最大面值
        sum,index=0,a
        while(index<=total):
            sum=sum+count_change_advance(total-index,index)
            index=index*2
        return sum

    
        



def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'


#对递归函数的计算过程进行可视化
def cascade(n):
    """ 打印数字 n 的前缀的级联 """
    if n<10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

#Example
def is_even(n):
    if n==0:
        return True
    else:
        return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    else:
        return is_even(n-1)

def play_alice(n):
    if n==0:
        print("Bob wins!")
    else:
        play_bob(n-1)
def play_bob(n):
    if n==0:
        print("Alice wins!")
    elif is_even(n):
        return play_alice(n-2)
    else:
        return play_alice(n-1)
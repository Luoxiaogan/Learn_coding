def f(a,b):
    if a>b:
        return f(a-3,2*b)
    elif a<b:
        return f(b//2,a)
    else:
        return b
def crust():
    print("70km")
    def mantle():
        print("2900km")
        def core():
            print("5300km")
            return mantle()
        return core
    return mantle
""" 
drill = crust ：drill 就是crust 函数
drill = drill ()： 运行 crust()，得到return 的 mantle，因此此时，drill 就是 mantle
drill = drill()：运行 mantle()，得到return 的 core，因此此时，drill就是core
drill =drill(): 运行 core()，再运行 mantel(),此时, drill 是mantle
drill() ： 运行mantle，两次输出之后，返回core（函数）
"""

""" 
n % 10 -> last_digit
n // 10 -> remove_last_digit 
"""

""" We need to keep track of a few things:
    - value
    - index
    - direction (very important) """
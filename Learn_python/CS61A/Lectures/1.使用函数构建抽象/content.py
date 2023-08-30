def pressure(v, t, n=6.022e23):
        """计算理想气体的压力，单位为帕斯卡

        使用理想气体定律：http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- 气体体积，单位为立方米
        t -- 绝对温度，单位为开尔文
        n -- 气体粒子
        """
        k = 1.38e-23  # 玻尔兹曼常数
        return n * k * t / v

def fib(n):
        """ 计算第n项斐波那契数列, for n>=2

        >>> fib(4)
        5
        >>> fib(3)
        4
        """
        pre, cur=0,1
        i=1
        while(i<=n):
                pre,cur=cur,pre+cur
                i=i+1
        return cur
#高阶函数，能够接受参数，再返回参数

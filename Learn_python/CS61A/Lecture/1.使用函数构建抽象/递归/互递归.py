#mutually recursive
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
    
#也可以整合到一起
def is_even2(n):
    if n==0:
        return True
    else:
        if (n-1)==0:
            return False
        else:
            return is_even((n-1)-1)
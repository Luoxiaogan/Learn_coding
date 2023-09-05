#链表：linked list
empty = "empty"
def is_link(s):
    """ s is a linked list """
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    assert is_link(rest)
    return [first, rest]

def first(s):
    assert is_link(s)
    assert s != empty
    return s[0]

def rest(s):
    assert is_link(s)
    assert s != empty
    return s[1]

def len_link(s):
    length = 0
    while s != empty:
        s, length = rest(s), length+1
    return length

def getitem_link(s, i):
    while i > 0:
        s, i =rest(s), i-1
    return first(s)

def len_link_recursive(s):
    if s == empty:
        return 0
    else:
        return 1+len_link_recursive(rest(s))
    
def getitem_link_recursive(s,i):
    if i==0:
        return first(s)
    else:
        return getitem_link_recursive(rest(s), i-1)
    
def extend_link(s,t):
    """将 t 插入到链表 s 的每个元素之后"""
    assert is_link(s) and is_link(t)
    if s==empty:
        return t
    else:
        return link(first(s), extend_link(rest(s),t))
    
def apply_to_all_link(f,s):
    assert is_link(s)
    if s==empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f,rest(s)))

def keep_if_link(f,s):
    """ 返回 s 中 f(e) 为 True 的元素 """
    assert is_link(s)
    if s==empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept

def join_link(s, separator):
    """ 返回分隔符分隔的s中所有元素组成的字符串 """
    if s== empty:
        return ""
    elif rest(s)==empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
    
def partitions(n, m):
    """ 返回一个由n个分区组成的链表,每个分区的部分数最多为m。每个分区表示一个链表 """
    if n==0:
        return link(empty, empty)
    elif n<0 or m==0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m ,without_m)
    
def print_partitions(n,m):
    lists = partitions(n,m)
    strings = apply_to_all_link(lambda s: join_link(s, '+'), lists)
    print(join_link(strings, '\n'))
#Slicing


#Aggregation

#Tree——Recursive description, Relative description

def tree(root_label,branches=[]):#构造函数
    for branch in branches:
        assert is_tree(branch),'Branches must be trees'
    return [root_label]+list(branches)

def label(tree):#选择器
    return tree[0]

def branches(tree):#选择器
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):#Recuisive function
            return False
    return True
    
def is_leaf(tree):#检查是否有分支
    return not branches(tree)

#Tree Processing
def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])
    
def count_leaves(t):
    """ Count the leaves of a tree """
    if is_leaf(t):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(t)]
        return sum(branch_counts)

def leaves(tree):
    """ Return a list containing all the leaf lables of tree """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum((leaves(branche) for branche in branches(tree)),[])
    
def increment_leaves(t):
    """ Return a tree like t with leaf labels incremented """
    if is_leaf(t):
        return tree(label(t)+1,[])
    else:
        bs=[increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)
    
def increment(t):
    """ Return a tree like t but with all labels incremented """
    return tree(label(t)+1, [increment(b) for b in branches(t)])

def print_tree(t,indent=0):
    print(' '*indent + str(label(t)))
    for b in branches(t):
        print_tree(b,indent+1)

def min_depth(t):
    """ A simple function to return the distance between t's root and its closest leaf """
    if is_leaf(t):
        return 0
    h=float('inf')# Python's version of infinity
    for b in branches(t):
        h=min(h,1+min_depth(b))
    return h
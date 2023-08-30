#2.作为通用方法的函数
#Example: 迭代改进的通用方法
def improve(update, close, guess=1):
    """ update用于更行，close用于判断是否达到一定精度，guess初始设定为1 
    (repetitive refinement)
    """
    while not close(guess):
        guess=update(guess)
    return guess

##应用于求解黄金比例
def golden_update(guess):
    return 1/guess+1
def square_close_to_successor(guess):
    return approx_eq(guess*guess, guess+1)
def approx_eq(x, y, tolerance=1e-50):
    return abs(x-y) < tolerance
#所以，求解黄金比例的函数就是：improve(golden_update, square_close_to_successor)

#Lists
import operator
odds=[32,34,45,56]
print(odds[0],' ',odds[3])
print(len(odds))
digits=[1,8,2,8]
print(len(digits))
print(digits[3])
operator.getitem(digits,3)
print([2,7]+digits*2)
print(operator.add([2,7],operator.mul(digits,2)))
pairs=[[10,20],[30,40]]
print(pairs[1])
print(pairs[1][0])

#Containers
digits=[1,8,2,8]
print(1 in digits)#True
print(5 not in digits) #True
print(1 == '1') #False
print('1' in digits)#False
print([1,8] in digits)#False
print([1,2] in [[1,2], 4])#True
print([1,2] in [[[1,2]],3])#False

#For Statments-----Sequence Iteration
def count(s,value):
    """ Count the number of times that value occurs in sequence s.
    """
    total=0
    for element in s:#for every element in squence s
        if element==value:
            total+=1
    return total
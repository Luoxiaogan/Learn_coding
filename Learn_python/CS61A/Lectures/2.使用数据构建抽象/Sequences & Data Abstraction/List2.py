import operator
#List Comprehensions
letters=['a','b','c','d','e','f','m','n','o','p']
print([letters[i] for i in [3,4,6,8]])
odds=[1,3,5,7,9]
print([x+1 for x in odds])
print([x+1 for x in odds if 25%x==0])

def divisors(n):
    return [1]+[x for x in range(2,n) if n%x==0]

#Strings
'curry = lambda f: lambda x: lambda y :f(x,y)'
exec('curry = lambda f: lambda x: lambda y :f(x,y)')#执行字符串中的命令

curry = lambda f: lambda x : lambda y : f(x,y)
add1=curry(operator.add)(1)

#simple-quoted and double-quoted strings are equivalent.
#\n

city='Berkeley'#Strings are Squences
print(len(city))
print(city[0])

# the "in" and "not in" operators match substrings
print('here' in 'Wheres Waldo?')#True----->String
print(234 in [1,2,3,4,5])#False----->List
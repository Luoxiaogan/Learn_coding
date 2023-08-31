#Dictionaries
numerals={'I':1, 'V':5, 'X':10}#没有顺序之分只有一一对应,unordered
print(numerals['X'])#10
#'X' is a key and 10 is the value
print(numerals.keys())#dict_keys(['I', 'V', 'X'])
print(numerals.values())#dict_values([1, 5, 10])
print(numerals.items())#dict_items([('I', 1), ('V', 5), ('X', 10)])
items=[('I', 1), ('V', 5), ('X', 10)]# A list
dict(items)#dict_items([('I', 1), ('V', 5), ('X', 10)])
dict(items)['X']#10
'X' in numerals# True
10 in numerals# False
numerals.get('X',0)#Return the value for key if key is in the dictionary, else default.
numerals.get('X',0)#10
numerals.get('X-Ray',0)#defailt 0

#Dictionaries Comprehension
squares={x:x*x for x in range(10)}

print({1:2, 1:3})#{1:3},tow keys cac't be equal!
print({1:[2,3]})
#Can't use lists and dictionaries as keys!!!
'''Bitwise Operators
& (AND)
|(OR)
^ (XOR)
~(NOT)
 << (left shift)
 >>(right shift)'''

'''Identity operators
Check if two reference point to the same object in memory.

is,is not

a=[1,2]
b=a
c=[1,2]
a is b #True
a is c #False
is not is an identity operator in python yhat checks whether
a=[1,2,3]
b=[1,2,3]

a==b  #True(same contents)
a is b #False(different objects)
a is not b #True (not the same object)

a is c #True (c references the same list as a)'''

'''Membership operators
 Test for membership in sequences like lists or string
     in,not in'''


'''Membership operators
in-present
not in -not present
list = [10,20,40]
'''

num=[10,20,30]
print(20 in num)
print(40 in num)

'''Identity Operators
is-same object
is not-different object
'''
n=10
m=10

print(n is m)
print(n is not m)

'''Ternary operators'''
#value_if_true condition else value_if_false

s=10
t=40
max = s if s>t else t
print(max)

'''LIST (MUTABLE,Ordered
collection of items inside ordered
(keeps sequence)
Mutable(Can change)'''


my_list=[10,20,30,40]

#List Operations
#1.Access Elements

print(my_list[0])
print(my_list[-2])

#2.slicing

print(my_list[1:3])


#3.Add Elements

my_list.append(50)
my_list.insert(2,15)

print(my_list)

#4.Remove Elements

my_list.remove(20)
my_list.pop()
del my_list[1]
print(my_list)

#5.Update Element

my_list[1]=100
print(my_list)


print(len(my_list))
my_list.sort()
print(my_list)



my_list.reverse()
print(my_list)


'''Tuple collection
inside ordered(keeps sequence)
immutable(cannot change)
'''


my_tuple=(10,10,10,20,30,40)

#1.Access
print(my_tuple[0])

#2.Slicing
print(my_tuple[1:3])

#3.Count and Index
print(my_tuple.count(10))#count occurance
print(my_tuple.index(20))#find index


#my_tuple[1]=100 # error(not allowed)

#3.SET(UNORDERED,UNIQUE VALUES)

'''what is a set?
collection of items inside{}
Unordered(keeps sequence)
NO duplicate values
'''

my_set={10,30,20,30,30,40,50}
print(my_set)

#set operators
#1.Add/Remove

my_set.add(50)
my_set.remove(20)
print(my_set)

#2.union(unique values)

a={1,2,3,4}
b={2,5,6,1}
print(a|b)

#3.Intersection(Common)
print(a & b)

#4.Difference
print(a-b)

#5 Symmetric Difference
print(a^b)

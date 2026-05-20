#Creating a set file
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))


my_empty_set = set()
print(type(my_empty_set))
print(my_empty_set)

lst = [1,1,1,2,2,3,4,5,6]
print(lst)
my_set = set([1,1,1,2,2,3,4,5,6])
print(my_set)


#Basic set operations
#Adding and removing
my_set.add(7)
print(my_set)
my_set.remove(3)
print(my_set)

#Discard means it will remove the items from the sets
my_set.discard(7)
print(my_set)

my_set.add(7)
print(my_set)

#pop method
poped  = my_set.pop()
print(poped)
print(my_set)

#clearing the set
my_set.clear()
print(my_set)

#Set Membership test
set = set([1,2,3,4,5])
print(3 in set)
print(10 in set)

#Methematical operators
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

#Union
union_set = set1.union(set2)
print(union_set)
intersection_set = set1.intersection(set2)
print(intersection_set)

#Difference
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
difference_set = set1.difference(set2)
print(difference_set)

## Sets Methods
set1={1,2,3,4,5}
set2={3,4,5}

## is subset
print(set2.issubset(set1))

print(set1.issuperset(set2))

#Counting unique words
text="In this tutorial we are discussing about sets In this tutorial we are discussing about sets"
words = text.split()
print(words)

Unique_words = set(words)
print(f"unique:{Unique_words}")
print(len(Unique_words))





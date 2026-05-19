## creating a tuple
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))


lst=list()
print(type(lst))
tpl=tuple()
print(type(tpl))


numbers = tuple([1,2,3,4])
print(numbers)

numbers = list((1,2,3,4))
print(numbers)


mixed_tuple = ([1,"Asmit",3.14,True])
print(mixed_tuple)


## Accessing Tuple Elements
print(numbers[2])
print(numbers[-2])


print(numbers[0:2])
print(numbers[::-1])
print(numbers[0:3:2])

## Tuple Operations

concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple)


print(mixed_tuple * 3)
print(numbers * 3)

## Immutable Nature Of Tuples
## Tuples are immutable, meaning their elements cannot be changed once assigned.

lst=[1,2,3,4,5]
print(lst)

lst[1]="Krish"
print(lst)


tpl=(1,2,3,4)
print(tpl)

'''tpl[3] = "Asmit"  ## Show Error Because Tuples are immutable
print(tpl)'''

## Tuple Methods
print(numbers.count(1))
print(numbers.index(3))

## Packing and Unpacking tuple
## packing
packed_tuple=1,"Hello",3.14
print(packed_tuple)

a,b,c = packed_tuple
print(a)
print(b)
print(c)


## Unpacking with *
numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(first)
print(middle)
print(last)


numbers_lst=[1,2,3,4,5,6]
numbers_tup=(1,2,3,4,5,6)
print(numbers_lst)
numbers_lst[2] = "py"
print(numbers_lst)


## Nested Tuple
## Nested List
lst=[[1,2,3,4],[6,7,8,9],[1,"Hello",3.14,"c"]]
lst[0][0:3]


nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))

## access the elements inside a tuple
# print(nested_tuple[0])
# print(nested_tuple[1][2])
nested_tuple[1][1:]

nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))
for i in nested_tuple:
    print("index" ,i )
    for j in i :
        print(j)






#Square all numbers in a list using map()
numbers = [1,2,3,4,5,6]
square = list(map(lambda x:x**2,numbers))
print(square)

#Convert all names to uppercase
names = ["asmit","kiran","virat"]
upper_case = list(map(lambda x:x.upper(),names))
print(upper_case)

#Add 10 to every number
numbers = [1,2,3,4]
result = list(map(lambda x:x + 10,numbers))
print(result)

#Find lengths of words
words = ["python","asmit","virat"]
len_words = list(map(lambda x:len(x),words))
print(len_words)


#Multiply two lists element-wise
lst1 = [2,4,6]
lst2 = [2,4,6]
multiply = list(map(lambda x,y:x*y,lst1,lst2))
print(multiply)

#Convert Celsius to Fahrenheit
celsius = [0,20,30,40]
c_f = list(map(lambda x:9/5*x+32,celsius))
print(c_f)

#Extract first character from each word
names = ["apple","orange","banana"]
extract = list(map(lambda x:x[0],names))
print(extract)

#Check even or odd
numbers = [20,30,27,45]
even_odd = list(map(lambda x:"Even" if x%2==0 else "odd",numbers))
print(even_odd)

#Remove spaces from strings
names = [" asmit "," virat "," sudeep "]
space = list(map(lambda x:x.strip(),names))
print(space)

#Cube of all numbers
numbers = [2,3,4,5]
cube = list(map(lambda x:x**3,numbers))
print(cube)



#Sort the following list based on the second element of each tuple.
numbers = [(1, 5), (2, 3), (4, 1), (3, 2)]
result = sorted(numbers,key = lambda x:x[1])
print(result)


#Extract only even numbers from the list.

numbers = [1,2,3,4,5,6,7,8,9,10]
result = list(map(lambda x:"Even" if x%2==0 else "odd",numbers))
print(result)

#Add corresponding elements from three lists
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
result = list(map(lambda x,y,z:x+y+z,a,b,c))
print(result)

#Sort the dictionary based on values
data = {"a":32,"b":31,"c":40}
result = sorted(data.items(),key = lambda x:x[1])
print(result)

#Convert all string numbers into integers
nums = ["1", "2", "3", "4"]

result = list(map(lambda x: int(x), nums))

print(result)

#Using map() and filter(), return squares greater than 10
numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x**2, numbers)

result = list(filter(lambda x: x > 10, squares))

print(result)

#Sort strings based on their length
words = ["python", "sql", "java", "datascience"]

result = sorted(words, key=lambda x: len(x))

print(result)

#Filter students scoring above 75.
students = [
    ("Asmit", 85),
    ("John", 70),
    ("Alice", 90)
]

result = list(filter(lambda x: x[1] > 75, students))

print(result)

#Reduce all product prices by 20%.
prices = [1000, 2000, 3000]

discounted = list(map(lambda x: x - (0.2 * x), prices))

print(discounted)
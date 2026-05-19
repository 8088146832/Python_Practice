''' kwargs stand for "keyword arguments"
The ** leta a function accept any number of named (keyword) argumenys
inside the function,kwargs treated like a dictionary.


JASON-Javascript Object Notation
it will be in key value pairs
student={
"name":"Alice"
"age":35
"city":"paris"
}
'''

'''def add(a,b):
    return a+b
a=int(input("Enter a:"))
b=int(input("Enter b:"))
result=add(a,b)
print("Addition:",result)'''


def greet(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")#JASON Value

greet(name="Alice",age=35,city="Paris")

a=10
b=40
add=(a+b)

print(f"Addition of {a} and {b} is:",add) # f is called formated string

'''
*args

*args stands foe "arguments"

The * allows a function to accept anu number of positional arguments

inside the function,args is treated like a tuple'''

def add_numbers(*args):
    print(args)
add_numbers(1,2,3,4)



'''Using Both together '''

def demo(*args,**kwargs):
    print("Args:",args)
    print("kwargs:",kwargs)
demo(1,2,name="Alice",age=35,city="Paris")
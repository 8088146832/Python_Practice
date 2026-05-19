'''Functions
function is a set of instructions to perform specific task
. It is a reusable code block.

syntax:
def function_name(parameter): #Function Defination
#return val

function_name(argument)  #Function Call
'''

def add(a,b):
    return a+b
result=add(3,4)
print("Addition:",result)

def add(a,b):
    return a+b
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
result=add(a,b)
print("Addition:",result)

def simple_intrest(p,t,r):
    si=(p*t*r)/100
    return si
principal=int(input("Enter principal Amount"))
time=int(input("Enter time"))
rate=int(input("Enter Interest"))
result=simple_intrest(principal,time,rate)
print("Interest is:",result)

def show_menu(): #Function without parameters
    print("1.show room")
    print("2.view room")
    print("3.Calculate bills")
show_menu()

'''def book_room(room_no,guest_name="Viraj",room_type="deluxe"):
    return f"Room {room_no}({room_type}) booked for {guest_name}"

print(book_room(101))
print(book_room(201,"jhon","suite"))'''

#function
'''def calc_sum(a,b):
    return a+b

sum=calc_sum(1,2)
print(sum)'''

####
'''def print_hello():
    print("hello python")

print_hello()'''

###
'''def avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

avg(20,30,40)'''

#program
'''cities = ["bengaluru","hyderabad","mumbai","Delhi","rajastan"]
heros = ["thor","hanuman","shaktiman","ironman"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heros)'''

#program
'''heros = ["thor","hanuman","shaktiman","ironman"]
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(heros)'''

#program
'''def fact_n(n):
    fact = 1
    for i in range (1,n+1):
        fact *= i
    print(fact)
fact_n(3)'''

#program
'''def usd_inr(usd):
    inr = usd * 83
    print(usd,"USD =",inr,"INR")
usd_inr(100)'''

#program
'''def input_num(n):
    return n % 2 == 0
result1 = input_num(9)
result2 = input_num(8)
print("EVEN:",result1)
print("ODD:",result2)'''

#program
'''def greet(name="Guest"):
    return f"Hello, {name}"

print(greet())
print(greet("Asmit"))'''



























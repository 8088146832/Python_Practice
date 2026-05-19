#Error handling program
#program1
'''print("---ZeroDivisionError---")
try:
    a=int(input("Enter Numerator"))
    b=int(input("Enter denominator"))
    result=a/b
    print("Division result:",result)
except ZeroDivisionError:
    print("Error:Cannot Divisible by zero")
finally:
    print("Program ended successfully")'''

#program 2
'''print("---ValueError Demo---")
try:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    print("You entered:",a,b)
except ValueError:
    print("Invalid input!,type numbers only")
finally:
    print("program ended successfully")'''

#program 3
'''print("---IndexError Demo---")
try:
    lst=[1,2,3]
    index=int(input("Enter list element (0-2)"))
    print("accessing list element is:",lst[index])
except:
    print("Error:list element is out of range")
finally:
    print("program ended successfully")'''

#PRACTICE PROGRAMS
#program 4

'''def arithametic(a,b):
    return a+b,a-b,a*b,a/b
a=int(input("Enter a"))
b=int(input("Enter b"))
result = arithametic(a,b)
print("Addition,Sustraction,Multiplication,Division:",result)'''

#program 5
'''def largest(a,b,c):
    return a>b>c
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
if a>b and a>c:
    print("largest number is:",a)
elif b>a and b>c:
    print("largest number is:",b)
elif c>a and c>b:
    print("largest number is:",c)
else:
    print("invalid output!")'''

#program 6
'''def largest(a,b,c):
    return max(a,b,c)
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
result=largest(a,b,c)
print("largest number is:",result)'''

#program 7
'''def calc_bills(a,b):
    return a*b
a=int(input("enter number of days"))
b=2000
result=calc_bills(a,b)
print("total bill is:",result)'''

#program 8
'''print("---ZeroDivisionError---")
try:
    a=int(input("Enter numerator"))
    b=int(input("Enter denominator"))
    result=a/b
    print("Division Result:",result)
except ZeroDivisionError:
    print("a number cannot be divisible by zero")
finally:
    print("program ended safely")

print("---ValueError---")
try:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    print("you entered:",a,b)
except ValueError:
    print("type only number")
finally:
    print("program ended safely")

print("---IndexError---")
try:
    lst=[1,2,3]
    index=int(input("Enter list index (0-2):"))
    print("Accessing list element:",lst[index])
except IndexError:
    print("Error:number is out of range")
finally:
    print("program ended safely")'''



'''#program 8
class AgeError(Exception):
    pass
try:
    age=int(input("Enter your age."))
    if age < 18:
        raise AgeError("Age must be above 18.")
    print("Access granted,you can vote")
except AgeError as e:
    print("Custom Error:",e)
finally:
    print("program ended safely")

#program 9

class WeakPasswordError(Exception):
    pass
try:
    password=input("enter your password.")
    if len(password) < 8:
        raise WeakPasswordError("password must be atleast 8 characters long")
    print("access granted,password valid")
except WeakPasswordError as e:
    print("Custom Error:",e)
finally:
    print("program ended safely")
    
#program 10

class CheckBalanceError(Exception):
    pass
try:
    balance=10000
    amount=int(input("Enter your amount to withdraw"))
    if amount > balance:
        raise CheckBalanceError("Insufficient fund!")
    print("Amount withdrawn safely")
    balance-=amount
    print("Your current balance is:",balance)
except CheckBalanceError as e:
    print("Custom Error:",e)
finally:
    print("program ended safely")'''

#PRACTICE PROGRAMS
#program 1

'''r=float(input("Enter radius"))
area=3.14 * r * r
print("Area of circle is:",area)'''

#program 2
'''c=float(input("Enter temperature"))
f=(c*9/5)+32
print("celcious to farenhate is:",f)'''

#program 3
'''km=float(input("Enter kilometers:"))
meters=km*1000
print("km in meter:",meters)'''

#program 4
'''a=int(input("Enter a:"))
b=int(input("Enter b:"))
a,b=b,a
print("After swaping:",a,b)'''

#program 5
'''num=int(input("Enter a number:"))
if num > 0:
    print("positive number")
elif num < 0:
    print("Negative number")
else:
    print("zero")'''

#program 7
'''num=int(input("Enter a number:"))
if num % 5 == 0 and num % 11 == 0:
    print("number divisible by 5 and 11")
else:
    print("not divisible")'''

#program 6,15,16,17,20 doubt

#/////////////////////////////////////////////
#program 1
'''class Student:
    name = "Asmit"
    age = 25
s1 = Student()
print(s1.name)
print(s1.age)'''

#program 2
'''class employee:
    empname = "Asmit"
    empid = 123
    empsalary = 60000
e1=employee()
print(e1.empname)
print(e1.empid)
print(e1.empsalary)'''

#program 3
'''class Student:
    def setdata(self,name,age):
        self.name = name
        self.age = age
    def showdata(self):
        print(self.name)
        print(self.age)
s1=Student()
s1.setdata("ravi",21)
s1.showdata()'''

#program 4

'''class Student:
    def setdata(self,name,age):
        self.name = name
        self.age = age
    def check_age(self):
        if self.age >= 18:
            print("eligible")
        else:
            print("not eligible")
    def showdata(self):
        print(self.name)
        print(self.age)
s1=Student()
s1.setdata("package",32)
s1.showdata()
s1.check_age()'''

#program 5
'''class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,self.age)
s1=Student("package",21)
s1.show()'''

#program 6
'''class Student:
    def setdata(self,name,marks):
        self.name=name
        self.marks=marks
    def showdata(self):
        print(self.name)
        print(self.marks)
    def check_passfail(self):
        if self.marks >=36:
            print("ravi is pass")
        else:
            print("ravi is fail")
s1=Student()
s1.setdata("ravi",12)
s1.showdata()
s1.check_passfail()'''

#program 7
'''class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
    def check_age(self):
        if self.age >= 18:
            print("Asmit is can vote")
        else:
            print("Asmit cannot vote")
s1=Student("Asmit",36)
s1.show()
s1.check_age()'''


#program 8
'''class Employee:
    def __init__(self,name,worktime):
        self.name=name
        self.worktime=worktime
    def show(self):
        print(self.name,self.worktime)
    def emp_bonus(self):
        if self.worktime > 10:
            print("bonus added")
        else:
            print("bonus not added")
e1=Employee("Asmit",15)
e1.show()
e1.emp_bonus()'''

#program 9
'''class Student:
    def setdata(self,name,marks):
        self.name=name
        self.marks=marks
    def showdata(self):
        print(self.name)
        print(self.marks)
    def check_grade(self):
        if self.marks > 90:
            print("Raju obtained 'A' grade")
        elif self.marks > 50:
            print("Raju obtained 'B' grade")
        elif self.marks > 36:
            print("C")
        else:
            print("fail")
s1=Student()
s1.setdata("Raju",25)
s1.showdata()
s1.check_grade()'''

#program
'''class Student:
    def __init__(self,name):
        self.name=name
        print(self.name)
s1 = Student("Asmit")'''


#program
'''class Student:
    def show(self):
        print("this is method")
s1 = Student()
s1.show()'''

#program
'''class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        print("Account created successfully")
    def deposite(self,amount):
        self.amount=amount
        print("Amount credited successfully:",amount)
b1 = BankAccount("Asmit",100)
b1.deposite(1000)'''

#program

'''class DataAnalysis:
    def __init__(self,data):
        self.data = data
    def average(self):
        return sum(self.data)/len(self.data)
    def maximum(self):
        return max(self.data)
    def minimum(self):
        return min(self.data)
    def summary(self):
        print("Data:",self.data)
        print("Maximum:",self.maximum())
        print("Minimum:",self.minimum())
        print("Average:",self.average())
marks = [89,90,95,99]
d1 = DataAnalysis(marks)
d1.summary()'''

#program
'''class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("package",21)
print(s1.name,s1.age)'''

#program
'''class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
s1=student("Asmit",21)
s1.display()'''

#program

'''class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1=student("package",21)
s1.display()'''

#program
'''class car:
    def __init__(self,brand,colour="White"):
        self.brand=brand
        self.colour=colour
c1=car("BMW")
print(c1.brand,c1.colour)'''

#program

'''class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
r1=rectangle(6,2)
print("Area:",r1.area())'''

#program
'''class evenodd:
    def __init__(self,num):
        self.num=num
    def check(self):
        if self.num % 2 == 0:
            print("Even")
        else:
            print("odd")
e1=evenodd(20)
e1.check()'''


#program
'''class student:
    def setdata(self,name,marks):
        self.name=name
        self.marks=marks
    def showdata(self):
        print(self.name)
        print(self.marks)
s1=student()
s1.setdata("package",95)
s1.showdata()'''

#program
'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show(self):
        print("Name:",self.name,"Marks:",self.marks)
s1=Student("package",94)
s1.show()'''

#program
'''class Car:
    def __init__(self,brand,colour="White"):
        self.brand=brand
        self.colour=colour
    def display(self):
        print(f"Brand:",self.brand,"Colour:",self.colour)
c1=Car("BMW")
c1.display()'''

#program
'''class Employee:
    company = "Google"
    company2 = "TCs"
    def __init__(self,name):
        self.name=name
e1=Employee("Asmit")
e2=Employee("Bhargav")
print("Asmit:",e1.company,"Bhargav:",e2.company2)'''

#program
'''class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def apply_discount(self,percent):
        self.price-=self.price * percent
l=Laptop("Acer",50000)
l.apply_discount(10)
print(l.price)'''

#program
'''name = "Hello Python!"
print(name)'''

#program
'''a=input("Enter your name:")
print("Welcome To RCB Camp:",a)'''


#program
'''a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
result=a+b
print("Addition of two number is:",result)'''

#program
'''def A_of_R(l,b):
    return l*b
result = A_of_R(20,10)
print("Area of rectangle is:",result)'''

#program
'''def C_to_F(celsius):
    return (celsius * 9/5) + 32
temp=float(input("Enter temperature in celsius:"))
result=C_to_F(temp)
print("Temperature in farenhate is:",result)'''


#program
'''a=int(input("Enter a number:2"))
result1=a*a
result2=a*a*a
print("Square of number is:",result1)
print("Cube of number is:",result2)'''


#program
'''a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a > b:
    print("Number is largest:",a)
else:
    print("Number is largest:",b)'''

#ASSIGNMENT QUESTIONS
#program-1
'''print("Hello Python!")'''

#program-2
'''name=input("Enter your name:")
print("Welcome to RCB camp:",name)'''

#program-3
'''a=int(input("Enter a number:"))
b=int(input("Enter second number:"))
result=a+b
print("Addition:",result)'''

#program-4
'''length=float(input("Enter a number:"))
breadth=float(input("Enter a number:"))
result=length * breadth
print("Area of rectangle is:",result)'''

#program-5
'''celsius=float(input("Enter temperature in celsius:"))
farenhate = (celsius * 9/5) + 32
print("Temperature in farenhate is:",farenhate)'''

#program-6
'''x,y = 1,8
x,y = y,x
print(x,y)'''

#program-7
'''a=int(input("Enter a number:"))
result1=a*a
result2=a*a*a
print("given number square is:",result1)
print("given number cube is:",result2)'''

#program-8
'''a=int(input("enter a number:"))
if a % 2 == 0:
    print("Even number")
else:
    print("odd number")'''

#program-9
'''a=int(input("Enter a number:"))
b=int(input("Enter second number:"))
if a > b:
    print("Largest number is:",a)
else:
    print("Largest number is:",b)'''

#program-10
'''p=float(input("Enter principal amount:"))
t=float(input("Enter time:"))
r=float(input("Enter intrest amount:"))
si=(p*t*r)/100
print("Simple intrest is:",si)'''


#program-11
'''a=int(input("Enter a number:"))
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")'''

#program-12
'''a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>b and a>c:
    print("greater number:",a)
elif b>a and b>c:
    print("greater number:",b)
else:
    print("greater number:",c)'''

#program-13
'''n=int(input("Enter a number:"))
if n % 5 == 0 and n % 11 == 0:
    print("Number divisible by 5 and 11")
else:
    print("not divisible by 5 and 11")'''

#program-14
'''year=int(input("type year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("not leap year")'''

#program-15

'''a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
op=input("Enter operator:")
if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
else:
    print(a/b)'''

#program-16

'''o_c=input("Enter alfhabet")
if o_c in 'aeiou':
    print("ovels")
else:
    print("conconents")'''

#program-17

'''marks=int(input("Enter marks:"))
if marks > 90:
    print("A")
elif marks > 75:
    print("B")
else:
    print("c")'''

#program-18

'''n = input("Enter number: ")
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")'''

#program-20
'''cp=float(input("Enter cost price:"))
sp=float(input("Enter selling price:"))
if sp > cp:
    profit = sp - cp
    print("Profit %:",(profit/cp)*100)
else:
    profit = cp - sp
    print("profit:",(profit/cp)*100)'''

#program-21

'''cp=float(input("Enter cost price:"))
sp=float(input("Enter selling price:"))
if sp > cp:
    profit = sp - cp
    print("Profit %:",profit)
else:
    profit = cp - sp
    print("profit:",profit)'''

#program-22
'''n = int(input("Enter n: "))
print("Sum =", n * (n + 1) // 2)'''

#program-23
'''a=int(input("Enter a number:"))
for i in range (1,11):
    print(a,'x',i,'=',a*i)'''

#program-24
'''n=int(input("Enter a number:"))
fact = 1
for i in range (1,n+1):
    fact *= i
print("Factorial =",fact)'''


#program-25
'''n = int(input("Enter number: "))
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n //= 10
print("reverse:",rev)'''



#program-27
'''n=input("Enter string:")
print(n[::-1])'''

#program-28
'''s = input("Enter string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")'''

#program

'''def add(a,b):
    return a+b
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
result = add(a,b)
print("Addition:",result)'''

#program
'''def check_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(check_prime(2))'''

#program

'''def find_fact(n):
    fact = 1
    for i in range (1,n+1):
        fact *= i
    print(fact)
find_fact(3)'''

#program

'''d = {"b": 2, "a": 1, "c": 3}

sorted_dict = dict(sorted(d.items()))
print(sorted_dict)


#program

d = {"a": 10, "b": 25, "c": 15}

max_value = max(d.values())
print("Highest value:", max_value)


with open("file.txt", "w") as f:
    f.write("Hello, this is a sample file.\nWelcome to Python file handling.")

with open("file.txt", "r") as f:
    content = f.read()
    print(content)

with open("file.txt", "r") as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))

with open("file.txt", "r") as f:
    content = f.read()
    words = content.split()
    print("Number of words:", len(words))

with open("file.txt", "r") as f:
    content = f.read()
    print("Number of characters:", len(content))

with open("file.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())'''


'''def is_palindrome(s):
    s = str(s)

    if s == s[::-1]:
        return "palindrome"
    else:
        return "not palindrome"

s = input("Enter a string:")
result = is_palindrome(s)
print(result)'''

'''string = input("Enter your name:")
if string in 'aeiou':
    print("ovels")
else:
    print("consonents")'''

s=input("Enter string:")
vowels="aeiou AEIOU"
v_count = c_count = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v_count+=1
        else:
            c_count+=1
print("Vowels:",v_count)
print("consonents:",c_count)

numbers = [1,2,3,4,4,4,3,2]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency










































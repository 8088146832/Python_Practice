'''Conditional statements
if
_____________
Syntax
if condition
#statement block

if else
_________
syntax
if condition:
#statement block
 else:
 #statement block

 if else
 _________
 syntax
 if condition1:
 #statement block
 elif condition2:
 #statement block
 else:
 #statement block
 '''
age = 32
if age > 18:
    print("Adult")

if age > 18:
    print("adult")
else:
    print("minor")

age = int(input("Enter your age"))
if age > 18:
    print("Adult")

if age > 18:
    print("adult")
else:
    print("minor")



marks=int(input("Enter your marks"))
if marks >= 85:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("f")


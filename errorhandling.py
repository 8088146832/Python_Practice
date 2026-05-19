'''Error Handling
error handling in python is done using exceptions,exception allow
a program to handle runtime errors gracefully instead of crashing

python mainly use the following key words

1.try
2.except
3.else
4.finally
5.raise

syntax

try:
#code that may cause an error

except:

#code that runs if error occurs
'''
#program
'''try:
    a=10
    b=0
    c=a/b
    print(c)
except:
    print("Error Ocurred")'''

#program
print("----ZeroDivisionError----")
try:
    x=int(input("Enter numerator"))
    y=int(input("Enter denominator"))
    result = x/y
    print("Division Result:",result)
except ZeroDivisionError:
    print("Error:Cannot divide by zero")
finally:
    print("program ended safely")

#program

print("---ValueError Demo---")
try:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    print("You entered:",a,b)
except ValueError:
    print("Error:Invalid input! Please enter numbers only")
finally:
    print("program ended safely")


#program
print("---IndexError Demo---")
try:
    lst = [10,20,30]
    index = int(input("Enter list index (0-2):"))
    print("Accessing list element:",lst[index])
except IndexError:
    print("Error: List index out of range")
finally:
    print("program ended safely")

#CUSTOM EXCEPTIONS
#program
class AgeError(Exception):
    pass
print("---Custom AgeError Demo---")
try:
    age = int(input("Enter your age:"))
    if age < 18:
        raise AgeError("Age must be 18 or above to continue.")
    print("Access granted.Age is valid.")
except AgeError as e:
    print("Custom Error:",e)
finally:
    print("program ended successfully.")

#program

class WeakPasswordError(Exception):
    pass
try:
    password=input("Enter your password.")
    if len(password)<8:
        raise WeakPasswordError("password must be atleast 8 character")
    print("Access granted.password is valid.")
except WeakPasswordError as e:
    print("Custom Error:",e)
finally:
    print("program ended successfully")


#program
amount=float(input("Enter amount to withdraw"))
class BalanceError(Exception):
    pass
try:
    balance = 5000
    if amount > balance:
        raise BalanceError("Insufficient fund!")
    print("Amount withdraw successfully")
    balance-=amount
    print("Current balance is:",balance)
except BalanceError as e:
    print("Custom Error:",e)
finally:
    print("program ended successfully")





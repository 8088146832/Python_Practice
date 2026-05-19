try:
    result=1/0
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")

try:
    result=1/2
    a=b
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than zero")
except Exception as ex1:
    print(ex1)
    print("Main Exception got caught here")

try:
    a=b
except NameError as ex:
    print(ex)

try:
    result=1/0
except ZeroDivisionError as ex:
    print(ex)
    print("Denominator should greater than 0")


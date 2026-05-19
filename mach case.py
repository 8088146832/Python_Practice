'''
Match case:
match expression:
case pattern1:
#statement block
case pattern2:
#statement block
case pattern3:
#default pattern'''

operator = input("Enter operator(+,-,*,/)")
x=int(input("Enter x"))
y=int(input("Enter y"))
match operator:
    case'+':
        result = x+y
    case'-':
        result = x-y
    case'*':
        result = x*y
    case'/':
        result = x/y

print(result)

num = int(input("Enter number"))
if num>0:
    print("positive")
else:
    print("negative")


num = int(input("Enter number"))
if num % 2 == 0:
    print("even")
else:
    print("odd")
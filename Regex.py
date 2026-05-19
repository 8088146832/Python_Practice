# '''Regular Expression are used to search,match and manipulate text patterns'''
#
# '''Comman regex pattern
# 1.Character Classes
# Escape sequences(\d,\s,\w,\.)
#
# \d - digit(0-9)
# \w - word(a-z,A-Z,0-9)
# \s - whitespace
# ^ - start of string
# $ - end of string
# \. - it will print .
#
# 2.Custom patterns
# [abc] - matches a,b or c
# [a-z] - lowercase
# [A-Z] - uppercase
#
# 3.Quantifiers
#
#
# + - 1 or more
# * - 0 or more
# . - any character
#
# when to use Regex?
# use regex when you want to:
# validate input(email,password)
# Extract data(numbers,URLs)
# clean text data
# search patterns in logs/files
# '''
#1
import re

'''re.match() checks only at the biggning
of the string'''

text="Programming Python programming"

result=re.match("Programming",text)

if result:
    print("Match Found")
else:
    print("NO match")


#2
'''search function
re.search() checks
anywhere in the string'''


text="Python Programming"

result=re.search("Programming",text)

if result:
    print("Match found")
else:
    print("No match")

#3
'''re.sub() is used to replace text'''

text="Python programming"

result=re.sub("Python","Java",text)
print(result)

#4
'''re.split() splits a string based on pattern'''

text="apple,banana,orange"
result=re.split(",",text)
print(result)


text="My phone number is 215-555-7777"
result=re.sub(r'\d','*',text)
print(result)

import re
email = input("Enter Email Address: ")
pattern=r'^\w+@\w+\.\w+$'
result = re.match(pattern,email)
if result:
    print("valid Email")
else:
    print("invalid Email")

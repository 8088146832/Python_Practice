'''1.For loop
for variable in sequence:
    #statement block

2.While Loop
while condition:
    #statement block
'''
for i in range(1,5):
    print(i)


i=1
while i<=5:
    print(i)
    i+=1


fruits=["apple","banana","orange"] #for(i=0,i<n,i++)
for fruit in fruits:
    print(fruit)


fruits=["apple"]
for fruit in fruits:
    print(fruit)



for i in range (1,6):
    if i == 3:
        break
    print(i)

for i in range (1,6):
    if i == 3:
        continue
    print(i)

for i in range (1,6):
    if i == 3:
        pass
    print(i)


i=1
while i<= 10:
    if i == 5:
        break
    print(i)
    i+=1

i=2
while i<= 10:
    if i==4:
        continue
    print(i)
    i+=1


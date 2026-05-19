#creating a list
lst=[]
print(type(lst))

names = ["Asmit","bob","Ram",1,2,3,4]
print(names)

mixed_lst = ["Asmit",1,3.14,True]
print(mixed_lst)

#Accessing List Elements
fruits = ["Apple","Banana","Watermelon","Grapes","Guava","Mango"]
print(fruits)

#One Element
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
print(fruits[5])
print(fruits[-2])

#slicing
print(fruits[1:])
print(fruits[::-1])
print(fruits[0:5:2])


#Modifying the list elements
fruits[4]="Orange"
print(fruits)

#List Methods
fruits = ["Apple","Banana","Watermelon","Grapes","Guava","Mango"]
fruits.append("orange")
print(fruits)

fruits.insert(1,"Banana")
print(fruits)

fruits.remove("Banana")
print(fruits)

#Pop function
pop_fruits = fruits.pop()
print(pop_fruits)
print(fruits)

index = fruits.index("Watermelon")
print(index)

fruits.insert(1,"Banana")
print(fruits)

count = fruits.count("Banana")
print(count)

fruits.remove("Banana")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.clear()
print(fruits)

# Slicing List
numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])

print(numbers[::3])

print(numbers[::-2])

### Iterating Over List
numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in list:
    # print(i)
for number in numbers:
    print(number)


fruits=["apple","banana","cherry","kiwi","gauva"]
for fruit in fruits:
    print(fruit)

print(len(fruits))

for i in range(0,len(fruits)):
    print("index",i)
    print(fruits[i])

lst = []
for i in range (0,20):
    if i%2==0:
        lst.append(i)
        print("interation",i,lst)

lst_2 = [x**2 for x in range (10)]
print(lst_2)

lst_3 = [x*2 for x in range (20)]
print(lst_3)

### Basic List Comphrension

sqaure=[num**2 for num in range(10)]
print(sqaure)

### List Comprehension with Condition
lst = []
for i in range(10):
    if i % 2 == 0:
        lst.append(i)

print(lst)


even_numbers = [num for num in range(10) if num%2==0]
print(even_numbers)

## Nested List Comphrension

lst1=[1,2,3,4]
lst2=['a','b','c','d']

pair=[[i,j] for i in lst1 for j in lst2]

print(pair)


marks = [60,70,80,96]
subject = ["Kan","eng","mat","sci"]
pair = [[i,j] for i in marks for j in subject]
print(pair)
for i in pair:
    print(i)

#Examples of lists

to_do_list=["Buy Groceries","Clean the house","Pay bills"]
## Adding to task
to_do_list.append("Shedule Meeting")
to_do_list.append("Go for a run")

## Removing a completed task
to_do_list.remove("Clean the house")

## Checking if the task is in the list
if "Pay bills" in  to_do_list:
    print("Dont forget to pay the bills")
print("The remaining tasks are:")
for task in to_do_list:
    print(f"-{task}")



# Organizing student grades
grades = [85, 92, 78, 90, 88]

# Adding a new grade
grades.append(95)

# Calculating the average grade
average_grade = sum(grades) / len(grades)
print(f"Average Grade: {average_grade}")

# Finding the highest and lowest grades
highest_grade = max(grades)
lowest_grade = min(grades)
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")


# Managing an inventory
inventory = ["apples", "bananas", "oranges", "grapes"]

# Adding a new item
inventory.append("strawberries")

# Removing an item that is out of stock
inventory.remove("bananas")

# Checking if an item is in stock
item = "oranges"
if item in inventory:
    print(f"{item} are in stock.")
else:
    print(f"{item} are out of stock.")

# Printing the inventory
print("Inventory List:")
for item in inventory:
    print(f"- {item}")


# Collecting user feedback
feedback = ["Great service!", "Very satisfied", "Could be better", "Excellent experience"]

# Adding new feedback
feedback.append("Not happy with the service")

# Counting specific feedback
positive_feedback_count = sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())
print(f"Positive Feedback Count: {positive_feedback_count}")

# Printing all feedback
print("User Feedback:")
for comment in feedback:
    print(f"- {comment}")



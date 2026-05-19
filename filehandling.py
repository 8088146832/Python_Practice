'''File handling in python is used to create,read,write,append and manage

File handling allow you to:


store data permanently
read data from file
write or update data
append data to file

example:saving student records,logs,reports

file=open("filename.text","modes")

file modes

r-Read(default)
w-Write(create new)
a-append
x-create new file
b-binary mode
t-text mode(default)
r+ - Read+Write'''

'''file = open("data1.txt","w")
file.write("Rahul")
file.write("Rohan")
file.write("Raju")

file.close()

print("Data Written successfully")'''


'''with open ("students.txt","w") as file:
    file.write("John,22\n")
    file.write("Mary,21\n")
    file.write("Alice,23\n")
    file.write("Bob,24\n")'''

'''with open ("students.txt","r") as file:
    print("File Data:")
    print(file.read())'''

#append
'''with open ("students.txt","a") as file:
    file.write("rahul,22\n")'''
###
'''with open ("students.txt","r") as file:
    print("File Data")
    print(file.read())'''


def add_student():
    name=input("Enter Student Name:")
    age=input("Enter Student Age:")

    with open ("students.txt","a") as file:
        file.write(name+","+age+"\n")
    print("Student Added Successfully")

#.View Student
def View_student():
  try:
    with open("students.txt","r") as file:
        data=file.readlines()
        if not data:
            print("Student not found")
            return
        print("\n Student Records:")
        for line in data:
            name,age = line.strip().split(",")
            print(f"Name:{name},{age}")
  except FileNotFoundError:
      print("File Not Found")



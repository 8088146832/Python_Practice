'''Class and objects
class is a template or blueprint of an object to create an objects
it defins attribute (variables) and methods(function)
that the object created from it will have

syntax of class:
class ClassName:
#attributes
#methods


class Student:
    name="ABC"
    age=22

Objects:is an instance of class.
it represents a real world entity

syntax to create objects

object name=ClassName()
'''


#program 1
'''class Student:
    name="ABC"
    age=22  #variables or attributes

s1=Student()
print(s1.name)
print(s1.age)'''


#program 2
'''class Employee:
    EmployID=123
    EmpSalary=50000
    EmpName="Asmit"
e1=Employee()
print(e1.EmployID)
print(e1.EmpSalary)
print(e1.EmpName)'''

#program 3

'''class Student:
    def setdata(self,name,age):  #if we use function in class is called method
        self.name = name
        self.age = age
    def showdata(self):
        print(self.name)
        print(self.age)
s1=Student()
s1.setdata("Ravi",32)
s1.showdata()'''

#program 4
'''class Employee:
    def setdata(self,Empsalary,Empname):
        self.Empsalary = Empsalary
        self.Empname = Empname
    def showdata(self):
        print(self.Empsalary)
        print(self.Empname)
e1=Employee()
e1.setdata(20000,"Asmit")
e1.showdata()'''
a

#program 6
'''class Student:
    def setdata(self,name,age):  #if we use function in class is called method
        self.name = name
        self.age = age
    def check_vote(self):
        if self.age > 18:
            print("Ravi,can vote")
        else:
            print("Ravi,cannot vote")
    def showdata(self):
        print(self.name)
        print(self.age)
s1=Student()
s1.setdata("Ravi",32)
s1.showdata()
s1.check_vote()'''

#program 7

'''Constructors: is a special function.It runs autometically when the object is created'''

'''class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name,self.age)

s1=student("ABC",32)
s1.show()'''

#Difference between constructor and methods
''' Feature                 constructor                    method

1.Definition          special function used to      Normal function inside class
                     initialize object

2.Name                 Always__init__()              Any name eg:display(),show(),...


3.purpose              Initialize object data        Perform Operators/Action


4.Execution            Automatically called when     Called manually using object
                        object is created

5.Return type            No Return value              can return value


6.Syntax                  def__init__()              def method_name(self) '''


#constructor
'''class Student:
    def __init__(self,name):
        self.name = name
        print(self.name)
s1 = Student("Ravi")'''

#method
'''class Student:
    def show(self):
        print("This is a method")
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
        print("Account deposited succesfully",amount)
b1 = BankAccount("Ravi",100)
b1.deposite(1000)'''

#program
'''class DataAnalysis:
    def __init__(self,data):
        self.data=data
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
marks=[84,90,78,93,88]
analysis=DataAnalysis(marks)
analysis.summary()'''


#program
'''class Rectangular:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def calculate(self):
        result=(self.length*self.bredth,2*self.length*self.bredth)
        print("Area and Perimeter of rectangular:",result)
r1=Rectangular(40,10)
r1.calculate()'''








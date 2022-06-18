#Abstract Classes

from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def get_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary
    
#For Multiple Inheritance
    
class Person1:
        
    def name(self):
        return("****"+"Shivam Singh"+"****")

class Person2:
   
    def name(self):       
        return("####"+"Shivam Singh"+"####")

class Person(Person2,Person1):
    # print('working')
    def name(self):
        return super(Person,self).name()
    
#decorator 
def check_divisor(func):
    def inner(a,b):
        if b==0:
            return "Divison by zero is not possible."
        return func(a,b)
    return inner


@check_divisor
def divide(a,b):
    return a/b

print("Abstract class Example")
full_time = FulltimeEmployee('Shivam', 'Singh',"15")
print("Expected Salary of ",f"{full_time.full_name} is",full_time.get_salary()+"Lakh") 

print("Multiple Inheritance Example")      
obj=Person()
print(obj.name())

print( "Decorator Example")
print(divide(4,5))
print(divide(40,0))
from inspect import trace
from pickle import FALSE
from TestManager import TestManagers

class Person:
    def __init__(self, first_name, last_name,age,license):
        self.first_name = first_name
        self.last_name1 = last_name
        self.age = age
        self.license = license
    
    ##

    @property
    def is_license(self):
        print("call is_license")
        return self.license

    # @property
    # def age(self):
    #     return self._age

    # @age.setter
    # def age(self,age):
    #     if(age<0):
    #         raise ValueError("invalid age")
    #     self._age = age

        


def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')    
    return wrapper

    
@trace
def hello():
    print('hello')
    return 1

@trace
def world():
    print('world')


def testNum():    
    return 2


# person = Person("good", "vega", 30,False)
# print(person.is_license)
# person.is_license = True
# print(person.is_license)

# def startEnd(func):
#     def wrapper():
#         print("시작")
#         func()
#         print("끝")        
#     return wrapper
    


# @startEnd
# def say_hello():
#     print('hello')

# @startEnd
# def say_hi():
#     print('hi')

# say_hello()
# say_hi()


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@naver.com'

    @property
    def email(self):
        return self.first + '.' + self.last + '@naver.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    objects = TestManagers()

emp1 = Employee('John', 'Smith')
emp1.fullname = 'Corey Schafer'

#emp1.objects.TestFunc()

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
emp1.fullname = 'holy shit'
print(emp1.email)
    

    # def printemail(self):
    #     return f'{self.first}' + '.' + f'{self.last}' + '@naver.com'

# emp1 = Employee('john', 'smith')

# emp1.first = 'kim'

# print(emp1.first)
# print(emp1.email)
# print(emp1.fullname())

# print(emp1.printemail())
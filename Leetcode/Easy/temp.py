'''
for randam use
'''

# def Sum(x,y):
#     return x+y
# print(Sum(5,10))

# def what():
#     def up():
#         return "hi"
#     return up()
# whatsUp = what()
# print(whatsUp)

# def mynum(a):
#     return a + 2
# def num(b):
#     newVal=10
#     return b(newVal)
# print(num(mynum))

# def num(a=10,*numbers,**phonebook):
#     print("a=",a)
#     for i in numbers:
#         print(i)
#     for j,k in phonebook.items():
#         print(j,k)
# num(10,4,5,6,7,deep=21,sharan=21,aaryen=21)

# class Instructor:
#     companyName = "bluelime"
#     def __init__(self,course):
#         self.course = course
#     def company(self):
#         print("company name=",Instructor.companyName)
# obj = Instructor("Hello")
# obj.company()  

  
    
# class India():
#     def cap(self):
#         print("Delhi is the capital of India")
#     def lang(self):
#         print("Hindi is the primary language")
# class America():
#     def cap(self):
#         print("Washington D.C. is the capital of USA")
#     def lang(self):
#         print("English is the primary language")
        
# rupees = India()
# dollars = America()
# rupees.cap()
# rupees.lang()
# dollars.cap()
# dollars.lang()

# for world in rupees, dollars:
#     world.cap()
#     world.lang()
    
    
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class square(shape):
    def __init__(self,side):
        self.__side = side
    def area(self):
        return self.__side*self.__side
    def perimeter(self):
        return 4*self.__side
myans=square(5)
print(myans.area())
print(myans.perimeter())

#day 12 will cover classes in Python
#It is a simple class program in which myfunc() is an object method

print("Wel-Come to Day 12 of 21 Days Programming Challenge")
class Person:                 # initializing class
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):         #defining method
    print("Hello my name is " + self.name)

p1 = Person("John", 36)  
p1.myfunc()           #calling class method
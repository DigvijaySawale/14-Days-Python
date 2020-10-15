#day 11 will cover functions in python

print("Wel-Come to Day 11 of 21 Days Programming Chalenge\n")
def fun1() :
    print("This is function with no arguments\n")              #function with no arguments
    

def fun2(name):    #function with 1 argument
    print("This is function with 1 arguments")
    print("Hello",name,"\n")

def fun3(fname,lname):        #function with 2 arguments
    print("This is function with 2 arguments")
    print("Hello",fname,lname,"\n")

def fun4(name = "Digvijay"):  #function with default parameter
    print("This is function with default parameter")
    print("Hello",name,"\n")

def fun5(food):     #passing list as an argument to function
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

def fun6(x):          ##function with return statements
    return x*5

#calling functions
fun1()
fun2(input("Enter name: "))
fun3(input("Enter first name: "),input("Enter last name: "))
fun4("Ram")
fun4()
fun5(fruits)
print(fun6(3))
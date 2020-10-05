# day 1 will cover the basics of python
# personal information

print("Wel-Come to day 1 of 21 days programming challenge")
print("Please enter your personal information")
#output
firstname = input("Enter your First Name: ")
lastname  = input("Enter your Last Name: ")
#taking input

age= int(input("Please enter your age: "))
#taking input and converting string into integer data types

print("Hello",firstname,lastname,"\n")
print("You are",age,"years old.\n")

#data types
a=type(firstname)
b=type(age)
print(a)
print(b)
print("\n")

#multiline strings
mulstr = """This is multiline string
It consist of multiple lines of text
such as paragraph."""
print(mulstr)
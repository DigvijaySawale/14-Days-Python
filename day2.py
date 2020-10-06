#day 2 will cover conditional statements (if) and for loops

print("Wel-come to Day 2 of 21 Days Programming Challenge\n")
print("BMI of students in Class")
nos=int(input("Please enter no of students: "))
print("Enter student respectively\n")

a,b,c=0,0,0
for std in range(nos):
    nm = input("Enter name: ")
    ht = float(input("Enter Height in meters: "))
    wt = float(input("Enter Weight in kg: "))
    bmi = wt/(ht*ht)
    print("Body-Mass Index is:",bmi)
    if bmi<18.5:
        print(nm,"is Underweight\n")
        a = a +1
    elif 18.5<=bmi<=24.9:
        print(nm,"has normal weight\n")
        b = b +1
    else:
        print(nm,"is overweight\n")
        c =c +1
print("***Summary***")
print("Under-weight Students:",a,"\nNormal Weight Students:",b,"\nOver-Weight Students:",c,"\n")



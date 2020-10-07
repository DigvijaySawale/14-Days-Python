#day3 will cover while loop and break statement in python
#factorial problem and concept of infinite loop
print("Wel-come to Day 3 of 21 Days Programming Challenge\n ")
print("*****FACTORIAL*****")
num = int(input("Enter the number to find the factorial: "))
fact=1 #declaring a variable as fact and assigning 1 to it

while num>0:       # start whil loop
    fact*=num
    num-=1
print("Factoirial of given number is :",fact,"\n")

print("Joker's Magic\n")
fac2=int(input("Enter the factorial value: "))

while True:
    if fac2==fact:
        print("Well done, You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")
        fac2=int(input("Enter the factorial value: "))


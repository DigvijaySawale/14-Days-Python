#day 4 will cover basics of loops
#maximum marks in class problem
print("Wel-Come to Day 4 of 21 Days Programming Challenge\n")
marks=list()     #initializing list 
stu=int(input("Enter the number of students: "))

for i in range(0,stu):    #range function 
    mar=int(input("Enter Marks: "))
    marks.append(mar)   #append method to add element at the end of list
print("Marks of all Students:",marks)

max=0
for j in marks:
    if j>max:
        max = j

print("Maximum marks are:",max,"\n")

marks.sort()        #sort method to sort elements of list
print("Marks in ascending order are:",marks)
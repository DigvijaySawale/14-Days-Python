#day 8 will cover tuples in python programming language

print("Wel-Come to Day 8 of 21 Days Programming Challenge\n")

thistuple = tuple()  #declaring tuple
thistuple = ('digvijay', 'chetan', 'pratik', 'ashish', 'mayur','digvijay', 'pratik', 'aniket')
print(thistuple)
print("""
|`````````````````````````````````|
| 1.Print element using Index     |
| 2.Print length of tuple         |
| 3.Print elements using range    |
| 4.Find element's existance      |
| 5.Count element occurance       |
| 6.Find index of element         |
| 7.Exit                          |
|_________________________________|
""")
ch = int(input("\nEnter choice number: "))
while ch!=7:
    if ch ==  1:
        ind = int(input("Enter the index of element to be printed: "))
        print(thistuple[ind])
        ch = int(input("\nEnter choice number: "))
        
    elif ch == 2 :
        print("Length of tuple:",len(thistuple))
        ch = int(input("\nEnter choice number: "))

    elif ch == 3 :
        sr = int(input("Enter starting range: "))
        er  = int(input("Enter end range: "))
        print("Printing range :",thistuple[sr:er])
        ch = int(input("\nEnter choice number: "))

    elif ch == 4 :
        ele = input("Enter the element to be found: ")
        if ele in thistuple:
            y = thistuple.index(ele)
            print("Element Found at position",y)
        else:
            print("Element does not exist")
        ch = int(input("\nEnter choice number: "))

    elif ch == 5 :
        ele2 = input("Enter the element to find its count: ")
        x = thistuple.count(ele2)
        print("Element occured",x,"times")
        ch = int(input("\nEnter choice number: "))

    elif ch == 6 :
        ele3 = input("Enter the element to find its index: ")
        z= thistuple.index(ele3)
        print("Element's index:",z)
        ch = int(input("\nEnter choice number: "))
    else:
        print("\nAlert!!! Enter correct choice")
        ch = int(input("\nEnter choice number: "))

print("Tuple : ",thistuple)
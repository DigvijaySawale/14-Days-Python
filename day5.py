#day 5 will cover all list methods()
#hotel menu using list
print("Wel-Come to Day 5 of 21 Days Programming Challenge\n")
lst = list()
print("Operations In List Data Structure")
print("""
|````````````````````````````|
|1.Append   5.Clear   9.Copy |
|2.Count    6.Index   10.Sort|
|3.Insert   7.Remove  11.View|
|4.Reverse  8.Pop     12.Exit|
|____________________________|\n""")#  multiline comment

ch=int(input("Enter operation number: "))

while ch!=12:
    if ch == 1 :
        print("append() : Adds an element at the end of the list")
        ele = input("Enter element: ")
        lst.append(ele)
        ch=int(input("\nEnter operation number: "))
    
    elif ch == 2:
        print("count() : Returns the number of times element occured in list with the specified value")
        ele = input("Enter element to find its count: ")
        x=lst.count(ele)
        print(ele,"occured",x,"times")
        ch=int(input("\nEnter operation number: "))

    elif ch == 3:
        print("insert() : Adds an element at the specified position")
        ele = input("Enter element: ")
        no = int(input("Enter index: "))
        lst.insert(no,ele)
        ch=int(input("\nEnter operation number: "))

    elif ch == 4:
        print("reverse() : Reverses the order of the list")
        lst.reverse()
        print("Reversed List:",lst)
        lst.reverse()   #reteriving original list
        ch=int(input("\nEnter operation number: "))

    elif ch == 5:
        print("clear() : Removes all the elements from the list")
        lst.clear()
        ch=int(input("\nEnter operation number: "))

    elif ch == 6:
        print("index() : Returns the index of the element in its first occurance ")
        ele = input("Enter element: ")
        ind= lst.index(ele)
        print(ele,"occured at",ind,"index")
        ch=int(input("\nEnter operation number: "))

    elif ch == 7:
        print("remove() : Removes the element in its first occurance")
        ele = input("Enter element: ")
        lst.remove(ele)
        ch=int(input("\nEnter operation number: "))

    elif ch == 8:
        print("pop() : Removes the element at the specified position")
        pos=int(input("Enter Position: "))
        lst.pop(pos)
        ch=int(input("\nEnter operation number: "))

    elif ch == 9:
        print("copy() : Returns a copy of the list")
        copi = lst.copy()
        print("Copied List:",copi)
        ch=int(input("\nEnter operation number: "))

    elif ch == 10:
        print("sort() : Sorts the list")
        lst.sort()
        print("Sorted List:",lst)
        ch=int(input("\nEnter operation number: "))

    elif ch == 11:
        print(lst)
        ch=int(input("\nEnter operation number: "))

    else:
        print("Alert!!! ->Enter Valid Operation Number")
        ch=int(input("\nEnter operation number: "))

print("Final List:",lst)
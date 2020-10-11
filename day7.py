#day 7 will cover all Dictionary methods

print("Wel-Come to Day 7 of 21 Days Programming Chalenge")
Dict = dict()
print("Operation in Dictionary data structure")
print("""
|```````````````````````````````````````````|
|1.Get    4.Items  7.PopItem  10.View Dict  |
|2.Clear  5.Keys   8.Update   11.SetDefault |
|3.Copy   6.Pop    9.Values   12.Exit       |
|___________________________________________|
""")
Dict = {'Name': 'Digvijay', 'Lastname': 'Sawale','College':'D Y Patil College of Engineering','Rollno':110,'Year':'TE','Div':'B'}
print(Dict)
ch = int(input("\nEnter the operation number: "))

while ch != 12:
    if ch == 1:
        print("get() : Returns the value of the specified key")
        x = Dict.get(input("Enter the key: "))
        print("\nIts Value is ",x)
        ch = int(input("\nEnter the operation number: "))

    elif ch == 2:
        print("clear() : Removes all the elements from the dictionary")
        Dict.clear()
        ch = int(input("\nEnter the operation number: "))

    elif ch == 3:
        print("copy() : Returns a copy of the dictionary")
        copi = Dict.copy()
        print("\nCopied Dictionary:",copi)
        ch = int(input("\nEnter the operation number: "))

    elif ch == 4:
        print("items() : Returns a list containing a tuple for each key value pair")
        x = Dict.items()
        print(x)
        ch = int(input("\nEnter the operation number: "))

    elif ch == 5:
        print("keys() : Returns a list containing the dictionary's keys")
        x = Dict.keys()
        print(x)
        ch = int(input("\nEnter the operation number: "))

    elif ch == 6:
        print("pop() : Removes the element with the specified key")
        Dict.pop(input("Enter the key: "))
        print(Dict)
        ch = int(input("\nEnter the operation number: "))

    elif ch == 7:
        print("popitem() : Removes the last inserted key-value pair")
        Dict.popitem()
        print(Dict)
        ch = int(input("\nEnter the operation number: "))

    elif ch == 8:
        print("update() : Updates the dictionary with the specified key-value pairs")
        ke = input("Enter key: ")
        val = input("Enter value of above key: ")
        Dict.update({ke:val})
        ch = int(input("\nEnter the operation number: "))

    elif ch == 9:
        print("values() : Returns a list of all the values in the dictionary")
        x = Dict.values()
        print(x)
        ch = int(input("\nEnter the operation number: "))

    elif ch == 10:
        print("Current Dictionary:",Dict)
        ch = int(input("\nEnter the operation number: "))

    elif ch == 11:
        print("setdefault() : Returns the value of the specified key. If the key does not exist: insert the key, with the specified value")
        ke = input("Enter key: ")
        val = input("If key doesnt exist, enter value: ")
        x = Dict.setdefault(ke,val)
        ch = int(input("\nEnter the operation number: "))

    else:
        print("Alert!!! ->Enter Valid Operation Number")
        ch=int(input("\nEnter the operation number: "))

print("Final Dictionary:",Dict)


    

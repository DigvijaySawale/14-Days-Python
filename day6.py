#day 6 will cover basic Dictionary Data Structure
print("Wel-Come to Day 6 of 21 Days Programming Challenge")

Dict = dict()
Dict = {'Name': 'Digvijay', 'Lastname': 'Sawale','College':'D Y Patil College of Engineering','Rollno':110,'Year':'TE','Div':'B'}

print(Dict,"\n")    #printint the dictionary

for x in Dict:
    print(x)    #printing keys in dictionary usib=ng for loop

for y in Dict:
    print(Dict[y])   #printing values of the keys in dictionary using for loop


for x,y in Dict.items():   # item() method to access key value pair
    print(x,":",y)
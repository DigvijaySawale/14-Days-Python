# dahy 14 will cover slicing operation on strings
#Its a simple palindrome program

string=input("Enter string:")   #taking input

if string==string[::-1] :               #reversing the string using slicing operation 
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")
# This is the project in which we will make pdf to speak
import pyttsx3  #import python text to speech module

import PyPDF2  #import python pdf module

book = open(input("Enter the book name"), 'rb')  #opening book and reading it

pdfreader = PyPDF2.PdfFileReader(book)   
pages=pdfreader.numPages  #counting pages
print("There are",pages,"pages in the book") #total pages
speaker= pyttsx3.init() #initialization of python text to speech
page = pdfreader.getPage(int(input("Enter page no to start reading"))-1)
text = page.extractText() 
speaker.say(text)
speaker.runAndWait()


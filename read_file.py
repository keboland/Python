#! /usr/bin/python

f = open("birds.txt", "r")
data = f.read()
words = data.split(" ")				#Creates variable words which splits contents of data according to a space between words

f.close()					#Closes the file

print("The words in the text are:")		#Prints 
print(words)					#Prints variable words 
num_words = len(words)				#Creates variable num_words equal to the length of the words variable
print("The number of words is ", num_words)	#Prints the number of words with the variable num_words

lines = data.split("\n")			#Creates variable lines equal to the each new line in file
print("The lines in the test are:")		#Prints Text
print(lines)					#Prints lines
print("The number of lines is:",len(lines))	#Prints text and results of length of lines




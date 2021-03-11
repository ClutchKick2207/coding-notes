#!/bin/python3

#For the purposes of neatness:
print("\n") #new line

#Print string:
print('Time for strings!:')
print("Strings and things:") #printing a simple string (letters)
print('Hello, world!') #as per tradition!
print(''' Hello, this is
a multi-line string!''') #how to print a multi line string
print("This is"+" a string") #how you can add strings to make a string

print("\n") #new line

#Math
print('Math time:')
print(50 + 50) #addition
print(50 - 50) #substraction
print(50 * 50) #multiplication
print(50 / 50) #division
print(50 + 50 - 50 * 50 / 50) #PEMDAS (Pentesting math!)
print(50 ** 2) #exponents (to the power of)
print(50 % 2) #modulo (remainder) (i.e. 50/2 = 25, where the leftover (50 - 25) is the output)
print(50 // 2) #Number without leftovers

print("\n") #new line


#Variables & Methods
print('Fun with variables and methods!')
quote = 'All is fair in love and war' #declring a variable (a nice quote!)
print(len(quote)) #the len() function is used to find the length (i.e. the length of the variable (in characters) of 'quote')
print(quote.upper()) #prints the variable in upper-case lettering
print(quote.lower()) #prints the variable in lower-case lettering
print(quote.title()) #prints the variable in title form (the first letter of each word is capitalised)

	#Declaring some variables (The personal stuff...)
name = 'Ariz' #string (ie str(Ariz) )
age = 13 #integer (ie: int(13) )
fav_decimal_number = 4.8 #float (floating point integer) (ie: float(4.8) )

print(int(age)) #returns 'age' as an integer (although it already is one)
print(int(29.55)) #int function does not round (i.e. just takes integers before the decimal point)

	#Calling variales using the 'print' function
print("My name is " + name + " and I am " + str(age) + " years old") #make sure that all the variables are converted to strings.

	#Variable Manipulation
age += 1 #adding 1 to the variable 'age'
print('After a very long year, I am now ' + str(age) + ' years old') #proof of concept

	#Proof that a variable can also be used for this purpose:
birthday = 1
age += birthday
print('Another birthday later, ' + name + ' turns ' + str(age) + ' years old') #Don't forget to make the integer a string!

print('\n') #Printing a new line (kind of getting boring)

#Functions
print("Now, some functions!")
def who_am_i(): #Defining a function (don't forget the indenting!)
	name = 'ariz'#variables in a function are only callable in the function.
	age = 13 #Global variables (those not tied to anything) can be called.
	print("My name is " + name + " and I am " + str(age) + " years old")

who_am_i() #Calling the function


	#Adding in parameters
def add_one_hundred(num): #defining a function with a parameter (--><-- *nice*)
	print(num + 100) #get the parameter and use it in the function

add_one_hundred(100) #uses the function that is defined above

	#Adding in multiple parameters
def add(x,y): #Declaring a variable with multiple parameters
	print(x + y) #used by incorporating the variables defined as parameters

add(7,5) #Calling the function
add(305,207) #Using some bigger numbers...

	#Using return
def multiply(x,y): #defining a function
	return x * y #returns stores the value that is calculated in the line

print(multiply(3,7)) #'print' necessary to see contents of 'return'

def square_root(x): #defining yet another function
	return x ** 0.5 #You should know why this works...

print(square_root(64)) #gets a 'float' integer

print("\n") #print a new line

#Boolean Expressions (True or False):
print("Time for some Boolean expressions!")
bool1 = True #setting the variable as true
bool2 = 3*3 == 9 #The asnwer for thr equation is correct, makinh the variable 'True'. Be sure the when you mean 'equals to' to use two '=' signs, ie: ==
bool3 = False
bool4 = 3*3 != 9 #i.e. False

print(bool1, bool2, bool3, bool4)
print(type(bool4))
print(type(bool2))

bool5 = "True" #becomes a string, don't do if you desire a boolean expression
print(type(bool5))

#Ralational and Boolean Operators
greater_than = 7 > 5 #quite simple, if the equation is true, it will output as true
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (5 < 7) #Both have to be true output true
test_or = (7 > 5) or (5 < 7) #True + False = True, itherwise makes sense
test_not = not True #kinda obviously false

print("\n") #I should really just make a function for this...
def new_line():
	print("\n")
#Now that is over with...

#Conditional Statements
print('Conditional statements')
def soda(money): #a simple function to exp;in conditional statements
	if money>= 2: #If the money variable is 2 or more, do the following...
		return "You've got yourself a soda!"
	else: #If it is anything else, do this:
		return "No soda for you!"

print(soda(3))
print(soda(1))

def alcohol(age, money):
	if (age >= 18) and (money >= 5):
		return "We're getting tipsy!"
	if (age >= 18) and (money < 5):
		return "Come back with more money!"
	if (age <= 18) and (money >= 5):
		return "Nice try, kid!"
	if (age <= 18) and (money < 5):
		return "You are too poor, and too young!"

print(alcohol(24,10))
print(alcohol(32,1))
print(alcohol(13,100))
print(alcohol(12,1))

print('\n') # *NOT* using the function

#Lists
print('Lists have brackets')
movies = ['The art of Racing in the Rain', 'The Fast and the Furious', 'Too Fast too Furious'] #just some personal favs

print(movies[1]) #Acutally the second movie
print(movies[0]) #The first item in the list
print(movies[0:2]) #Even though you also called 1 it doesn't output, so you #need to do this
print(movies[0:3]) #this doesn't actually print 3, but it prints 1 and 2 now
print(movies[1:]) #Slicing, prints all movies from 1
print(movies[:1]) #Just pulls out 0
print(movies[-1]) #pulls the last movie
print(len(movies)) #prints the length

movies.append('JAWS') #appends the movie to the list
print(movies)

movies.pop() #deletes the last thing in the list if nothing is stated
print(movies)

movies.pop(1) #removes the 2nd movies

movies = ['The art of Racing in the Rain', 'The Fast and the Furious', 'Too Fast too Furious'] #just some personal favs v2
person = ["Jeff", "Jimmy", "James"]
combined = zip(movies, person)
print(list(combined))

#Tuples

print('Tuples have parentheses and cannot change')
grades = ('A', 'B', 'C', 'D', 'E')
print(grades)

print("\n") #print a new line

#Looping
print('for loops - start to finish of iterate.')
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables: #prints interations untils finished
	print(x)

print('While loops - Execute while True')
i = 1
while i < 10: #A simple while loop
	print('i')
	i += 1

#Importing
print('Importing is important:')

import sys #System functions and parameters (import that module)

from datetime import datetime #Import a specific part of a module
print(datetime.now()) #run the module

from datetime import datetime as dt #importing a module with an alias
print(dt.now)

def new_line(): # Makes a functions to add a new line...
	print('\n')

new_line() #Calling the function
print("")
#Advaced Strings
print('Advanced Strings')
my_name = 'Ariz'
print(my_name[0]) #First letter in the name
print(my_name[-1]) #Last letter in the name

sentence = 'This is a sentence.'

print(sentence[:4]) #first word from the sentence (i.e. 'This')
print(sentence[-9: -1]) #last word from the sentence (i.e. 'sentence') without '.'

print(sentence.split) #split seprint("")ntence by delimiter (by default a space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split) #the thing at the front is the delimiter (could be anything else)
print(sentence_join)
new_line() #for clarity in the outputs
print("\n".join(sentence_split))

quoteception = "I said, 'give me all the money'" #this is how you print the '' in a text
print(quoteception)

print("A" in "Apple") #Boolean (prits true)
letter = "A"
word = "Apple"
print(letter in word) #Drive the concept

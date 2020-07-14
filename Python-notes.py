#Python Notes (Written in Python 3.8)


print('Hello, World!') #The ritual is complete!



#Variables:


#Variable Quick Rules:
'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
'''

#examples of the use of variables in Python:
x = 69
variable = 420
#Note that you can both have the information in a variable as a string and a integer like so:
xxx = 'variable' #as a string
yyy = 249729307 #as an integer
#Note that there is no command to declare a variable, and it is simply stated

#Program utilising variables:

var1 = 'variables are a useful way to save time, as it makes a program more versatile and more efficient to run'
print(var1)

#You can specify what format you want a piece of code, by simply putting in one of the below:
var2 = int(18475927387592) #To make the info a integer
var3 = str('hi there, this will now be a string') #Makes it a string

#Remember that if you are going to make something a 'string' it can either be:
example = 'example'
example = "example"
#But it cannot be:
    example = "example'

#examples of legal and illegal variable names:

#Legal variable names:
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"

#Illegal variable names:
    2myvar = "John"
    my-var = "John"
    my var = "John"

#It is possible to make more than one variable in a line, like the below:
    x, y, z = 'testing', 'also', 'right'

#You can also assaign the same input to multiple variables:
    x = y = z = 'people'

#A note on Global variables:
#Global variables are variables that are seperate to any other function, and
#it allows for everything to use it, with an example below:
    example_int = 'this is a string'
    def myfunction():
        #example_int can be used in this function as it is a Global variable
        print(example_int)


#Comments:


#Comments are a great way to let other people know what a piece of code does
#or allows for you to add in extra information for you to view for later

#Comments can be used anywhere by simply inserting a '#' as you are seeing everywhere

#Multi-line comments are achieved by putting a '#' on the line below...
#so that you can continue your rambling.

'''
You can also use a triple quotes if you wish and it can work! (Although you should just use #'s as they
are the official way of doing so)
'''



#Data Types:


#Data Types:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

#If you ever need to know what data-type a variable is using, use the 'type()':
x = 5
print(type(x))

#-------------------------------------------------------------------------------
#How to set different data types:
    x = "Hello World"	#str
    x = 20	            #int
    x = 20.5            #float
    x = 1j	            #complex
    x = ["apple", "banana", "cherry"]	#list
    x = ("apple", "banana", "cherry")	#tuple
    x = range(6)	                    #range
    x = {"name" : "John", "age" : 36}	#dict
    x = {"apple", "banana", "cherry"}	#set
    x = frozenset({"apple", "banana", "cherry"})	#frozenset
    x = True	        #bool
    x = b"Hello"	    #bytes
    x = bytearray(5)	#bytearray
    x = memoryview(bytes(5))	        #memoryview
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#How to setting the different data types:
    x = str("Hello World")	#str
    x = int(20)	            #int
    x = float(20.5)	        #float
    x = complex(1j)	        #complex
    x = list(("apple", "banana", "cherry"))	    #list
    x = tuple(("apple", "banana", "cherry"))	#tuple
    x = range(6)	        #range
    x = dict(name="John", age=36)	            #dict
    x = set(("apple", "banana", "cherry"))	    #set
    x = frozenset(("apple", "banana", "cherry"))    #frozenset
    x = bool(5)	            #bool
    x = bytes(5)	        #bytes
    x = bytearray(5)	    #bytearray
    x = memoryview(bytes(5))#memoryview
#-------------------------------------------------------------------------------




#Numbers:




#There are 3 main operations that are available in python for the use of numbers:
    int()
    float()
    complex()
#Or when assigned with numbers:
    x = 1 #int (integer)
    y = 2.8 #float (float)
    z = 1y #complex (algrebic style)
#But to check what operation is being used, simply use this command, like so:
    print(type(#variable goes here))
                                    Int
--------------------------------------------------------------------------------
#Int is used when expressing a number that is a whole number (that can be posit-
#ive or negative), without decimals, and of unlimited size. E.G:
    integer1 = -1
    integer2 = 2354629845698372465897246
    integer3 = 45
                                    Float
--------------------------------------------------------------------------------
#Float is used when you are using a number that has decimal digits, and otherwi-
#se can have the same properties as an integer. E.G:
    floating_point_number1 = 1.235462
    floating_point_number2 = 4.0
    floating_point_number3 = -75.32
#Float can also be used to specify specific numbers, like 'e' (representing to -
#the power of 10) and can be used like below:
    floating_point_number4 = 35e3 (where the number is: 35 * 10^3)
    floating_point_number5 = 14E9 (where the number is: 14 * 10^9)
    floating_point_number6 = -8e9 (where the number is: -8 * 10^9)

                                    Complex
--------------------------------------------------------------------------------
#Complex numbers are numbers that are used to represent imaginary numbers (by u-
#sing 'j') and are used when imaginary numbers are present. E.G.:
    complex_number1 = 4j
    complex_number2 = 3 + 5j
    complex_number3 = -10j

--------------------------------------------------------------------------------

#All of these can be exchanged with each other (mostly), by using a few commands:)
    '''
    Look at the commands at the very top!
    '''
--------------------------------------------------------------------------------
#Something that is interesting to look at is the 'random' module
#used like this:
import random
print(rand.randrange(1,1000))

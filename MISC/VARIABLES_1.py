#VARIABLES.PY

import sys

a = 5   #numbers
b = 10
print(a+b) #string

message = "hello WORLD"
print(message)

print("Hello, World")
print("Hello", "World")

a= str(a)
print(type(a))

print(type(b), "\n")
"""the print(type(b) + "\n") statement will raise a TypeError 
because you cannot concatenate a string with a type object. You 
should use a comma to separate the arguments in the print function 
instead."""

print("VERSION\n", sys.version)
print("PATH\n", sys.path)
print(sys.executable)
print(sys.flags,"\n")

"""
This portion of the code is for testing greater than or less than, 
also if statement
"""
if 5>2:
	print("Five is greater than two")
	
x="John"
print(type(x))


#This portion is going to talk about casting
x=str(3)
y=int(3)
z=float(3)

print(x)
print(y)    #This is an integer
print(z)    #This is a float



"""
---------------------------------------------
VARIABLE NAMING CONVENTIONS
---------------------------------------------
"""

"""
Rules for Python variables:

1. A variable name must start with a letter or the underscore 
character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters 
and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three 
different variables)
5. A variable name cannot be any of the Python keywords.

3x = "John" #This will give an error
x3 = "John" #This will not give an error
jojo's = "John" #This will give an error
jojos = "John" #This will not give an error
jojo_s = "John" #This will not give an error
"""


"""
Multi-word Variable Names
It's for readability purposes :) """
mySampleVariable = "John"   #This is a Camel Case first letter is small
MySampleVariable = "John"   #This is a Pascal Case
my_sample_variable = "John" #This is a Snake Case
My_Sample_Variable = "John" #This is a Pascal Case

X,Y,Z = "Amsterdam", "Berlin", "Copenhagen" #Assigns different values to multiple variables
print("\n" + X)
print(Y)
print(Z + "\n\n")

X = Y = Z = "Amsterdam" #Assigns same value to multiple variables
print(X)
print(Y)
print(Z, "\n\n")

# Unpack what???
"""
If there is a list of values, Python allows you to extract the
values into variables. This is called unpacking. 
"""
countries = "Amsterdam", "Berlin", "Copenhagen", "Dublin"
x,y,z,a = countries
print(x)
print(y)
print(z)
print(a)

"""
X,Y,Z = countries  -> INCORRECT
because you are trying to unpack four values into three variables. 
The countries tuple contains four elements, but you are only 
providing three variables (X, Y, Z) to unpack them into.
This will raise a ValueError."
"""

a="awesome"
b="Python is"
print(b+a)
print(b + a)
print(b +' ' + a)
print(b +" " + a)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print("\n")
print(x,y,z)
print(x + y + z)

p=5
#q = High
#print(p + q) #This will give an error because High is not a variable
#print(p,q) #This will give an error because High is not a variable
q = "High"
print(q + "p")
print(q + str(p))
print(q, p, "!")
print(q, str(p),"!", "\n")

""""
Comma in the print function, it separates the arguments 
and prints them with a space in between by default. 
Each argument can be of a different type, and the print 
function will handle the conversion to a string automatically.

Comma: Used in the print function to separate arguments, 
automatically adding spaces between them. It can handle different data 
types.
Plus: Used for string concatenation. All operands must be strings, 
so you need to convert non-string values to strings using str().

"""
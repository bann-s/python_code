#Data types

#String
name = "John"
print(name)

#Integer
age = 30
print(age)

#Float
height = 5.9
print(height)   

#Boolean
a = True
b = False
print(a)
print(b)

#List
fruits = ["apple", "banana", "cherry"]
print(fruits)

#Tuple
colors = ("red", "blue", "green")
print(colors)   

#Set
fruits = {"apple", "banana", "cherry"}
print(fruits)

#Dictionary 
person = {"name": "John", "age": 30, "city": "New York"}
print(person)

#Type conversion
x = 1
y = 2.8
z = 1j

#convert from int to float:
a = float(x)
print(a)

#convert from float to int:
b = int(y)
print(b)    

#convert from int to complex:
c = complex(x)  
print(c)

#Specify a variable type
x = str("Hello World")
y = int(20)
z = float(20.5)
print(x)
print(y)
print(z)

#Get the data type
x = 5
print(type(x))

print(int(35.88))
print(float(35))


import random
print(random.randrange(1,100))
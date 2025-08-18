# Variables in Python are containers used to store data in memory. Unlike statically typed languages, 
# Python is a dynamically typed language, meaning you don’t need to declare the type of a variable explicitly. 
# A variable is created the moment a value is assigned to it.

#Keep in mind that None is not equivalent to False, 0, or an empty string.

# How Variables Work Internally
# When you assign a value to a variable, a memory location is created to store the value, and the variable becomes a reference (or label) to that memory location

# Boolean Variables
# Variables can also store Boolean values (True or False): 
# True and False must start with capital letters in Python.

# Special Value: None
# If you want to indicate that a variable has no value, you can use None. It is a special value in Python. 
# Keep in mind that None is not equivalent to False, 0, or an empty string.

# Accessing Undefined Variables
#If you try to access a variable that has not been defined, Python will raise a NameError

# Python way of swapping variables
# In Python, you can swap the values of two variables without needing a temporary variable.
# This is done using tuple unpacking, which allows you to assign multiple variables in a single line.

# Example of swapping variables
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)
a, b = b, a  # Swapping values using tuple unpacking
print("After swapping: a =", a, ", b =", b) 
# Output:
# Before swapping: a = 5 , b = 10
# After swapping: a = 10 , b = 5
# This method is concise and efficient, making it a preferred way to swap values in Python.

#---------------------------------------------------------------------------------------------------
#isinstance(a, int) in Python checks whether the variable a is an instance of the int class (in plain words: “is a an integer?”).

#Example
a = 5
print(isinstance(a, int))  # True

b = 5.0
print(isinstance(b, int))  # False (because b is a float)

c = True
print(isinstance(c, int))  # True in Python, because bool is a subclass of int


#Why True is int in Python
isinstance(True, int)  # True
#This is because bool inherits from int:

issubclass(bool, int)  # True
#So True behaves like 1 and False like 0 in arithmetic.
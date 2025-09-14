"""
This script demonstrates the use of list comprehension to calculate the square roots of numbers using python comprehensions.

Create a List of Squares of numbers from 1 to 10

Sample Output

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
a= [i**2 for i in range(1,11)]
print(a)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b= [i**0.5 for i in range(1,11)]
print(b)





#You are going shopping. Let’s make a grocery list so that you can plan your budget.
#Store the number of cucumbers you want to buy in a variable called cucumbers. 
# Make sure it’s at least 1, and that it’s the appropriate datatype! 
# The store doesn’t sell partial cucumbers.
# 2. Each cucumber costs 3.25 doubloons. Store the price per cucumber in a variable called price_per_cucumber.
# 3.Create a new variable called total_cost which is the product of how many cucumbers you are going to buy and the cost per cucumber.
# 4. Print out total_cost.
# What datatype is it?

cucumbers = 3
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print( total_cost)
print(type(total_cost))
# The datatype of total_cost is <class 'float'> because it is a product of an integer and a float.



#In Python 2, when we divide two integers, we get an integer as a result. When the quotient is a whole number, this works fine:
#quotient = 6/2
# the value of quotient is now 3, which makes sense
#However, if the numbers do not divide evenly, the result of the division is truncated into an integer. In other words, the quotient is rounded down to a whole number. This can be surprising when you expect to receive a decimal and you receive a rounded-down integer:
#quotient = 7/2
# the value of quotient is 3, even though the result of the division here is 3.5

#To yield a float as the result instead, programmers often change either the numerator or the denominator (or both) to be a float:
#quotient1 = 7./2
# the value of quotient1 is 3.5
#quotient2 = 7/2.
# the value of quotient2 is 3.5
#quotient3 = 7./2.
# the value of quotient3 is 3.5

#An alternative way is to use the 
#float()  method:
#quotient1 = float(7)/2 
# the value of quotient1 is 3.5


cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers / num_people
print ("whole cucumbers",whole_cucumbers_per_person)
cucumbers = 100.0

float_cucumbers_per_person = float(cucumbers) / num_people
print( "whole cucumbers",float_cucumbers_per_person)
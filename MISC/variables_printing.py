#This is a lession to print some types

def algebra(x):
    fun = x*x +1
    print("printing the calculated result " + str(fun))
    return fun

x = 5
y = "hello, World"

print(x)
print(y)

"""
Multi line commenting
print("HELLO WORLD")
"""

if 2 > 2: 
    print("2 is greater than 2")

elif 5 > 2:
    print("5 is greater than 2")
else:
    print ("2 is greater than 5")

print("Now going to call function algebra")
algebra(2)
print("Done with the function algebra")
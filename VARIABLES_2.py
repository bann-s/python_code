#this portion of the code is about Global and Local Variables

x = "amazing"   #Global Variable

def my_function():
    x="fantastic" #Local Variable
    print("Python is " + x)

my_function()   #This will print with local Variable fantastic

print("Python is " + x,"\n") #This will print with Global Variable amazing

#-------------------------------------------------

#This portion of the code is about Global Keyword defined inside a function
#If you use the global keyword, the variable belongs to the global scope.

x = "amazing"

def my_fun():
    global x   #This will make the variable x global
    x = "simple"
    print("Python is " + x, "\n")

my_fun()

print("Python is " + x, "\n")

#-------------------------------------------------

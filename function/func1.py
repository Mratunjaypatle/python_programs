# There are two types of function 
# 1.  pre defined 
# 2.  User defined
"""
function is reusbale block of code that performs a specific task..

Parameter : You can pass data into function using variables that is called parameter
Arguments : we pass our data into the function while calling the function.

Returning the data using return statement..

"""

def myfunction() : ## user defined function
    print("this is my function.")

myfunction() # calling a function 


def my_name(name) :
    print(f"hello {name}") 

my_name("samay")


def add(a , b):
    print(a+b)

add(10,20)


def add_numbers(a,b=20) :
    return a+b

print(add_numbers(20))


# formatted string literal 

def say_hello (name , message = "how are you ..") :
    print(f"{message}  {name}")

say_hello("Adam")





# Namespace 

# Namespace(collection of names and their asssociate objects maintained by python) are 
# dictionaries where the variable are keys  and its value is made as value of dictionary .
# Scope 

#Scope is the region of a program where a particular variable, function, or object name can be accessed or referenced. 
#It determines the visibility and lifetime of identifiers within a program.

# Short Definitions

# Namespace:
# A namespace is a collection of names and their associated objects maintained by Python.

# Scope:
# Scope is the area of a program in which a name is directly accessible.

#LEGB RULE 



# a--->global variable 
#b--->local variable 
#We can acess the global variable inside the local variable but cannot directly modify it.

#Accessing directky gives an error.
a=2

def temp():
    a=a+1
    print(a)

temp()
print(a)
# Traceback (most recent call last):
#   File "c:\Users\vansh\OneDrive\Desktop\Filehandling\decoratorsandnamespaces.py", line 28, in <module>
#     temp()
#     ~~~~^^
#   File "c:\Users\vansh\OneDrive\Desktop\Filehandling\decoratorsandnamespaces.py", line 25, in temp
#     a=a+1
#       ^
# UnboundLocalError: cannot access local variable 'a' where it is not associated with a value



#WE DO IT USING "GLOBAL".
a=2

def temp():
    global a
    a=a+1
    print(a)

temp()
print(a)

#Built-in scope
# LEGB Rule in Python

# The LEGB Rule is the order in which Python searches for a variable name.

# LEGB stands for:

# L → Local Scope
# E → Enclosing Scope
# G → Global Scope
# B → Built-in Scope

# When Python encounters a variable, it searches for it in this order:

# Local → Enclosing → Global → Built-in
# 1. Local Scope (L)

# Variables defined inside a function.

# def show():
#     x = 10
#     print(x)

# show()

# Output:

# 10

# Here, x is searched in the local scope first.

# 2. Enclosing Scope (E)

# Variables in an outer function that encloses an inner function.

# def outer():
#     x = 20

#     def inner():
#         print(x)

#     inner()

# outer()

# Output:

# 20

# Here, x is found in the enclosing scope.

# 3. Global Scope (G)

# Variables declared outside all functions.

# x = 30

# def show():
#     print(x)

# show()

# Output:

# 30

# Here, x is found in the global scope.

# 4. Built-in Scope (B)

# Names predefined by Python, such as print(), len(), and input().

# a = [1, 2, 3]
# print(len(a))

# Output:

# 3

# len() is found in Python's built-in scope.

# Exam Definition

# LEGB Rule:
# The LEGB rule is the order Python follows to resolve variable names. Python searches for a name in the Local, Enclosing, Global, and Built-in scopes respectively.

# Diagram
# Built-in Scope
#       ↑
# Global Scope
#       ↑
# Enclosing Scope
#       ↑
# Local Scope

# Python searches from Local → Enclosing → Global → Built-in until the variable is found.

def outer():
    a=1
    def inner():
        nonlocal a
        a=+1

        print("inner",a)
    inner()
    print("outer",a)


outer()
print("main ")



#------------------------------------------------------------------------------------------


#DECORATORS:
#Decorrators are the functions receives another function as input and adds some 
# functionality (decoration) to it and returns it.

def my_decorator(func):
    def wrapper():
        print("********************")
        func()
        print("********************")

    return wrapper
def hello():
    print("HELLO")

a=my_decorator(hello)
a()
#------------------------------------------------------------------------------------------
def my_decorator(func):
    def wrapper():
        print("********************")
        func()
        print("********************")

    return wrapper
@my_decorator
def hello():
    print("HELLO")
hello()

#----------------------------------------------------------------------------------------



#Decorator function in python which calculates the running time of a python function


import time
def Decorator_timer(func):
    def wrapper(*args):
        start=time.time()
        func(*args)
        print("Time Taken by the ",func.__name__,time.time()-start,"Secs")
    return wrapper


@Decorator_timer  #Shortcut for using the decorators.
def say_hello():
    print("Hello")
    time.sleep(3)

say_hello()

@Decorator_timer
def square(num):
    print(num**2)





#------------------------------------------------------------------------------------------

def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args)==data_type:
                func(*args)

            else:
                raise TypeError("THIS IS NOT THE VALID DATA TYPE FOR THIS FUNCTION TO WORK")
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(num):
    print(num**2)

square(56)


#--------------------------------------------------------------------------------------------

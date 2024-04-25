# if 5 >2:
#     print("Five is greater than two!")

# This is explanation about comments:
# - To explain a block of python code.
# - You use python to prevent a block of code from running in python

# CREATING VARIABLES

# x = 5
# y = "John"
# print(x)
# print(y)
# x = 4
# x = "Sally"
# print (x)

# - Casting in Variables
# To specify the data type of a variable, you use Casting

# X = str(3)  # X will be '3'
# Y = int(3)  # Y will be 3
# Z = float(3)  # Z will be 3.0
# G = complex(3)  # G will be (3+0j) etc .,

# Get the Type or Data type used with the variable type()
# x = 5
# y = "John"
# print (type(x))

# Assigning Multiple Values to Multiple Variables
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# One Value to Multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

#Unpack a collection
# names = ["John", "Bob", "Mary"]
# x, y, z = names
# print(z)

#Outputing variables
# x = "Python "
# y = "is "
# z = "awesome"
# print (x, y, z)

# x = "Moses"
# y = 10
# print(x, y)

# Global Variables
# Variables that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

# z = "awesome"

# def myfunc():
#     z = "fantastic"
#     print("Python is " + z)

# myfunc()

# print ("Python is " + z)

# ## Using the "GLOBAL KEYWORD" in a function
# def tfunc():
    
#     global b
    
#     b = "Welcome"

# tfunc()
# print("Python is " + b)

# p = "Introdcution to Python"

# def intro_func():
#     global p
#     x = "fantastic"
# intro_func()
# print("Python is "  + p)

# To set specific data type in python

# c = str("Hello World")
# f = int(20)
# b = float(20.5)

# f = range(6)
# t = frozenset ({"Hello", "World"})

# #Display t
# print(type(t))

# u = bytearray(6)
# print(type(u))

# f = memoryview(bytes(6))
# n = None
# print(n)


# random number in interger

# import random

# print(random.randrange(1, 10))

# a = "Hello, World!"
# print(a[2:8])

## Looping Through a String
# - We have the for loop: A for loop in Python is a control flow statement that is used to repeatedly execute a block of code as long as a certain condition is met or as long as the condition is TRUE
# for x in "banana":
#     print(x)

# To calculate the length of a string
# The len() function returns the length of a string:

# a = "Hello, World!"
# print(len(a))


# To check a string

# txt = "The Best things in life aren't cheap"
# print("cheap" in txt)

# # Assignment

# # - Use "if" statement with the check option for string

# # # Check if NOT
# # To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

# # - To check if "expensive" is NOT present in the following sentence:

# # txt = "The Best things in life aren't cheap"
# print("expensive" not in txt)

# Use "if" with not
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")








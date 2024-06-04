# # This is for variable
# name = "Alice"
# age = 25
# print(type(name), type(age))

# This prints out the data inputed on after the other
# name = "Linux"
# print(name[4])

## This is for Integer Data Type
# Name = "Moses"
# say = "Welcome Here! Your age is"
# age = 10
# print (Name, say, age)

#This is for Float Data Type
# age = 100.5
# print (type(age))
# my_name = "Captain Dunkurk"
# my_address = "Tijuana, Mexico"
# my_address_num = 2+3j
# print ( my_name, my_address, my_address_num)

##Strings Data Type
# name = "John"
# message = """
# Welcome, John.
# This is your new class on Python programming
# """
# print (name, message)

#Boolean Data type
# is_greater = 10 < 5
# print (is_greater)


## List Data Type sample
# fruits = ["apple", "banana", "cherry"]
# numbers = [1, 2, 3, 4, 5]
# print (type(fruits), type(numbers))

# Tuples
#     - Tuples are similar to lists but are immutable (cannot be changed / or modified after creation), and it is enclosed in parentheses
## Sample Tuple

# Creating a tuple

# my_tuple = (1, 2, 3, 4, 5)

# # Attempting to modify the tuple
# my_tuple[0] = 10 #This line will raise an error because tuples are immutable
# print (my_tuple)

# Dictionaries
# Dictionaries are unordered collection of "key:value" pairs, enclosed curly braces {key:value}

# person = {"Name":"Alice", "Age": 25, "City":"Lagos"}
# car = {"Brand": "Toyota", "Model": "Corolla", "Year": 2019}
# print (person, car)

##Sets
    # - Set are unordered collections of unique items, enclosed in curly braces or created using set {} function.
# numbers = {1, 2, 3, 4, 5}
# print (type(numbers))

# Data type of Bool
## Boolean means True or false
# age = 2000
# if age > 2000:
#     print ("That's true!")
# else:
#     print ("That's false!")

# age = str(2000)
# print (type(age))

## Calculating the length of the data
# name = "John"

# print(len(name))


# unique_chars = set ("Hello")
# print (unique_chars)

## Operators in Python
# Operators are special symbols in Python that perform operations on variables and values. Python supports a variety of operators, including Arithmetic, Comparison, and Logical operators.#
# This is the addition operator
# x = 5
# y = 3
# print(x + y)  # Outputs: 8

# This is the multiplication operator
# x = 10
# y = 100
# print(x * y)  # Outputs: 1000

# This is the subtraction operator

# b = 10000
# r = 700
# # print(b - r) # Outputs: 9300
# print (b / r)

## The Modulus Operator
# h = 2
# t = 5

# print (h % t)

# Comparison Operators:
# Comparison operators compare two values and return a Boolean (True or False).

x = 5
y = 3
# # print(x == y)  # Outputs: False

#     #• Not Equal (!=):
# print(x != y)  # Outputs: True

   # • Greater Than (>):
# print(x > y)  # Outputs: True

# Less than (<):
# print(x < y)  # Outputs: False

   # • Greater Than or Equal To (>=):
# print(x >= y)  # Outputs: True
#     • Less Than or Equal To (<=):
# print(x <= y)  # Outputs: False

## LOOPS
# For Loop
# numbers = [1, 2, 3, 4, 5]
# for mum in numbers:
#     print(mum)

# While Loop

# num = 1
# while num <= 5:
#     break
# print (num + 1)
# num = 1
# while num <= 10:
#     print(num)
#     num += 1

## Functions

## Function naming/Definition

# This code defines a function called my_function that prints a greeting message to the user. 
# The function does not take any parameters and does not return any value. 
# It prints three lines of text: "Hello Loveth the trouble maker", "I hope this class penetrates your mind", and "Thank You!".
def my_function():
    """
    # Prints a greeting message to the user.
    Hello Loveth the trouble maker

    # This function does not take any parameters.

    # It prints a multi-line string that includes a greeting message and a thank you message.
    I hope this class penetrates your mind
    Thank You!
    
    This function does not return any value.
    
"""
    print("Hello Loveth the trouble maker")
    print("I hope this class penetrates your mind")
    print("Thank You!")

my_function()
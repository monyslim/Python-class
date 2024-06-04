# def add(a, b):
#     return a + b
          
# def subtract(a, b):
#     return a - b
          
# def multiply(a, b):
#     return a * b
          
# def divide(a, b):
#     if b != 0:
#        return a / b
#     else:
#         return "Error: Division by zero!"
# result = add(5, 3)
# print("Addition result:", result)
          
# result = subtract(8, 2)
# print("Subtraction result:", result)

# name = input("Enter your name: ")
# print("Hello, " + name + "!")

# Reading from a file
# with open("myfile.txt", "r") as f:
#     content = f.read()
# print(content)

# Writing to a file
with open("myfile.txt", "a+") as f:
    ## Move the cursor to the beginning of the file
    f.seek(0)

    # Read the existing content of the file
    existing_content = f.read()
    if existing_content:
        f.write("\nThis content will be appended on a new line.")
    else:
        f.write("This content will be appended on a new line.")
print("Existing content:", existing_content, "")
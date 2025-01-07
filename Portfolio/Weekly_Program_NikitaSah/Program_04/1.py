"""
1.	Functions are often used to validate input. Write a function 
    that accepts a single integer as a parameter and returns True if 
    the integer is in the range 0 to 100 (inclusive), or False otherwise. 
    Write a short program to test the function.
"""

def checkFunction(value):
    return True if 0 <= value <=100 else False

input_value = int(input("Enter the Value :"))
print(checkFunction(input_value))
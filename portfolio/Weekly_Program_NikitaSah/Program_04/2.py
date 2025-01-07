"""
2.	Write a function that has a single string as its parameter, 
    and returns the number of uppercase letters, and the number of 
    lowercase letters in the string. Test the function with a short program.
"""

upperCase = 0
lowerCase = 0

def checkFunction(characters):
    global upperCase, lowerCase
    for character in characters:
        if character.isupper():
            upperCase += 1
        elif character.islower():
            lowerCase += 1
    return [upperCase, lowerCase]


input_value = input("Enter the Value :")
output_Value = checkFunction(input_value)
print("UpperCase Letter :", output_Value[0], "\nLowerCase Letter :", output_Value[1])
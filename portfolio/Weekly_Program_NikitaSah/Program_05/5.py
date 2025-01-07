"""
5.	Last week you wrote a program that processed a collection of temperature 
    readings entered by the user and displayed the maximum, minimum, and mean. 
    Create a version of that program that takes the values from the command-line 
    instead. Be sure to handle the case where no arguments are provided!
"""

import sys
value = sys.argv[1:]

def strToInt(strList):
    value = []
    for string in strList:
        value.append(int(string))
    return value

if len(value) > 1:
    print("The Minimum temperature is ", min(value))
    print("The Maximum temperature is ", max(value))
    print(f"The Mean temperature is  {sum(strToInt(value))/len(value):.2f}")
else:
    print("Sufficient Value not Provided")
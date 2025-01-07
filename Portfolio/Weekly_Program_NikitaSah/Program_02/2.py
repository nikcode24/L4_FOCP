"""
Task 2:
 Write a program that prompts a user to enter a temperature in Celsius, and then
 displays the corresponding temperature in Fahrenheit.
 For Example:
 Enter a temperature in Celsius: 32.5
 32.5C is equivalent to 90.5F.
"""

celcius = float(input("Enter a temperature in Celcius: "))

fahren = (celcius * 1.8) + 32

print(f"{celcius}C is euivalent to {fahren}K")
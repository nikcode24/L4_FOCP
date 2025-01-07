"""
3. Over the summer, temperatures in Yorkshire reached 38.4C. Write a program that
    converts this value in Celsius to the equivalent temperature in Fahrenheit, and then
    displays both.
"""

print("-"*20)

# Given temperature in Celsius
temp_Celsius = 38.4

# Convert Celsius to Fahrenheit
fahrenheit = (temp_Celsius * 9/5) + 32
print(f"{temp_Celsius}C to the equivalent temperature in {fahrenheit:.2f}F")

print("-"*20)

# Convert back from Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit:.2f}F to the equivalent temperature in {celsius}C")

print("-"*20)
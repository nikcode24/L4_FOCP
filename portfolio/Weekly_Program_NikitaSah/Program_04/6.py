"""
6.	Write a program that takes a centigrade temperature and displays the equivalent 
    in Fahrenheit. The input should be a number followed by a letter C. The output 
    should be in the same format.
"""

# °F = °C × (9/5) + 32
# (°F - 32)*5/9 = °C × (9/5) + 32

def celsiusToFahrenheit(value):
    return value * (9/5) + 32

def fahrenheitToCelsius(value):
    return (value - 32)*5/9
    

celsius = float(input("Enter the Value in Celsius :")[:-1])
print(f"\n{celsius}C is equals to {celsiusToFahrenheit(celsius):.2f}F")
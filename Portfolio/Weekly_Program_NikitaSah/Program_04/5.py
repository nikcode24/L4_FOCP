"""
5.	Write and test a function that converts a temperature measured in degrees 
    centigrade into the equivalent in Fahrenheit, and another that does the reverse 
    conversion. Test both functions. (Google will find you the formulae).
"""

# °F = °C × (9/5) + 32
# (°F - 32)*5/9 = °C × (9/5) + 32

def celsiusToFahrenheit(value):
    return value * (9/5) + 32

def fahrenheitToCelsius(value):
    return (value - 32)*5/9
    

celsius = float(input("Enter the Value in Celsius :"))
fahrenheit = float(input("Enter the Value in Fahrenheit :"))
print(f"\n{celsius}C is equals to {celsiusToFahrenheit(celsius):.2f}F")
print(f"{fahrenheit}F is equals to {fahrenheitToCelsius(fahrenheit):.2f}C")
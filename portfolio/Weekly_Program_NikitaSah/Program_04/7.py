"""
7.	Write a program that reads 6 temperatures (in the same format as before), and 
    displays the maximum, minimum, and mean of the values. 
    Hint: You should know there are built-in functions for max and min. 
    If you hunt, you might also find one for the mean.
"""

temperature = []

print("Enter the Value Like 32C")
i = 0
while i < 6:
    input_value = input(f"Enter The Temperature {i+1} : ")
    if input_value[-1:].upper() == "C":
        temperature.append(int(input_value[:-1]))
        i += 1  # Move to the next iteration only if input is correct
    else:
        print("Invalid input! Please try again.")

print(f"Maximum Temperature : {max(temperature)}C")
print(f"Minimum Temperature :  {min(temperature)}C")
print(f"Mean Temperature    : {(sum(temperature)/len(temperature)):.2f}C")
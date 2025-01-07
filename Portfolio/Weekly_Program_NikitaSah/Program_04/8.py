"""
8.	Modify the previous program so that it can process any numberof values. The input 
    terminates when the user just pressed "Enter" at the prompt rather than 
    entering a value.
"""

def argFunction(*args):
    temperature = []
    listTuple = list(args)
    for item in listTuple:
        temperature.append(int(item[:-1]))
    return [max(temperature), min(temperature), (sum(temperature)/len(temperature))]

input_value = input("Enter the number :").split()
returnTemperature = argFunction(*input_value)

print(f"Maximum Temperature : {returnTemperature[0]}C")
print(f"Minimum Temperature : {returnTemperature[1]}C")
print(f"Mean Temperature    : {returnTemperature[2]:.2f}C")
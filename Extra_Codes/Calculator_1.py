# Task 1: Calculation Operation By Using Function(Calculator 1).

def calculator(num1,num2,operation):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        if (num2 == 0):
            return "Eroor: division by 0"
        return num1 / num2
    elif operation == 4:
        return num1 * num2
    elif operation == 5:        
        if num2 == 0:
            return "Error: Modulus by 0"
        return num1 % num2
    else:
        return "No any operation selected"

def main():
    while True:
        num1=float(input("Enter a Num1 : "))
        num2=float(input("Enter a Num2 : "))
        operation = int(input("Enter a Operation Number : "))
        ans = calculator(num1,num2,operation)
        print(ans)

        again = input("Are you sure to calculate again : yes/no ").lower()

        if again != "yes":
            break

if __name__ == "__main__":
    main()
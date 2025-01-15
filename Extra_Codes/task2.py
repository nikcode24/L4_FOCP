# Task 1: Calculation Operation By Using Function and try except for exception case(Calculator 1).

def calculator(num1,num2,operation):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        try:
            return num1 / num2
        except Exception as e:
            return e
    elif operation == 4:
        return num1 * num2
    elif operation == 5:        
        try:
            return num1 % num2
        except Exception as e:
            return e
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
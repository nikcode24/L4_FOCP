# Task 4: Calculator 2

def calculation():
    while True:
        operation = input("Please enter Operation: ")
        print(eval(operation))
        again = input("Are you sure to do Operation(Y/N)?: ").lower()
        if again != "yes":
            break

calculation()
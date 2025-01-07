# 2. Write a program that simulates the way in which a user might choose a password.
#  The program should prompt for a new password, and then prompt again. If the two
#  passwords entered are the same the program should say "Password Set" or
#  similar, otherwise it should report an error.

password = input("Enter a new password: ")
passwordConfirm = input("Enter a confirm new password: ")

if password == passwordConfirm:
    print("Password set Successfully")
else:
    print("Error: Passwords do not match. Please try again.")
# 3. Modify your previous program so that the password must be between 8 and 12
#  characters (inclusive) long.

password = str(input("Enter a new password: "))
passwordConfirm = str(input("Enter a confirm new password: "))

if (len(password) >= 8 and len(password) <= 12):
    if password == passwordConfirm:
        print("Password set Successfully !")
    else:
        print("Password Mismatched !")
else:
    print("Password must be between 8 to 12 Character !")
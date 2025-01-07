# 4. Modify your program again so that the chosen password cannot be one of a list of
#  common passwords, defined thus:

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password = str(input("Enter a new password: "))
passwordConfirm = str(input("Enter a confirm new password: "))

if len(password) >= 8 and len(password) <= 12:
    if password == passwordConfirm:
        if password not in BAD_PASSWORDS:
            print("Password set Successfully !")
        else:
            print("Common Password. Enter Random Password !")
    else:
        print("Password Mismatched !")
else:
    print("Password must be between 8 to 12 Character !")
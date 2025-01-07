# 5.  Modify your program a final time so that it executes until the user successfully
#  chooses a password. That is, if the password chosen fails any of the checks, the
#  program should return to asking for the password the first time.

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password = str(input("Enter a new password: "))
    passwordConfirm = str(input("Enter a confirm new password: "))

    if len(password) >= 8 and len(password) <= 12:
        if password == passwordConfirm:
            if password not in BAD_PASSWORDS:
                print("Password set Successfully !")
                break
            else:
                print("Common Password. Enter Random Password !")
        else:
            print("Password Mismatched !")
    else:
        print("Password must be between 8 to 12 Character !")
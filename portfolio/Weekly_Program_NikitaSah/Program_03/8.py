# 8. Modify the "Times Table" again so that the user still enters the number of the table,
#  but if this number is negative the table is printed backwards. So entering "-7"
#  would produce the Seven Times Table starting at "12 times" down to "0 times".

number = int(input("Enter a number for the table: "))

if number >= 0:
    for i in range (0,13):
        print(f"{i} x {number} = {i * number}")
        i+=1
else:
    for i in range (12, -1, -1):
        print(f"{i} x {number} = {i * number}")
        i+=1

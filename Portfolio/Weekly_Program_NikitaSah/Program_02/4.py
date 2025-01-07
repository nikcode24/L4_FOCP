"""
Task 4:
 A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
 first count the sweets and then divide them according to how many pupils attend
 that day. Write a program that will tell the teacher how many sweets to give to each
 pupil, and how many she will have left over.
"""

numberOfSweets = int(input("Number of Sweets in tub: "))
numberOfPupils = int(input("Number of pupils: "))

giveSweet = numberOfSweets // numberOfPupils
sweetLeftOver = numberOfSweets % numberOfPupils

if giveSweet <= 1 and sweetLeftOver <= 1:
    print(f"{giveSweet} Sweet to give to each pupil and {sweetLeftOver} sweet will be left over")

elif giveSweet <= 1 and sweetLeftOver > 1:
    print(f"{giveSweet} Sweet to give to each pupil and {sweetLeftOver} sweets will be left over")

elif giveSweet > 1 and sweetLeftOver <= 1:
    print(f"{giveSweet} Sweets to give to each pupil and {sweetLeftOver} sweet will be left over")

elif giveSweet > 1 and sweetLeftOver > 1:
    print(f"{giveSweet} Sweets to give to each pupil and {sweetLeftOver} sweets will be left over")

else:
    print("Invalid Give and left over Sweets")
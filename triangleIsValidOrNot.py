# Write a Python program to input side of a triangle and check whether triangle is valid or not using if else.
# How to check whether a triangle can be formed or not if sides of triangle is given using if else in python programming.
# Logic to check triangle validity if sides are given in python program.

inputFirstSide = float(input('Enter Your First Side Value: '))
inputSecondSide = float(input('Enter Your First Side Value: '))
inputThirdSide = float(input('Enter Your First Side Value: '))

a = inputFirstSide
b = inputSecondSide
c = inputThirdSide

if a + b > c and a + c > b and b + c > a :
    print("Triangle is valid")
else : print("Triangle is not valid")

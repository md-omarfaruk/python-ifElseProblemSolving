# Write a Python program to find all roots of a quadratic equation using if else.
# How to find all roots of a quadratic equation using if else in Python programming.
# Logic to find roots of quadratic equation in Python programming.

import math

a = float(input('Input value of a: '))
b = float(input('Input value of b: '))
c = float(input('Input value of c: '))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    r1 = -b + math.sqrt(discriminant) / (2*a)
    r2 = -b - math.sqrt(discriminant) / (2*a)

elif discriminant == 0:
    r1 = r2 = -b / (2*a)

elif discriminant < 0:
    r1 = -b / (2*a)
    r2 = -b / (2*a)
imaginary = math.sqrt(discriminant) / (2*a)

print(r1, r2, imaginary)


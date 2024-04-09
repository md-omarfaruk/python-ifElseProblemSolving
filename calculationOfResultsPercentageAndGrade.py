# Write a PYTHON program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade 
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F


percentageOfMark = float(input('Enter The Percentage Number Of Your Mark: '))

if percentageOfMark >= 90 and percentageOfMark <= 100 :
    print("Grade A")
elif percentageOfMark >= 80:
    print("Grade B")
elif percentageOfMark >= 70:
    print("Grade C")
elif percentageOfMark >= 60:
    print("Grade D")
elif percentageOfMark >= 40:
    print("Grade E")
elif percentageOfMark < 40:
    print("Grade F")

    # SOLVED
# Write a PYTHON program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

	

units = float(input('type a integer number: '))

if units >= 0 and units <= 50:
    subBill = units * 0.50
    totalBill = subBill + subBill/100*20
    print(totalBill)
elif units >= 51 and units <= 100:
    subBill = units * 0.75
    totalBill = subBill + subBill/100*20
    print(totalBill)
elif units >= 101 and units <= 200:
    subBill = units * 1.20
    totalBill = subBill + subBill/100*20
    print(totalBill)
elif units >= 250 :
    subBill = units * 1.50
    totalBill = subBill + subBill/100*20
    print(totalBill)


    # SOLVED
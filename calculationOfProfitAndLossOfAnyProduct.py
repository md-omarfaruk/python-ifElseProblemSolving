# Write a python program to input cost price and selling price of a product and check profit or loss.
# Also calculate total profit or loss using if else.
# How to calculate profit or loss on any product using if else in python programming.
# Program to calculate profit and loss of any product in python.


costPrice = float(input('Input cost price: '))
sellingPrice = float(input('Input selling price: '))

if sellingPrice > costPrice:
    profit = sellingPrice - costPrice
    print('Profit: ', profit)
elif sellingPrice < costPrice:
    loss = costPrice - sellingPrice
    print('Loss: ', loss)

    # SOLVED
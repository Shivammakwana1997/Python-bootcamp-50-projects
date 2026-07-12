'''
you sell diffrent chai sizes

instead pf writing formulas everywhere , create a function 

task 

write calculate_bill(cups,price_per_cup)

return total bill

use this function for multiple orders

'''

def calculate_bill(cups,price_per_cup):
    total = cups * price_per_cup
    return total



order1 = calculate_bill(3,30)
print("Order 1 : ",order1)

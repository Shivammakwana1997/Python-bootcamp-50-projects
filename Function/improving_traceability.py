'''

your shop addd a 10% vat one everyorder
you want this to be consistent and traceable

task:
write add_vat(price,vat_price)
use it to compute final prices for a 3 orders

'''


def add_vat(price,vat_price=10):
    return price * (100+vat_price)/100 

orders = [100,150,200]


for price in orders:
    final_amount = add_vat(price,10)
    print(f"Price {price} with VAT: {final_amount}")
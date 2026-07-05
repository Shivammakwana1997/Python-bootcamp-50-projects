def delivery_wavier(order_amount: int, delivery_fee = 0) -> int:
    if order_amount >= 300:
        return 0
    else:
        return delivery_fee

print(delivery_wavier(450, 40))
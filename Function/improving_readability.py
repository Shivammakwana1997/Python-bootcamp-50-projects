'''
Improving Readability with Functions
-------------------------------------
You sell different chai sizes.
Instead of writing formulas everywhere, create a reusable function.

Task:
  Write calculate_bill(cups, price_per_cup)
  - Return total bill
  - Use this function for multiple orders
'''

# Function to calculate the total bill based on number of cups and price per cup
def calculate_bill(cups, price_per_cup):
    total = cups * price_per_cup  # Multiply cups by price to get total
    return total  # Return the calculated bill


# Order 1: 3 cups at ₹30 each
order1 = calculate_bill(3, 30)
print("Order 1 : ", order1)  # Output: 90

# Order 2: 5 cups at ₹25 each
order2 = calculate_bill(5, 25)
print("Order 2 : ", order2)  # Output: 125

# Order 3: 2 cups at ₹50 each
order3 = calculate_bill(2, 50)
print("Order 3 : ", order3)  # Output: 100


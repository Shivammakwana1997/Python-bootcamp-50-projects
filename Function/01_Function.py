# ============================================================
# Section 5 - Functions in Python
# ============================================================

# -----------------------------------------------
# What is a Function?
# A function is a reusable block of code that
# performs a specific task.
#
# Syntax:
#   def function_name(parameters):
#       body
#       return value
# -----------------------------------------------

# -----------------------------------------------
# 1. Basic Function (no parameters)
# -----------------------------------------------

def greet():
    print("Namaste! Welcome to Chai Order System ☕")

greet()

# -----------------------------------------------
# 2. Function with Parameters
# -----------------------------------------------

def print_order(name, chai_type):
    print(f"Order placed for {name} → {chai_type}")

print_order("Shivam", "Masala Chai")
print_order("Hitesh", "Ginger Chai")

# -----------------------------------------------
# 3. Function with Default Parameter
# -----------------------------------------------

def make_chai(chai_type="Masala Chai", cups=1):
    print(f"Making {cups} cup(s) of {chai_type}")

make_chai()                          # uses defaults
make_chai("Ginger Chai", 2)         # custom values

# -----------------------------------------------
# 4. Function with Return Value
# -----------------------------------------------

def calculate_bill(price, cups):
    total = price * cups
    return total

bill = calculate_bill(30, 3)
print(f"Total Bill: ₹{bill}")

# -----------------------------------------------
# 5. Function with *args (multiple arguments)
# -----------------------------------------------

def order_items(*items):
    print("Items ordered:")
    for item in items:
        print(f"  - {item}")

order_items("Masala Chai", "Samosa", "Biscuit")

# -----------------------------------------------
# 6. Function with **kwargs (keyword arguments)
# -----------------------------------------------

def user_info(**details):
    print("User Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

user_info(name="Shivam", city="Surat", cups_per_day=4)
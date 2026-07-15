'''
Avoiding Code Duplication with Functions
------------------------------------------
Instead of repeating print statements for every order,
we define a reusable function print_order() that handles
the logic once and can be called multiple times.

Benefit: If we need to change the format, we only change it in ONE place.
'''

# Reusable function to print a chai order
# Parameters:
#   name      - the customer's name
#   chai_type - the type of chai ordered
def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai")  # Formatted output


# Calling the function for a sample order (avoids copy-pasting print statements)
print_order("Aman", "Masala")
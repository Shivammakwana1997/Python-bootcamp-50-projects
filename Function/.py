'''
Scopes and Name Resolution (LEGB Rule)
----------------------------------------
Python looks up variable names in this order:
  L - Local    : inside the current function
  E - Enclosing: outer function scope (for nested functions)
  G - Global   : top-level of the script/module
  B - Built-in : Python's built-in names (print, len, etc.)
'''


# --- GLOBAL SCOPE example ---
def serve_chai():
    chai_type = "Masala"  # Local variable - exists only inside this function
    print(f"Inside function: {chai_type}")  # Reads local 'chai_type'


chai_type = "Lemon"  # Global variable - accessible throughout the module

serve_chai()  # Calls function -> prints "Masala" (local takes priority)

print(f"Outside function: {chai_type}")  # Prints global "Lemon" - unaffected by local


# --- ENCLOSING SCOPE example (nested functions) ---
def chai_counter():
    chai_order = "Lemon"  # Enclosing scope variable

    def print_order():
        # Reads 'chai_order' from enclosing (outer) function - LEGB: E
        print(f"Order: {chai_order}")

    print_order()  # Inner function can access enclosing scope


chai_counter()  # Output: Order: Lemon
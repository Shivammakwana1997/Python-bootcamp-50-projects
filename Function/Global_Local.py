"""
=============================================================
  Topic     : Python Variable Scopes - Global vs Local
  Section   : Functions → Scope & Closures
  File      : Global_Local.py
  Author    : Shivam Makwana
  Date      : 2026-07-18
=============================================================

  LEGB Rule (Python Scope Resolution Order):
  ------------------------------------------
  L - Local      → Variables defined inside the current function
  E - Enclosing  → Variables in the enclosing (outer) function scope
  G - Global     → Variables defined at the module (top) level
  B - Built-in   → Python's built-in names (len, print, etc.)

=============================================================
"""


# ── DEMO 1: Local vs Global Variable ─────────────────────────────────────────
# When a variable with the same name exists in both local and global scope,
# the local scope always takes priority inside the function.

def serve_chai():
    chai_type = "Masala"  # Local variable — only lives inside this function
    print(f"inside function {chai_type}")


chai_type = "lemon"  # Global variable — lives at module level
serve_chai()
print(f"Outside function: {chai_type}")  # Global value remains unchanged


# ── DEMO 2: Enclosing Scope (Nested Functions) ────────────────────────────────
# The inner function has its own local scope.
# Modifying a variable in the inner function does NOT affect the outer function's
# variable — because each creates its own local binding.

def chai_counter():
    chai_order = "lemon"  # Outer (enclosing) function's variable

    def print_order():
        chai_order = "ginger"  # Inner function creates its own local copy
        print("inner :", chai_order)  # Prints: ginger

    print_order()
    print("Outer: ", chai_order)  # Still prints: lemon  (enclosing scope unchanged)

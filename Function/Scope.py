"""
=============================================================
  Topic     : Python Nested Scope — Enclosing vs Global
  Section   : Functions → Scope & Closures
  File      : Scope.py
  Author    : Shivam Makwana
  Date      : 2026-07-18
=============================================================

  Demonstrates how Python resolves names across three levels:
    • Global scope  → module-level variable
    • Enclosing scope → outer function variable
    • Local scope   → inner function variable

  Key Concept:
  Without `nonlocal`, reassigning inside a nested function
  creates a NEW local variable and does NOT touch the outer one.

=============================================================
"""


def chai_counter():
    chai_order = "lemon"  # Enclosing scope variable

    def print_order():
        chai_order = "ginger"  # Creates a NEW local variable (does not modify outer)
        print("inner :", chai_order)  # Output: ginger

    print_order()
    print("Outer: ", chai_order)  # Output: lemon (enclosing scope unchanged)


# ── Entry Point ───────────────────────────────────────────────────────────────
chai_order = "masala"  # Global scope variable
chai_counter()
print("global :", chai_order)  # Output: masala (global scope unchanged)

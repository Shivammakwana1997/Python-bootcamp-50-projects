# =============================================================
# 📘 CHAPTER 1 — Mutable vs Immutable | Identity of Variables
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# Imagine your variable is a "label on a box".
#
# IMMUTABLE (like int, str, float):
#   When you change the value, Python does NOT edit the old box.
#   Instead, it creates a BRAND NEW box and sticks the label on it.
#   → That's why the id() (memory address) CHANGES after update!
#
# MUTABLE (like list, set, dict):
#   When you change the value, Python edits the SAME box.
#   → The id() stays the SAME even after you add/remove items.
#
# id() = Python's way of showing the memory address (like a home address)
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Why does id() change when we reassign an integer?
# ✅ ANSWER  : Because integers are IMMUTABLE. Python doesn't modify 
#              the original object. It creates a new one at a new address.

### MMutable is always working with identity not value 

# 🔹 Step 1: Creating a variable with value 10
sugar_amount = 10
print(f"Initial sugar amount: {sugar_amount}")   # Prints 10
print(type(sugar_amount))                         # Shows: <class 'int'>
print(id(sugar_amount))                           # Memory address of 10

# 🔹 Step 2: Reassigning to 20 → Python creates a NEW object!
sugar_amount = 20
print(f"Updated sugar amount: {sugar_amount}")   # Prints 20
print(type(sugar_amount))                         # Still <class 'int'>
print(id(sugar_amount))                           # ← DIFFERENT address than before!

# 💡 KEY TAKEAWAY:
#    Same variable name (sugar_amount) → but pointing to a DIFFERENT memory location
#    This proves: integers are IMMUTABLE in Python

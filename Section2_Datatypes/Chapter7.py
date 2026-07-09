# =============================================================
# 📘 CHAPTER 7 — Tuple | Immutable Ordered Collection
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# TUPLE = a fixed list that CANNOT be changed after creation
# Written in ( ) round brackets
#
# Think of it like a SEALED SPICE BOX:
#   → You can SEE what's inside (read values)
#   → But you CANNOT add, remove, or change the spices!
#   → It's permanent/immutable
#
# WHY USE TUPLES?
#   → When data should NOT be changed (like coordinates, config)
#   → Faster than lists
#   → Can be used as dictionary keys (lists cannot!)
#
# TUPLE UNPACKING:
#   → Assign each element of a tuple to a separate variable
#   → (a, b, c) = (1, 2, 3) → a=1, b=2, c=3
#
# SWAPPING VARIABLES:
#   → Python lets you swap in ONE line using tuple syntax!
#   → a, b = b, a  ← no temp variable needed!
#
# MEMBERSHIP CHECK:
#   → "item" in tuple → True if item exists in the tuple
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What is the difference between a Tuple and a List?
# ✅ ANSWER  : List → mutable (can be changed), uses []
#              Tuple → immutable (cannot be changed), uses ()

# ❓ QUESTION: How does Python swap two variables without a temp variable?
# ✅ ANSWER  : It uses tuple packing/unpacking behind the scenes.
#              a, b = b, a → Python packs (b, a) into a tuple first,
#              then unpacks into a and b.

'''
Tuple Datatypes
Tuple are immutable and are always written in () brackets
and is used when we want to store data that we don't want to change so tuple is immutable
'''

import typing_extensions
import typing_extensions

# 🔹 Creating a Tuple — a sealed masala blend recipe (fixed, won't change)
masala_blend = ("Cardamom", "Cinnamon", "Ginger", "Clove")
print(f"Masala Blend: {masala_blend}")             # All 4 spices in the tuple

# 🔹 TUPLE UNPACKING — assign each spice to its own variable
(spice1, spice2, spice3, spice4) = masala_blend    # Unpack all 4 values
print(f"Spice 1: {spice1}")   # Cardamom
print(f"Spice 2: {spice2}")   # Cinnamon
print(f"Spice 3: {spice3}")   # Ginger
print(f"Spice 4: {spice4}")   # Clove

# 🔹 VARIABLE SWAPPING using tuple syntax (no temp variable needed!)
ginger_ratio , cadramom_ratio = 2,1                # ginger=2, cardamom=1
print(f"Ginger Ratio: {ginger_ratio} and cadramom_ratio : {cadramom_ratio}")

ginger_ratio , cadramom_ratio  = cadramom_ratio, ginger_ratio  # SWAP! ← magic line
print(f"Ginger Ratio: {ginger_ratio} and cadramom_ratio : {cadramom_ratio}")
# Now ginger=1, cardamom=2 (values swapped!)

###membership 

# 🔹 MEMBERSHIP CHECK — is "masala" in the tuple?
print(f"Is ginger present in masala spices ? {"masala" in masala_blend}")
# "masala" is NOT in the tuple (exact match needed!) → False

# 💡 KEY TAKEAWAY:
#    Tuples are like READ-ONLY lists. Perfect for data that should never change.
#    Unpacking lets you assign multiple values in one clean line.

# =============================================================
# 📘 CHAPTER 9 — Set | Unordered, No Duplicates
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# SET = an unordered collection of UNIQUE items
# Written in { } curly braces (but no key:value pairs like dict!)
#
# Think of a Set like a SPICE RACK:
#   → No duplicates allowed — if you add "Ginger" twice, only one stays
#   → No fixed order — items appear randomly each time
#   → Great for SET OPERATIONS (like math sets!)
#
# SET OPERATIONS (math set theory in Python!):
#   .union(other)        → ALL items from BOTH sets (A ∪ B)
#   .intersection(other) → ONLY items in BOTH sets (A ∩ B)
#   A - B               → Items in A but NOT in B (A - B)
#   "item" in set       → Check if item exists (True/False)
#
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What happens if you add a duplicate to a set?
# ✅ ANSWER  : Python silently IGNORES it! No error.
#              {1, 2, 2, 3} → {1, 2, 3} (only unique values kept)

# ❓ QUESTION: What is the difference between union and intersection?
# ✅ ANSWER  : 
#   union()        → combines BOTH sets (all unique items from both)
#   intersection() → only items that APPEAR IN BOTH sets

'''
Set :- 
is a mutable data structure that is used to store multiple values in a single variable
Sets are unordered and do not allow duplicate values
They are defined using curly braces {}
'''

# 🔹 Create Set 1 — essential spices (must have in chai)
essential_spices = {"cardamom", "Ginger", "clove"}
print(f"Essential spices: {essential_spices}")          # Order may vary each run!

print(f"Type of essential spices: {type(essential_spices)}")  # <class 'set'>


# 🔹 Create Set 2 — optional spices (nice to have)
# Note: "Ginger" appears in BOTH sets!
optional_spices = {"black papper","fennel","Ginger"}                                    


# 🔹 UNION — combine both sets (all unique spices from both)
all_spices =  optional_spices.union(essential_spices)   # A ∪ B
print(f"all spices: {all_spices}")                      # All spices, no duplicates


# 🔹 INTERSECTION — only spices in BOTH sets
common_spices = optional_spices.intersection(essential_spices)  # A ∩ B
print(f"common spices: {common_spices}")                # Only "Ginger" (in both!)

# 🔹 DIFFERENCE — spices ONLY in essential (not in optional)
only_reserach = essential_spices - optional_spices      # A - B

print(f"only reserach spices: {only_reserach}")         # cardamom & clove (not in optional)


# 🔹 MEMBERSHIP CHECK — is Ginger in our essential set?
print(f"is ginger present in essential spices? {"Ginger" in essential_spices}")  # True

# 💡 KEY TAKEAWAY:
#    Sets are perfect when you need UNIQUE values and SET OPERATIONS.
#    Use set() when removing duplicates from a list: list(set(my_list))

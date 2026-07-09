# =============================================================
# 📘 CHAPTER 2 — Mutable Objects | Sets Stay at Same Address
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# Think of a SET like a BASKET.
# You can throw more items into the basket (add spices),
# but the BASKET ITSELF does not change — same basket, new items.
#
# That's why:
#   → id() BEFORE adding spices  == id() AFTER adding spices
#   → The memory address does NOT change!
#   → This proves: Sets are MUTABLE in Python
#
# MUTABLE = the object can be changed IN PLACE (same memory box)
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: If we add items to a set, does its id() change?
# ✅ ANSWER  : NO! Because sets are MUTABLE. Python edits the same
#              object in memory — the address stays the same.

# 🔹 Step 1: Create an empty set (like an empty spice basket)
spice_mix = set()

print(f"Initial spice mix id: {id(spice_mix)}")  # Check address BEFORE adding

# 🔹 Step 2: Adding spices one by one INTO the same set
spice_mix.add("Ginger")      # Spice 1 added
spice_mix.add("Cinnamon")    # Spice 2 added
spice_mix.add("Cardamom")    # Spice 3 added


print(f"Updated spice mix id: {id(spice_mix)}")  # Address is STILL the same!

# 💡 KEY TAKEAWAY:
#    The id() before and after adding items is IDENTICAL
#    → Sets are MUTABLE: items can be added/removed without creating a new object

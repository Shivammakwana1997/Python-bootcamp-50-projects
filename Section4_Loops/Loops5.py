# =============================================================
# 📘 LOOPS 5 — zip() | Loop Over Two Lists Together
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# zip() — pairing two (or more) lists together element by element
#
# Think of a zip as a PHYSICAL ZIPPER on your jacket:
#   Left side  = names  ["Shivam", "Rahul", "Abhi", "Hitesh", "Nikhil"]
#   Right side = bills  [100,       200,     300,    400,      500]
#   Zipped     = pairs  [("Shivam",100), ("Rahul",200), ...]
#
# zip(names, bills) creates pairs:
#   → ("Shivam", 100)
#   → ("Rahul", 200)
#   → ("Abhi", 300)
#   → ("Hitesh", 400)
#   → ("Nikhil", 500)
#
# for i, j in zip(names, bills):
#   → i = name from first list
#   → j = bill amount from second list
#   (both come out together, in sync!)
#
# IMPORTANT: zip stops at the SHORTEST list!
#   If one list has 3 items and other has 5 → only 3 pairs created.
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What happens if the two lists have different lengths?
# ✅ ANSWER  : zip() stops when the SHORTER list runs out.
#              Extra items in the longer list are IGNORED.
#              Use itertools.zip_longest() if you want all items.

# ❓ QUESTION: Can zip() work with more than 2 lists?
# ✅ ANSWER  : YES! zip(a, b, c) creates 3-element tuples.
#              for x, y, z in zip(a, b, c): works perfectly!

# 🔹 Two parallel lists — customer names and their bills
names = ["Shivam","Rahul","Abhi","Hitesh","Nikhil"]
bills = [100,200,300,400,500]


# 🔹 Pair them up using zip() and loop through together
for i , j in zip(names,bills):
    print(f"{i} has to pay {j}Rs")      # "Shivam has to pay 100Rs", etc.


# 💡 KEY TAKEAWAY:
#    zip() pairs two lists together like a zipper.
#    Perfect for parallel data: names+scores, items+prices, etc.
#    Stops at the shortest list — make sure lengths match for full data!

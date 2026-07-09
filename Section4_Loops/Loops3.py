# =============================================================
# 📘 LOOPS 3 — For Loop Iterating Over a List
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# FOR LOOP OVER A LIST — process each item one by one
#
# Instead of range(), we can loop directly over a LIST!
#
# Think of it like a chai order queue:
#   → Orders list = ["Shivam", "Rahul", "Abhi", "Hitesh", "Nikhil"]
#   → For each name in the queue → confirm their order
#
# for name in orders:
#   → name takes each value from the list, ONE at a time
#   → 1st: name="Shivam", 2nd: name="Rahul", ..., 5th: name="Nikhil"
#
# This is more PYTHONIC than using range(len(list)) — preferred style!
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Why loop over a list directly instead of using range(len(list))?
# ✅ ANSWER  : Direct iteration (`for name in orders`) is cleaner, more readable,
#              and more Pythonic. Only use range(len()) when you NEED the index number.

# ❓ QUESTION: What does "iterating" mean?
# ✅ ANSWER  : Iterating = going through a collection item by item.
#              Every time the loop runs = one "iteration".

# 🔹 A list of customer names who placed orders
orders = ["Shivam","Rahul","Abhi","Hitesh","Nikhil"]


# 🔹 Loop through each name and print order confirmation
for name in orders:
    print("Order recived for:",name)    # Runs 5 times: once per name

    
# 💡 KEY TAKEAWAY:
#    You can loop over ANY list (or string, tuple, set, dict) directly.
#    `for item in collection:` is the most Pythonic way to iterate.
#    No index needed unless you specifically want position numbers.

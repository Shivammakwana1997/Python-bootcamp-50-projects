# =============================================================
# 📘 LOOPS 4 — enumerate() | Loop with Index + Value
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# enumerate() — gives you BOTH the index AND the value together!
#
# Normal loop: `for item in menu:` → gives VALUE only
# enumerate: `for index, item in enumerate(menu):` → gives INDEX + VALUE
#
# Think of a numbered menu at a restaurant:
#   0 → Green Tea
#   1 → Masala Chai
#   2 → Iced Tea
#
# enumerate(menu) produces:
#   (0, "Greentea"), (1, "Masalachai"), (2, "Iced Tea")
#   ↑ tuple of (index, value)
#
# We UNPACK the tuple: for index, item in enumerate(menu)
#   → index = the position number (0, 1, 2...)
#   → item  = the actual value at that position
#
# TIP: Start from 1 instead of 0:
#   enumerate(menu, start=1) → (1, "Greentea"), (2, "Masalachai"), ...
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Why use enumerate() instead of range(len(menu))?
# ✅ ANSWER  : enumerate() is cleaner and more Pythonic.
#              range(len(menu)) works but is harder to read.
#              enumerate() was created specifically for this use case!

# ❓ QUESTION: What does "unpacking" mean in the for loop?
# ✅ ANSWER  : enumerate() returns pairs like (0, "Greentea").
#              Writing `for index, item` separates (unpacks) that pair
#              into two variables automatically.

# 🔹 A menu list with 3 items
menu = ["Greentea","Masalachai","Iced Tea"]

# 🔹 Loop with enumerate → get both index and item name
for index , item in enumerate(menu):
    print("item number:",index,"item name:",item)
    # Output:
    # item number: 0 item name: Greentea
    # item number: 1 item name: Masalachai
    # item number: 2 item name: Iced Tea

# 💡 KEY TAKEAWAY:
#    enumerate() = index + value together, in every iteration
#    Perfect for numbered menus, ranked lists, or when you need position info
#    Use enumerate(list, start=1) if you want counting to start from 1

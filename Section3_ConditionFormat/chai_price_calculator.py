# =============================================================
# 📘 PROJECT 1 — Chai Price Calculator
# 📚 Section  : 3 — Conditions & Control Flow
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# IF / ELIF / ELSE — Decision Making in Python
#
# Think of it like a MENU BOARD at a chai stall:
#   → Customer asks for "small" → charge 10
#   → Customer asks for "medium" → charge 20
#   → Customer asks for "large" → charge 30
#   → Customer asks something else → "Invalid cup size"
#
# HOW IT WORKS:
#   if  → check FIRST condition
#   elif → check NEXT condition (only if first was False)
#   else → runs when ALL above conditions are False
#
# .lower() → converts input to lowercase
#   So "SMALL", "Small", "small" all become "small"
#   This prevents case-sensitivity issues in user input
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Why do we use .lower() on the input?
# ✅ ANSWER  : User might type "Small" or "SMALL" or "small".
#              Without .lower(), only "small" would match.
#              .lower() makes all versions equal → better user experience.

# ❓ QUESTION: What is elif? Can we use multiple elif?
# ✅ ANSWER  : elif = "else if" → checks another condition if previous was False.
#              YES! You can have as many elif blocks as you need.

# 🔹 Take input from user and convert to lowercase for safe comparison
cup = input("choose your cup size (small/medium/large) : ").lower()

# 🔹 Check which size was chosen and print the price
if cup == "small":
    print("Price is : 10")         # Small cup → 10 Rs

elif cup == "medium":
    print("Price is : 20")         # Medium cup → 20 Rs

elif cup == "large":
    print("Price is : 30")         # Large cup → 30 Rs

else:
    print("Invalid cup size")      # None of the above → invalid input
    

# 💡 KEY TAKEAWAY:
#    if/elif/else is Python's way of making decisions.
#    Always use .lower() or .upper() on user input to avoid case mismatch.

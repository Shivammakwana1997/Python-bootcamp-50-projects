# =============================================================
# 📘 PROJECT 6 — Train Seat Booking System
# 📚 Section  : 3 — Conditions & Control Flow
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# MATCH / CASE — Python's Switch Statement (added in Python 3.10+)
#
# match/case is like a MULTI-WAY SIGNBOARD:
#   → "sleeper"  → ₹500
#   → "ac"       → ₹800
#   → "non-ac"   → ₹300
#   → "luxary"   → ₹1200
#
# It's similar to if/elif/elif/elif BUT:
#   → CLEANER and more readable for multiple fixed options
#   → Works great when comparing ONE variable to MANY exact values
#   → Python 3.10+ ONLY (won't work on older Python versions!)
#
# HOW IT WORKS:
#   match variable:
#       case "value1": → do this
#       case "value2": → do this
#       case _:        → default (like else) — we haven't used it here
#
# NOTE: We use .lower() so "AC", "Ac", "ac" all match "ac"
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What is match/case and when to use it?
# ✅ ANSWER  : match/case is Python's structural pattern matching.
#              Use it when you have ONE value to compare against MANY 
#              fixed options. Cleaner than long if/elif chains.

# ❓ QUESTION: What does case _: do?
# ✅ ANSWER  : _ is the "wildcard" — matches ANYTHING that didn't match above.
#              It's the match/case version of `else`.
#              (We haven't used it here, but it's good to know!)

# 🔹 Get seat type from user, convert to lowercase
seat_type = input("Enter seat type (sleeper/ac/non-ac/luxary):").lower()

# 🔹 Match the seat type and print the price
match seat_type:
    case "sleeper":
        print("Price is : 500")         # Sleeper class → ₹500
    case "ac":
        print("Price is : 800")         # AC class → ₹800
    case "non-ac":
        print("Price is : 300")         # Non-AC → ₹300
    case "luxary":
        print("Price is : 1200")        # Luxury class → ₹1200

# 💡 KEY TAKEAWAY:
#    match/case = cleaner alternative to long if/elif chains.
#    Only available in Python 3.10 and above.
#    Add `case _: print("Invalid seat type")` to handle wrong inputs!

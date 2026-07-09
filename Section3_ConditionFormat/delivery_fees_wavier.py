# =============================================================
# 📘 PROJECT 2 — Delivery Fee Waiver System
# 📚 Section  : 3 — Conditions & Control Flow
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# FUNCTIONS WITH TYPE HINTS & DEFAULT PARAMETERS
#
# Think of this like a Swiggy/Zomato rule:
#   → Order ≥ ₹300 → FREE delivery (delivery fee = 0)
#   → Order < ₹300 → Pay the delivery fee
#
# WHAT'S NEW HERE?
#   1. Type Hints → order_amount: int, -> int
#      These tell US (and tools) what TYPE of data to expect.
#      Python doesn't FORCE them, but they improve readability.
#
#   2. Default Parameter → delivery_fee = 0
#      If caller doesn't pass delivery_fee, it defaults to 0.
#      So delivery_wavier(500) would work with fee = 0.
#
#   3. Return Value → the function RETURNS a number (not just prints)
#      Caller gets the value back and can use it however they want.
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What are type hints in Python?
# ✅ ANSWER  : They are HINTS (not strict rules) telling what type 
#              a parameter/return should be. Tools like VS Code use 
#              them for autocomplete and warnings. Python ignores them at runtime.

# ❓ QUESTION: What is a default parameter?
# ✅ ANSWER  : A value used automatically if the caller doesn't provide one.
#              delivery_fee = 0 means → if not specified, fee defaults to 0.

def delivery_wavier(order_amount: int, delivery_fee = 0) -> int:
    # 🔹 If order is 300 or more → waive the delivery fee (return 0)
    if order_amount >= 300:
        return 0                        # FREE delivery! 🎉

    else:
        return delivery_fee             # Charge the normal delivery fee

# 🔹 Test: Order of 450 Rs with 40 Rs delivery fee
# Since 450 >= 300 → fee should be WAIVED → returns 0
print(delivery_wavier(450, 40))         # Output: 0

# 💡 KEY TAKEAWAY:
#    Functions RETURN values that can be used later.
#    Default parameters make functions flexible — not all args are required.
#    Type hints make code self-documenting and easier to understand.

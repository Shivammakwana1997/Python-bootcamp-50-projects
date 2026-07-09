# =============================================================
# 📘 CHAPTER 4 — Boolean & None Data Types
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# BOOLEAN (bool):
#   Only 2 possible values → True or False
#   Think of it like a light switch: ON (True) or OFF (False)
#
#   🔥 TRICK: In Python, True = 1 and False = 0 (behind the scenes!)
#   So you can actually do MATH with booleans!
#   Example: 5 + True = 5 + 1 = 6
#            5 + False = 5 + 0 = 5
#
# NONE:
#   None means "nothing", "empty", "no value assigned yet"
#   It's like an empty cup — the cup exists, but has NO tea in it.
#   bool(None) = False (because empty = false!)
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Can we use True/False in arithmetic?
# ✅ ANSWER  : YES! Python treats True as 1 and False as 0.
#              stri_count + is_boiling = 5 + 1 = 6

# ❓ QUESTION: What is None and why is bool(None) = False?
# ✅ ANSWER  : None = no value. Python treats "nothing" as False.
#              Just like 0 is falsy, None is also falsy.

# 🔹 Boolean example — is the kettle boiling? (True = yes, it's boiling)
is_boiling = True
stri_count = 5

# True acts as 1 here → 5 + 1 = 6 total actions
total_action = stri_count + is_boiling
print(f"Total action: {total_action}")             # Output: 6


# 🔹 None example — is there milk? No → None means empty/absent
milk_present = None
print(f"Is there milk?: {bool(milk_present)}")     # Output: False

# 💡 KEY TAKEAWAY:
#    True  = 1 (truthy)
#    False = 0 (falsy)
#    None  = nothing, treated as False when converted to bool

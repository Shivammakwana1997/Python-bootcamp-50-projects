# =============================================================
# 📘 PROJECT 5 — Snack Suggestion System
# 📚 Section  : 3 — Conditions & Control Flow
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# FUNCTION WITH TYPE HINT (but wrong type hint here — learning moment!)
#
# The function checks if a snack is available or not.
# If the snack is "Burger" → "Yes available"
# Otherwise → "not available"
#
# ⚠️ TYPE HINT MISMATCH (a bug to learn from):
#   def snack_Suggestion(snack: int) -> str:
#   The hint says `snack` should be an int, but we're passing a STRING!
#   Python doesn't crash because type hints are just HINTS, not enforced.
#   But this is BAD practice — the hint should say `str` not `int`.
#
# NAMING CONVENTION NOTE:
#   Function names should ideally be snake_case: snack_suggestion
#   PascalCase (snack_Suggestion) is used for CLASS names, not functions.
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Does Python enforce type hints?
# ✅ ANSWER  : NO! Type hints are just for HUMANS and tools (like mypy, VS Code).
#              Python runs the code regardless. But following correct hints
#              is good practice to avoid confusion and bugs.

# ❓ QUESTION: What should the correct type hint be here?
# ✅ ANSWER  : `snack: str` because we're comparing it to a string "Burger".
#              The `int` hint is technically a mistake in this code.

def snack_Suggestion(snack:int)->str:             # ⚠️ hint says int, should be str
    # 🔹 Check if the snack requested is Burger
    if snack == "Burger":
        return "Yes available"                    # Burger is on the menu!

    else:
        return "not available"                    # Sorry, not on the menu


# 🔹 Test: asking for a "Burger"
print(snack_Suggestion("Burger"))                 # Output: "Yes available"

# 💡 KEY TAKEAWAY:
#    Type hints are NOT enforced — they are documentation only.
#    Always make sure your type hints match what you actually pass!
#    Good hint → snack: str (since we compare it with a string "Burger")

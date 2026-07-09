# =============================================================
# 📘 PROJECT 3 — Smart Kettle Notification System
# 📚 Section  : 3 — Conditions & Control Flow
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# BOOLEAN CONDITION — if True / if False
#
# This is the SIMPLEST form of if/else — using a boolean directly.
# In Python, True and False are the two boolean values.
#
# When you write:
#   if kettle_boiled:
# Python reads it as:
#   if kettle_boiled == True:
# (They are equivalent! Python checks if the value is "truthy")
#
# TRUTHY values → if block runs:
#   True, any non-zero number, non-empty string, non-empty list
#
# FALSY values → else block runs:
#   False, 0, None, "", [], {}
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Do I need to write `if kettle_boiled == True`?
# ✅ ANSWER  : NO! Just writing `if kettle_boiled:` is enough.
#              Python automatically checks if the value is truthy.
#              Writing `== True` is redundant (and considered bad style).

# ❓ QUESTION: What is the difference between True and "true"?
# ✅ ANSWER  : True (capital T) is Python's boolean keyword.
#              "true" (lowercase) is just a string, NOT a boolean!

'''
You're creating a notification system for a smart kettle.
it should remind the user only when the kettle has finished boling task:
* A varraible kettle_boiled = True
* if boiled show : "Kettle done! Time to make chai!"

'''


# 🔹 Set the kettle state — True means boiling is complete
kettle_boiled = True

# 🔹 Check: is kettle done?
if kettle_boiled:
    print("Kettle done! Time to make chai!")      # Runs when True

else:
    print("Kettle is still boiling... please wait!")  # Runs when False

# 💡 KEY TAKEAWAY:
#    `if variable:` is cleaner than `if variable == True:`
#    Booleans make conditions super readable — like plain English!
#    Try changing kettle_boiled = False to see the else branch run.

# =============================================================
# 📘 WALRUS OPERATOR — := | Assign and Check in ONE Step
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# WALRUS OPERATOR (:=) — "Assign AND Check at the same time"
# Added in Python 3.8+  |  Called "walrus" because := looks like walrus eyes!
#
# NORMAL WAY (2 steps):
#   remainder = value % 5     ← Step 1: assign
#   if remainder:             ← Step 2: check
#       print(remainder)
#
# WALRUS WAY (1 step):
#   if (remainder := value % 5):    ← Assign AND check in ONE line!
#       print(remainder)
#
# The walrus operator ASSIGNS the result AND EVALUATES it for truth AT ONCE.
#
# WHY USE IT?
#   → Saves one line of code
#   → Great inside while loops: while (chunk := file.read(8192))
#   → Useful when the same calculation is needed for both condition AND body
#
# ⚠️ PARENTHESES REQUIRED: (remainder := value % 5)
#   You MUST wrap walrus expressions in () when used inside if/while
#   Otherwise Python gives a syntax error.
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Why is it called the "walrus operator"?
# ✅ ANSWER  : Because := looks like the eyes and tusks of a walrus! 🦭
#              It's a fun name for a named expression operator.

# ❓ QUESTION: When should I use walrus vs regular assignment?
# ✅ ANSWER  : Use walrus when you need the value BOTH in the condition 
#              AND inside the if/while block. Avoid overusing it — 
#              if it makes code HARDER to read, just use two lines!

# ─────────────────────────────────────────────────────────────
# 🔹 NORMAL WAY — two separate steps
# ─────────────────────────────────────────────────────────────
from typing import Required
value = 13
remainder = value % 5          # Step 1: calculate and store

if remainder:                  # Step 2: check if non-zero (truthy)
  print(f"Not divisible , remainder is {remainder}")   # 13 % 5 = 3 → prints!



# ─────────────────────────────────────────────────────────────
# 🔹 WALRUS WAY — assign AND check in ONE step!
# ─────────────────────────────────────────────────────────────
  value = 13 
  if (remainder := value % 5):     # := assigns result AND checks truthiness
    print(f"Not divisible , remainder is {remainder}")  # remainder is already set!

# 💡 KEY TAKEAWAY:
#    := (walrus) = assign value AND evaluate truth in a single expression
#    Most useful in: while loops, list comprehensions, and if conditions
#    Always wrap in parentheses: if (x := expr):
#    Python 3.8+ required — older versions will error!




# available_sizes = ['small' , 'medium' , 'large' , "Extra-large"]

# if (required_size := input("Enter the required size : ")) in available_sizes:
#    print(f"Serving {required_size} Chai")
# else:
#   print(f"Size {required_size} is unavailable!")


flavors = ["Masala Chai" , "Ginger Chai"]
print("Available Flavors : ",flavors)


while (flavors := input("Enter the required flavor : ")) not in flavors:
  print("Flavors not in the menu")

print(f"you choose {flavors} chai")


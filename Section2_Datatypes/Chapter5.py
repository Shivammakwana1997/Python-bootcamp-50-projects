# =============================================================
# 📘 CHAPTER 5 — Float Data Type & Floating Point Precision
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# FLOAT = numbers with a decimal point → 3.14, 95.5, 1.75
#
# ⚠️ FLOATING POINT TRAP (Very important!):
#   Computers store numbers in binary (0s and 1s).
#   Some decimal numbers CANNOT be stored perfectly in binary.
#   So Python stores an APPROXIMATION — very close, but not exact!
#
#   Example:
#     ideal_temp  = 95.5
#     current_temp = 95.499999
#     Difference = 95.5 - 95.499999 = 0.000001000...something weird
#
#   This tiny error is called FLOATING POINT PRECISION ERROR.
#   It matters a LOT in finance, science, and calculations!
#
# sys.float_info → shows Python's internal limits for float numbers
#   (min value, max value, decimal precision, etc.)
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Why is 95.5 - 95.499999 not exactly 0.000001?
# ✅ ANSWER  : Because floats are stored in binary. Not all decimals
#              can be represented exactly. Python shows the closest
#              possible value, which may have tiny errors.

# ❓ QUESTION: What does sys.float_info tell us?
# ✅ ANSWER  : It shows the hardware limits for floats:
#              max = biggest float, min = smallest positive float,
#              dig = number of reliable decimal digits (usually 15-17)

import sys  # sys module gives us system-level info about Python

# 🔹 Two temperature values — very close but slightly different
ideal_temp = 95.5
current_temp = 95.499999

print(f"ideal temp {ideal_temp}")                         # 95.5
print(f"current temp {current_temp}")                     # 95.499999
print(f"Difference temp {ideal_temp - current_temp}")     # ~0.000001 (tiny precision error visible!)
print(sys.float_info)                                      # Shows float hardware limits

# 💡 KEY TAKEAWAY:
#    Floats are not always 100% precise.
#    For exact decimal math (like money), use Python's `decimal` module instead.

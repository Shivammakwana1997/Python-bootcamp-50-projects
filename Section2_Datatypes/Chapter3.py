# =============================================================
# 📘 CHAPTER 3 — Integers & All Math Operators
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# Integers = whole numbers (no decimal point) like 1, 50, 100, 1000
#
# Python supports all basic math operators:
#   +   → Addition        (add things together)
#   -   → Subtraction     (take away)
#   *   → Multiplication  (repeat addition)
#   /   → Division        (split into parts) → gives FLOAT result
#   //  → Floor Division  (split & DROP the remainder) → gives INT
#   %   → Modulo          (only the REMAINDER after division)
#   **  → Power/Exponent  (base raised to a power)
#
# BONUS: You can write big numbers with _ as separator (like commas)
#   Example: 1_000_000 = 1000000 (easier to read!)
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What is the difference between / and //?
# ✅ ANSWER  : "/" gives exact result with decimals (float)
#              "//" gives only the whole number part (drops remainder)
#              Example: 7 / 4 = 1.75  |  7 // 4 = 1

# ❓ QUESTION: What does % (modulo) do?
# ✅ ANSWER  : It gives the REMAINDER left after division.
#              Example: 7 % 4 = 3  (because 7 = 4×1 + 3 leftover)

#Interger

# ─────────────────────────────────────────────────────────────
# 🔹 ADDITION — Mixing tea and ginger quantities
# ─────────────────────────────────────────────────────────────
black_tea_grams = 100
ginger_grams = 50



total_grams = black_tea_grams + ginger_grams       # 100 + 50 = 150
print(f"Total grams of tea and ginger: {total_grams}")

# ─────────────────────────────────────────────────────────────
# 🔹 SUBTRACTION — Using some grams for brewing
# ─────────────────────────────────────────────────────────────
remaining_grams = total_grams - 30                 # 150 - 30 = 120
print(f"Remaining grams after using 30 grams: {remaining_grams}") 


# ─────────────────────────────────────────────────────────────
# 🔹 DIVISION — Splitting milk equally per serving
# ─────────────────────────────────────────────────────────────
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings          # 7 / 4 = 1.75 (float result)
print(f"Milk per serving: {milk_per_serving}") 

# ─────────────────────────────────────────────────────────────
# 🔹 FLOOR DIVISION — How many full bags per pot?
# ─────────────────────────────────────────────────────────────
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots              # 7 // 4 = 1 (drops the .75)
print(f"Bags per pot: {bags_per_pot}")

# ─────────────────────────────────────────────────────────────
# 🔹 MODULO — How many bags are left over?
# ─────────────────────────────────────────────────────────────
remaining_bags = total_tea_bags % pots             # 7 % 4 = 3 (3 leftover bags)
print(f"Remaining bags: {remaining_bags}")


# ─────────────────────────────────────────────────────────────
# 🔹 EXPONENT — Amplifying flavor strength
# ─────────────────────────────────────────────────────────────
base_flavor_strength=2
scale_factor = 3

powerful_falvour = base_flavor_strength ** scale_factor  # 2^3 = 8
print(f"Powerful flavour is: {powerful_falvour}")


# ─────────────────────────────────────────────────────────────
# 🔹 LARGE NUMBERS — Readable format using underscores
# ─────────────────────────────────────────────────────────────
total_tea_leaves_harvest = 1_000_000_000           # Same as 1000000000, but readable!
print(f"Total tea leaves harvest: {total_tea_leaves_harvest}")

# 💡 KEY TAKEAWAY:
#    Python treats _ in numbers just like a comma in real life
#    1_000_000 is exactly the same as 1000000

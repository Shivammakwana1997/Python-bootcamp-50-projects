# =============================================================
# 📘 LOOPS 6 — While Loop | Repeat Until Condition is False
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# WHILE LOOP = "keep doing this AS LONG AS the condition is True"
#
# Think of boiling water for chai:
#   → Check: is temp < 100°C? YES → keep heating (add 5°C)
#   → Check: is temp < 100°C? YES → keep heating
#   → ...keep repeating...
#   → Check: is temp >= 100°C? NOW NO → stop the loop!
#   → Print: "Temperature has reached above 100"
#
# KEY DIFFERENCE from for loop:
#   for loop  → you know HOW MANY times to repeat (fixed count)
#   while loop → you repeat UNTIL a condition becomes False (unknown count)
#
# ⚠️ DANGER — INFINITE LOOP:
#   If you FORGET to update the variable (temp += 5),
#   the condition NEVER becomes False → loop runs FOREVER!
#   Always make sure the while condition eventually becomes False!
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: When should I use while loop vs for loop?
# ✅ ANSWER  : Use FOR loop when you know the exact count (loop 10 times).
#              Use WHILE loop when you loop UNTIL something happens
#              (like waiting for user input, or temperature to reach a level).

# ❓ QUESTION: What is temp += 5?
# ✅ ANSWER  : Shorthand for temp = temp + 5.
#              It increases temp by 5 each time the loop runs.
#              Without this, the loop would run forever!

# 🔹 Starting temperature (needs to reach 100°C for boiling)
temp = 40 

# 🔹 While loop — keep heating as long as temp is below 100
while temp < 100:
    print(f"Current temparature:{temp}")    # Show current temp
    temp += 5                               # ← CRITICAL: increase temp each time!
    
# 🔹 This line runs AFTER the loop exits (when temp >= 100)
print("Temperature has reached above 100")  # Loop finished!

# 💡 KEY TAKEAWAY:
#    while loop → repeat UNTIL condition is False
#    ALWAYS update the condition variable inside the loop (avoid infinite loop!)
#    The line AFTER the while block runs once the loop exits normally.

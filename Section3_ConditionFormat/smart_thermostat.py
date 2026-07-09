# =============================================================
# 📘 PROJECT 4 — Smart Thermostat Controller
# 📚 Section  : 3 — Conditions & Control Flow
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# NESTED IF — if inside another if (like a double check)
#
# Imagine a smart home app:
#   STEP 1: Is the device ON or OFF?
#           → If OFF → "Device is inactive" (no point checking temp)
#   STEP 2: If ON → Now check the temperature:
#           → >= 35°C → Turn on AC
#           → <= 15°C → Turn on Heater
#           → else    → Temperature is fine, no action needed
#
# This is NESTED IF — the inner if only runs when outer if is True
#
# TYPE HINTS with str:
#   device_status: str → hint that this should be a string
#   temperature: int   → hint that this should be an integer
#   -> str             → hint that the function returns a string
#
# "in" with LIST:
#   if device_status in ["deactive", "inactive"]
#   → Checks if the value matches ANY item in the list
#   → Cleaner than writing: if x == "a" or x == "b"
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Why use "in [list]" instead of multiple or conditions?
# ✅ ANSWER  : `x in [a, b, c]` is cleaner and more readable than
#              `x == a or x == b or x == c`. Same result, better style!

# ❓ QUESTION: What is a nested if?
# ✅ ANSWER  : An if block INSIDE another if block.
#              The inner if only runs when the outer if is True.

def check_temperature(device_status:str , temperature:int) ->str:
    # 🔹 OUTER CHECK: Is the device active?
    if device_status == "active":

        # 🔹 INNER CHECK: What is the temperature?
        if temperature >= 35:
            return "Turn on AC"           # Too hot! Cool it down.
        elif temperature <= 15:
            return "Turn on the Heater"   # Too cold! Warm it up.
        else:
            return "Temperature is ideal" # Perfect! No action needed.


    else: return "Device is inactive"     # Device is OFF → skip everything


# 🔹 Get device status from user
device_status = input("Enter the device status : ").lower()

# 🔹 Check if device is inactive BEFORE asking for temperature
if device_status in ["deactive", "inactive"]:    # Both spellings handled!
    print("Device is inactive")
else:
    temperature = int(input("Enter the temperature : "))   # Only ask if device is active
    print(check_temperature(device_status, temperature))   # Call function & show result

# 💡 KEY TAKEAWAY:
#    Nested ifs let you make decisions in layers (check one thing, then another).
#    "in [list]" is a clean way to check multiple values at once.
#    int(input()) converts string input to integer for numeric comparison.

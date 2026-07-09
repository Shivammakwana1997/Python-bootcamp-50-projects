# =============================================================
# 📘 PROJECT — ATM Simulator using While Loop
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# WHILE LOOP — ATM Machine Logic
#
# An ATM processes withdrawals ONE AT A TIME:
#   → Check if balance is enough
#   → If yes → deduct and confirm
#   → If no → show "insufficient balance"
#   → Move to the next withdrawal in the list
#   → Repeat until all withdrawals are processed
#
# INDEX-BASED WHILE LOOP:
#   index = 0
#   while index < len(withdrawal):
#       process withdrawal[index]
#       index += 1
#
#   → index starts at 0
#   → each loop picks withdrawal at current index
#   → index increments → moves to next item
#   → when index = len(list) → condition False → loop stops
#
# KEY CONCEPTS USED:
#   1. while loop with index counter
#   2. List indexing: widthdrawal[index]
#   3. .append() to build a message log
#   4. Conditional check: balance >= current_amount
#   5. Balance update: balance = balance - current_amount
#   6. return inside the while loop (exits function on first withdrawal!)
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Why does `return messages` inside the while loop cause early exit?
# ✅ ANSWER  : `return` inside a loop EXITS the function immediately!
#              So the ATM only processes the FIRST withdrawal and stops.
#              To process ALL withdrawals, `return` should be OUTSIDE the loop.

# ❓ QUESTION: What is len(widthdrawal)?
# ✅ ANSWER  : len() gives the NUMBER of items in the list.
#              while index < len(widthdrawal) → loop runs as many times as there are items.

'''
Atm simulator

'''



def atm_simulator(balance:int,widthdrawal:int)->str:

    index = 0           # 🔹 Start at the first item (index 0)
    messages = []       # 🔹 Empty list to collect all ATM messages

    # 🔹 Loop through all withdrawal requests
    while index < len(widthdrawal):
        current_ammount = widthdrawal[index]    # Get current withdrawal amount

        # 🔹 Check if balance is enough
        if balance >= current_ammount:
            balance = balance - current_ammount                           # Deduct from balance
            messages.append(f"widthdraw successfull and amount is {current_ammount}")
        else:
            messages.append(f"insuffisent amount and amount is {current_ammount}")  # Not enough!


        index += 1      # ← MUST increment index to avoid infinite loop!


        messages.append(f"Remaining amount of current balance is {balance}")
        return messages  # ⚠️ NOTE: This returns after only ONE withdrawal!
                         #    Moving this outside the while block would process all withdrawals.

    
# 🔹 Take input from user
balance = int(input("Enter the current balance : "))
widthdrawal = [int(input("Enter the widthdrawal amount : "))]   # Stored as a list
print(atm_simulator(balance,widthdrawal))           

# 💡 KEY TAKEAWAY:
#    While loop with index = manual control over which item to process
#    return inside a loop = exits the function IMMEDIATELY (only processes first item!)
#    Always increment the index (index += 1) to avoid an infinite loop.

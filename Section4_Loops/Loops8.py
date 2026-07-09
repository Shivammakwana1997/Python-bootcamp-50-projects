# =============================================================
# 📘 LOOPS 8 — for/else | Loop with Else Clause
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# FOR/ELSE — Python's special loop + else feature
#
# This is one of Python's UNIQUE features (many languages don't have it!):
#   → else block with a for loop runs when the loop COMPLETES NORMALLY
#   → If break is used, the else block is SKIPPED
#
# Think of it like a job interview search:
#   → Check each candidate one by one
#   → If someone IS eligible (age > 18) → hire them (break)
#   → If NO ONE is eligible after checking all → print "no one is eligible" (else)
#
# RULE: else with for/while:
#   → Loop finishes all iterations WITHOUT break → else RUNS
#   → Loop exits via break → else is SKIPPED
#
# TUPLE UNPACKING IN FOR LOOP:
#   Staff = [("Amit", 16), ("Zara", 17), ...]
#   for (name, age) in Staff: → unpacks each tuple into name and age
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: When does the else block of a for loop run?
# ✅ ANSWER  : Only when the loop COMPLETES all iterations WITHOUT hitting a break.
#              If break is used, the else is COMPLETELY SKIPPED.

# ❓ QUESTION: Why is for/else useful?
# ✅ ANSWER  : It replaces the need for a "found" flag variable.
#              Without for/else, you'd need: found = False → ... → if not found: print(...)
#              Python's for/else does this cleanly!

# 🔹 List of staff with names and ages (list of tuples)
Staff = [("Amit",16) , ("zara",17), ("raj",28), ("simran",18)]


# 🔹 Loop through each staff member and check eligibility (age > 18)
for (name,age) in Staff:           # Unpack each tuple → (name, age)
    if age > 18:
        print(f"{name} is eligible to manage the staff")    # Found someone!
        break                       # Exit loop — no need to check more
else:
    print("no one is eligible")     # Only runs if NO break was hit (nobody eligible)

# ⚡ TRACE:
#   ("Amit", 16)  → 16 > 18? NO → continue
#   ("zara", 17)  → 17 > 18? NO → continue
#   ("raj", 28)   → 28 > 18? YES → print "raj is eligible" → BREAK
#   else block is SKIPPED because break was triggered

# 💡 KEY TAKEAWAY:
#    for/else is Python's built-in "search and report" pattern
#    else runs only when loop finishes WITHOUT break (i.e., nothing was found)
#    Great for: searching lists, validating items, finding matches

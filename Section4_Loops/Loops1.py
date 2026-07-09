# =============================================================
# 📘 LOOPS 1 — Basic For Loop with range()
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# FOR LOOP = "do this task N times"
#
# Think of it like a chai stall with a token system:
#   → Token 1 served ✅
#   → Token 2 served ✅
#   → ... all the way to Token 10 ✅
#
# range(1, 11) → generates numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#   range(start, stop) → includes start, EXCLUDES stop
#   So range(1, 11) gives 1 to 10 (NOT 11)
#
# for i in range(1, 11):
#   → i takes each value from 1 to 10, ONE at a time
#   → Loop body runs once for EACH value of i
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Why does range(1, 11) not include 11?
# ✅ ANSWER  : range() is EXCLUSIVE at the end (stop value).
#              range(1, 11) gives → 1, 2, 3, ..., 10 (stops before 11)
#              This is the same as Python list indexing (also exclusive at end)

# ❓ QUESTION: What is `i` in the for loop?
# ✅ ANSWER  : `i` is a loop variable — a temporary container that holds
#              the current value in each iteration.
#              1st loop: i=1, 2nd loop: i=2, ..., 10th loop: i=10

# 🔹 Serve chai to 10 customers using token numbers 1 to 10
for i in range(1,11):
    print("Serving chai to token no:",i)    # Runs 10 times: i = 1, 2, ..., 10

# 💡 KEY TAKEAWAY:
#    for loop = repeat a task a specific number of times
#    range(start, stop) → start is INCLUDED, stop is EXCLUDED
#    The loop variable (i) changes with each iteration automatically

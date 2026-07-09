# =============================================================
# 📘 LOOPS 2 — Nested For Loop (Loop inside a Loop)
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# NESTED FOR LOOP = a loop INSIDE another loop
#
# Think of it like this scenario:
#   → There are 4 batches of students
#   → Each batch has 5 students
#   → We need to serve chai to EACH student in EACH batch
#
# OUTER LOOP → goes through each batch (1 to 4)
# INNER LOOP → goes through each student in that batch (1 to 5)
#
# Total iterations = 4 batches × 5 students = 20 print statements
#
# HOW IT RUNS:
#   batch=1 → student 1,2,3,4,5 (inner loop completes fully)
#   batch=2 → student 1,2,3,4,5 (inner loop completes again)
#   batch=3 → student 1,2,3,4,5
#   batch=4 → student 1,2,3,4,5
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: How many times does the inner loop run in total?
# ✅ ANSWER  : outer loop runs 4 times × inner loop runs 5 times = 20 total

# ❓ QUESTION: When should we use nested loops?
# ✅ ANSWER  : When you have data in rows AND columns (like a table, matrix,
#              or multi-level structure that needs to be processed together).

# 🔹 OUTER LOOP — 4 batches (batch=1, batch=2, batch=3, batch=4)
for batch in range(1,5):
    # 🔹 INNER LOOP — 5 students per batch (student=1 to 5)
    for student in range(1,6):
        print("Serving chai to batch ",batch,"student no",student)
        # Each print: "Serving chai to batch X student no Y"


# 💡 KEY TAKEAWAY:
#    Nested loops = loop inside a loop
#    Total iterations = outer count × inner count
#    Use them for grids, tables, matrices, or multi-level data structures

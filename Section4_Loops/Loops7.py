# =============================================================
# 📘 LOOPS 7 — break & continue | Loop Control Statements
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# BREAK — "STOP the loop immediately and EXIT"
# CONTINUE — "SKIP this iteration and go to the NEXT one"
#
# Think of a chai shop checking their flavor stock:
#   → Serving flavors one by one...
#   → "out of stock" → SKIP it (continue) → serve the next one
#   → "Discontinued" → STOP serving (break) → close the counter
#
# CONTINUE:
#   → Skips the REST of the current loop body
#   → Goes back to the TOP of the loop for the next iteration
#   → Loop does NOT exit — just skips ONE turn
#
# BREAK:
#   → Exits the loop IMMEDIATELY
#   → Code AFTER the loop still runs
#   → Any remaining items in the loop are NEVER processed
#
# Flow with the flavor list:
#   "Masala"       → serve ✅
#   "Ginger"       → serve ✅
#   "out of stock" → SKIP (continue) → go to next flavor
#   "Mint"         → serve ✅
#   "Discontinued" → print warning, BREAK → stop everything
#   "Lemon"        → NEVER reached (loop already exited)
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What is the difference between break and continue?
# ✅ ANSWER  : continue → skip current item, loop CONTINUES to next item
#              break    → EXIT the loop entirely, no more iterations

# ❓ QUESTION: Does code AFTER the loop run when break is used?
# ✅ ANSWER  : YES! break exits the loop, but the code AFTER the loop 
#              (outside the loop block) still executes normally.

def check_flavors(flavors: list):
    for flavor in flavors:
        # 🔹 CONTINUE — skip "out of stock" flavors, move to next
        if flavor == "out of stock":
            continue                                      # Skip this, next flavor!

        # 🔹 BREAK — stop everything if "Discontinued" found
        if flavor == "Discontinued":
            print(f"Discontinued item found: {flavor}")  # Warn user
            break                                         # EXIT loop immediately

        # 🔹 Normal case — serve the flavor
        print(f"Serving flavor: {flavor}")




# Example list to test the loop control
flavors_list = ["Masala", "Ginger", "out of stock", "Mint", "Discontinued", "Lemon"]
check_flavors(flavors_list)
print("out of the loops")    # This runs AFTER the function (outside everything)

# 💡 KEY TAKEAWAY:
#    continue = "skip and move on"
#    break    = "stop and exit"
#    Code after a loop ALWAYS runs (even after break), unless it's inside the loop.

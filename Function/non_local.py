"""
=============================================================
  Topic     : Python `nonlocal` Keyword — Modifying Enclosing Scope
  Section   : Functions → Scope & Closures
  File      : non_local.py
  Author    : Shivam Makwana
  Date      : 2026-07-18
=============================================================

  Key Concept:
  By default, an inner (nested) function CANNOT modify a variable
  from its enclosing function — it can only read it.

  `nonlocal` keyword:
  → Declares that the variable belongs to the nearest enclosing scope.
  → Allows the inner function to modify that outer variable directly.

  Without `nonlocal` → inner function creates its own local copy.
  With    `nonlocal` → inner function modifies the enclosing variable.

=============================================================
"""


def update_order():
    chai_type = "Elaichi"  # Enclosing scope variable (outer function)

    def kitchen():
        nonlocal chai_type       # ← Tells Python: use the outer `chai_type`
        chai_type = "kesar"      # ← Now modifies the enclosing variable directly

    kitchen()  # Call inner function to trigger the modification
    print("After kitchen update", chai_type)  # Output: kesar


# ── Entry Point ───────────────────────────────────────────────────────────────
update_order()
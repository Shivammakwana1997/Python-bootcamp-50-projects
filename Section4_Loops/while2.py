"""
=============================================================
  Topic     : Python `while` Loop — Counting Up & Down
  Section   : Section 4 → Loops
  File      : while2.py
  Author    : Shivam Makwana
  Date      : 2026-07-18
=============================================================

  Demonstrates two common `while` loop patterns:
    1. Count UP   → 0 to 4  (condition: number < 5)
    2. Count DOWN → 5 to 1  (condition: number1 > 0)

  Syntax:
    while <condition>:
        <body>
        <update counter>  ← must update to avoid infinite loop!

=============================================================
"""


# ── Pattern 1: Count Up (0 → 4) ──────────────────────────────────────────────
# Starts at 0, increments by 1 each iteration, stops when number reaches 5

number = 0
while number < 5:
    print(number)   # Prints: 0, 1, 2, 3, 4
    number += 1     # Increment — moves loop toward the exit condition


# ── Pattern 2: Count Down (5 → 1) ────────────────────────────────────────────
# Starts at 5, decrements by 1 each iteration, stops when number1 reaches 0

number1 = 5
while number1 > 0:
    print(number1)  # Prints: 5, 4, 3, 2, 1
    number1 -= 1    # Decrement — moves loop toward the exit condition
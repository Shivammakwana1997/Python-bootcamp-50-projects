"""
=============================================================
  Topic     : Python Functions — Basic Exercises
  Section   : Functions → Core Concepts
  File      : exc.py
  Author    : Shivam Makwana
  Date      : 2026-07-18
=============================================================

  Exercises:
    1. cube(x)    → Returns the cube of a number using exponentiation
    2. is_even()  → Checks if a number is even or odd (without using a loop)

=============================================================
"""


# ── Exercise 1: Cube of a Number ─────────────────────────────────────────────
# Returns x raised to the power of 3 (x³)

def cube(x):
    return x ** 3


print(cube(4))  # Output: 64


# ── Exercise 2: Even or Odd Check (without a for loop) ───────────────────────
# Uses the modulus operator (%) to determine divisibility by 2.
# If num % 2 == 0 → Even, otherwise → Odd

def is_even(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")


is_even(4)  # Output: 4 is even
is_even(5)  # Output: 5 is odd
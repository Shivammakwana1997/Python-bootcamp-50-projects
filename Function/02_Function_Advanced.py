# ============================================================
# Section 5 - Functions: Advanced Concepts
# ============================================================

# -----------------------------------------------
# 1. Lambda Functions (Anonymous Functions)
# -----------------------------------------------
# lambda arguments: expression

square = lambda x: x ** 2
add = lambda a, b: a + b

print("Lambda Examples:")
print(f"  Square of 5  : {square(5)}")
print(f"  Sum 3 + 7    : {add(3, 7)}")

# Lambda with sorted()
teas = ["Ginger Chai", "Masala Chai", "Green Tea", "Lemon Chai"]
sorted_teas = sorted(teas, key=lambda t: len(t))
print(f"\n  Sorted by length: {sorted_teas}")

# -----------------------------------------------
# 2. map() — Apply function to each item
# -----------------------------------------------

prices = [30, 45, 20, 60]
discounted = list(map(lambda p: p * 0.9, prices))

print("\nmap() Example:")
print(f"  Original : {prices}")
print(f"  10% Off  : {discounted}")

# -----------------------------------------------
# 3. filter() — Filter items by condition
# -----------------------------------------------

items = ["Masala Chai", "Cold Coffee", "Lemon Chai", "Cold Brew"]
hot_drinks = list(filter(lambda x: "Cold" not in x, items))

print("\nfilter() Example:")
print(f"  All items   : {items}")
print(f"  Hot drinks  : {hot_drinks}")

# -----------------------------------------------
# 4. Nested Functions (Inner Functions)
# -----------------------------------------------

def outer(msg):
    def inner():
        print(f"Message from inner: {msg}")
    inner()

outer("Hello from outer function!")

# -----------------------------------------------
# 5. Recursive Function
# -----------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"\nFactorial of 5 = {factorial(5)}")
print(f"Factorial of 7 = {factorial(7)}")

# -----------------------------------------------
# 6. Function as Argument (Higher Order Function)
# -----------------------------------------------

def apply(func, value):
    return func(value)

result = apply(lambda x: x * 3, 10)
print(f"\nHigher Order Function result: {result}")

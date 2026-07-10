# ============================================================
# Section 4 - Walrus Operator + match-case Combined Exercise
# ============================================================
#
# Walrus Operator (:=)
# → Assigns a value AND uses it in the same expression
#
# match-case
# → Python's structural pattern matching (Python 3.10+)
#   Like switch-case in other languages
# ============================================================

# -----------------------------------------------
# Exercise 1: Chai Size Selector with Walrus
# -----------------------------------------------

available_sizes = ["small", "medium", "large", "extra-large"]

print("=== Chai Size Checker ===")
size = "medium"  # simulating input for demo

if (required_size := size.lower()) in available_sizes:
    print(f"✅ Serving '{required_size}' Chai")
else:
    print(f"❌ Size '{required_size}' is unavailable!")

# -----------------------------------------------
# Exercise 2: match-case with Chai Type
# -----------------------------------------------

print("\n=== Chai Type Matcher ===")

def describe_chai(chai):
    match chai.lower():
        case "masala chai":
            return "Spiced Indian tea with ginger & cardamom 🫚"
        case "ginger chai":
            return "Strong ginger-flavored tea 🫚"
        case "green tea":
            return "Light and healthy antioxidant tea 🍵"
        case "lemon chai":
            return "Refreshing tea with lemon zest 🍋"
        case _:
            return "Unknown chai type! Please check the menu."

chai_orders = ["Masala Chai", "Lemon Chai", "Cold Brew", "Green Tea"]

for order in chai_orders:
    description = describe_chai(order)
    print(f"  {order}: {description}")

# -----------------------------------------------
# Exercise 3: Walrus in while loop (Number Game)
# -----------------------------------------------

print("\n=== Number Range Checker ===")

numbers = [5, 12, 3, 20, 8, 15]

for num in numbers:
    if (squared := num ** 2) > 100:
        print(f"  {num}² = {squared} → EXCEEDS 100 ⚠️")
    else:
        print(f"  {num}² = {squared} → Within range ✅")

# ============================================================
# Section 4 - Exercise: Discount Calculator using match-case
# ============================================================

# -----------------------------------------------
# Part 1: Basic Discount using Dictionary + Loop
# -----------------------------------------------

users = [
    {"id": 1, "total": 100, "coupon": "P120"},
    {"id": 2, "total": 500, "coupon": "F50"},
    {"id": 3, "total": 400, "coupon": "F40"},
]

discounts = {
    "P120": (0.2, 0),   # 20% off
    "F50":  (0.0, 50),  # flat ₹50 off
    "F40":  (0.0, 40),  # flat ₹40 off
}

print("=" * 40)
print("  Part 1: Dictionary-based Discount")
print("=" * 40)

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    final = user["total"] - discount
    print(f"User {user['id']} | Coupon: {user['coupon']} | Final Bill: ₹{final}")

# -----------------------------------------------
# Part 2: match-case for Coupon Discount
# -----------------------------------------------

print("\n" + "=" * 40)
print("  Part 2: match-case Discount System")
print("=" * 40)

def apply_discount(total, coupon):
    match coupon:
        case "P120":
            discount = total * 0.20       # 20% off
            label = "20% Percentage Off"
        case "F50":
            discount = 50                 # flat ₹50 off
            label = "Flat ₹50 Off"
        case "F40":
            discount = 40                 # flat ₹40 off
            label = "Flat ₹40 Off"
        case "FREESHIP":
            discount = 30                 # free shipping ₹30
            label = "Free Shipping (₹30)"
        case _:
            discount = 0
            label = "No Discount"

    final = total - discount
    return final, label

# Test the match-case function
orders = [
    {"id": 101, "total": 800, "coupon": "P120"},
    {"id": 102, "total": 300, "coupon": "F50"},
    {"id": 103, "total": 250, "coupon": "FREESHIP"},
    {"id": 104, "total": 150, "coupon": "UNKNOWN"},
]

for order in orders:
    final, label = apply_discount(order["total"], order["coupon"])
    print(f"Order {order['id']} | {label} | ₹{order['total']} → ₹{final}")

# -----------------------------------------------
# Part 3: Walrus Operator + match-case
# -----------------------------------------------

print("\n" + "=" * 40)
print("  Part 3: Walrus + match-case Demo")
print("=" * 40)

coupons = ["P120", "F40", "INVALID", "F50", "FREESHIP"]

for coupon in coupons:
    if (result := apply_discount(500, coupon))[1] != "No Discount":
        final, label = result
        print(f"Coupon '{coupon}' applied → {label} | Final: ₹{final}")
    else:
        print(f"Coupon '{coupon}' → Invalid / No discount")
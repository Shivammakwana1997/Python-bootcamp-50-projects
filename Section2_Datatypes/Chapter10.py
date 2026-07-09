# =============================================================
# 📘 CHAPTER 10 — Dictionary | Key-Value Store
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# DICTIONARY = a collection of KEY → VALUE pairs
# Written in { } with "key": value format
#
# Think of a Dictionary like a MENU CARD:
#   "type"    → "Masala Chai"    (key → value)
#   "price"   → 20               (key → value)
#   "sugar"   → "2 spoons"       (key → value)
#
# WHY USE DICTIONARIES?
#   → Fast lookups by key (like looking up a name in a phonebook)
#   → Stores related data together (like a database record)
#
# KEY METHODS:
#   dict[key] = value  → Add or update a key
#   del dict[key]      → Delete a key-value pair
#   .keys()            → Get all keys
#   .values()          → Get all values
#   .items()           → Get all key-value pairs as tuples
#   .popitem()         → Remove & return the LAST key-value pair
#   .update(other)     → Merge another dict into this one
#   .get(key, default) → Safe way to get a value (no KeyError if missing)
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What is the difference between dict[key] and dict.get(key)?
# ✅ ANSWER  : dict[key]        → raises KeyError if key doesn't exist
#              dict.get(key)    → returns None (or a default) if key missing
#              Always use .get() when you're not sure the key exists!

# ❓ QUESTION: What does .popitem() do?
# ✅ ANSWER  : Removes and RETURNS the LAST inserted key-value pair as a tuple.
#              Useful for processing items one by one from the end.

'''
Dictionary :- 
are mutable and are always written in {} brackets
'''

# 🔹 Creating a dict using dict() constructor
Chai_order = dict(type="Masala Chai",sugar="2 spoons",addons=["ginger","cardamom"])

print(f"type of chai order {Chai_order}")              # Full dict printed
print(f"type of chai order {type(Chai_order)}")        # <class 'dict'>


# 🔹 Creating an empty dict and adding key-value pairs one by one
chai_recipe = {}
chai_recipe["base"]="blacktea"                         # Add key "base"
chai_recipe["liquid"]="milk"                           # Add key "liquid"


print(f"Recipe base: {chai_recipe['base']}")           # "blacktea"
print(f"Recipe liquid: {chai_recipe['liquid']}")       # "milk"
print(f"Recipe : {chai_recipe}")                       # Full recipe dict

# 🔹 Delete a key
del chai_recipe["liquid"]                              # Remove "liquid" key entirely
print(f"Recipe : {chai_recipe}")                       # Only "base" remains


# 🔹 A new chai order dict
Chai_order = {"type":"Gingerchai","payment":"UPI","time":"11.34AM"}

print(f"order type {Chai_order.keys()}")               # dict_keys(['type', 'payment', 'time'])
print(f"order payment {Chai_order.values()}")          # dict_values(['Gingerchai', 'UPI', '11.34AM'])
print(f"order details {Chai_order.items()}")           # dict_items([('type','Gingerchai'), ...])



# 🔹 popitem() — remove and return the last key-value pair
last_item = Chai_order.popitem()                       # Removes "time": "11.34AM"
print(f"last item is {last_item}")                     # ('time', '11.34AM')

# 🔹 update() — merge extra_spices into chai_recipe
extra_spices ={"flavor":"Elaichi","color":"green"}
chai_recipe.update(extra_spices)                       # chai_recipe now has 3 keys
print(f"Update_Recipe : {chai_recipe}")                # base + flavor + color


# 🔹 .get() — safe way to fetch a value (no crash if key doesn't exist)
customer_note = Chai_order.get("Note","No notes")      # "Note" key doesn't exist
print(f"Notes: {customer_note}")                       # "No notes" (default returned)

# 💡 KEY TAKEAWAY:
#    Dictionaries are the BACKBONE of Python data management.
#    Always use .get() for safe access to avoid KeyError crashes.

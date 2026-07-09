# =============================================================
# 📘 CHAPTER 8 — List | Mutable Ordered Collection
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# LIST = an ordered, changeable collection of items
# Written in [ ] square brackets
#
# Think of a list like a SHOPPING LIST:
#   → You can ADD new items         → .append() / .extend() / .insert()
#   → You can REMOVE items          → .remove() / .pop()
#   → You can REVERSE the order     → .reverse()
#   → You can SORT alphabetically   → .sort()
#   → You can find MAX / MIN value  → max() / min()
#
# KEY METHODS:
#   .append(x)   → Add x to the END of the list
#   .remove(x)   → Remove FIRST occurrence of x
#   .extend(lst) → Add ALL items from another list
#   .insert(i,x) → Insert x at position i
#   .pop()       → Remove & return the LAST item
#   .reverse()   → Reverse the list IN PLACE (returns None!)
#   .sort()      → Sort the list IN PLACE (alphabetical/numerical)
#   max(lst)     → Highest value
#   min(lst)     → Lowest value
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What does .reverse() return?
# ✅ ANSWER  : None! It modifies the list IN PLACE and returns nothing.
#              So print(list.reverse()) will always print "None".
#              You need to print the list AFTER calling .reverse().

# ❓ QUESTION: What is the difference between .append() and .extend()?
# ✅ ANSWER  : .append() adds ONE item (even if it's a list, adds as 1 item)
#              .extend() adds ALL items from another iterable individually

''' 
List:- 
is a mutable data structure that is used to store multiple values in a single variable
Lists are ordered and allow duplicate values
They are defined using square brackets []
'''

import typing_extensions

# 🔹 Creating a list of chai ingredients
ingredients = ["water", "milk", "tea leaves", "sugar"]
ingredients.append("Sugar")                          # Add "Sugar" to end of list

print(f"The ingredients are:{ingredients}")          # All 5 items shown


# 🔹 Remove an ingredient (milk)
ingredients.remove("milk")                           # Removes first "milk" found
print(f"The ingredients are:{ingredients}")          # "milk" is gone now


# 🔹 Extend — add ALL spices from another list
spice_options = ["ginger","cardamom","clove"]
ingredients.extend(spice_options)                    # Adds 3 items individually
print(f"the new list is:{ingredients}")

#print(dir(list))                                    # Uncomment to see ALL list methods


# 🔹 Insert at a specific position (index 1 = second position)
ingredients.insert(1,"green tea")                    # "green tea" goes to index 1
print(f"the new list is:{ingredients}")

# 🔹 Pop — remove and return the LAST item
last_Added = ingredients.pop()                       # Removes last item and saves it
print(f"{last_Added}")                               # Shows what was removed

print(f"chai : {ingredients}")
print(f"chai: {ingredients.reverse()}")              # ⚠️ prints "None"! reverse() returns None

ingredients.reverse()                                # Actually reverse the list
print(f"chai: {ingredients}")                        # Now shows reversed order

# 🔹 Sort alphabetically
ingredients.sort()
print(f"soreted_chai: {ingredients}")                # Alphabetical order

# 🔹 max() and min() — useful for number lists
sugar_level = [1,2,3,4,5]   
print(f"max sugar level {max(sugar_level)}")         # 5
print(f"min sugar level {min(sugar_level)}")         # 1

# 💡 KEY TAKEAWAY:
#    Lists are the most used data structure in Python.
#    They are flexible — add, remove, sort, reverse, find max/min.

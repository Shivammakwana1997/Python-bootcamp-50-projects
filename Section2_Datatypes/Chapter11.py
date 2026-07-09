# =============================================================
# 📘 CHAPTER 11 — Advanced Datatypes | arrow & namedtuple
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# ARROW LIBRARY:
#   A better way to handle dates and times in Python.
#   Built-in datetime is complex → arrow makes it HUMAN FRIENDLY.
#   arrow.utcnow() → current time in UTC (Universal Standard Time)
#   .to("timezone") → convert to any timezone (like "Asia/Kolkata")
#
# NAMEDTUPLE (from collections):
#   A TUPLE with NAMED fields — like a lightweight class!
#   Instead of tuple[0], tuple[1] → you use tuple.name, tuple.age
#   Think of it like a mini "record" or "struct"
#
#   Example:
#     Person = namedtuple("Person", "name age city")
#     p = Person("Shivam", 25, "Surat")
#     p.name → "Shivam"  (much cleaner than p[0]!)
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: Why use arrow instead of Python's built-in datetime?
# ✅ ANSWER  : arrow is simpler, chainable, and handles timezones 
#              easily. datetime requires more verbose code for the same.

# ❓ QUESTION: What is a namedtuple and when to use it?
# ✅ ANSWER  : A namedtuple is a tuple with field names. Use it when
#              you want a lightweight, immutable record with readable names.
#              More memory-efficient than a full class or dict.

''' advanced datatypes 
datetime , time , calander
'''

# pyrefly: ignore [missing-import]
import arrow                                           # Third-party library for dates/times

# 🔹 Get current UTC time and convert to Berlin timezone
brewing_time = arrow .utcnow()                         # Get time in UTC
brewing_time = brewing_time.to("Europe/Berlin")        # Convert to Berlin local time
print(f"time in germany {brewing_time}")               # e.g. 2026-07-09T18:00:00+02:00


# 🔹 namedtuple — creating a lightweight "Chai Profile" type
from collections import namedtuple                     # Import namedtuple from collections

# Define a new named tuple type with 4 fields
chaiProfile = namedtuple("chaiProfile","masalachai kadakchai adrak chai")
# Now chaiProfile is a "blueprint" — like a class, but simpler!

print(chaiProfile)                                     # Shows the class definition

# 💡 USAGE EXAMPLE (how you'd create an instance):
# my_chai = chaiProfile(masalachai=2, kadakchai=1, adrak=3, chai=4)
# print(my_chai.masalachai) → 2

# 💡 KEY TAKEAWAY:
#    arrow → clean, readable date/time handling with timezone support
#    namedtuple → readable, immutable records (name your tuple fields!)

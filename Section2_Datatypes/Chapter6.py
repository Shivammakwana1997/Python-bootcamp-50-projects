# =============================================================
# 📘 CHAPTER 6 — Strings | Slicing | Encoding & Bytes
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# STRING = any text wrapped in quotes → "hello", 'world'
#
# SLICING — cutting a portion of a string:
#   text[start:end]    → from index start to end-1
#   text[:5]           → first 5 characters
#   text[12:]          → from index 12 to the end
#   text[::-1]         → REVERSE the entire string!
#
# ENCODING:
#   Computers understand only bytes (0s and 1s), not text.
#   So text must be ENCODED (converted to bytes) before storage.
#   .encode("utf-8") → text → bytes
#   .decode("utf-8") → bytes → text (back to human-readable)
#
# BYTES (b"..."):
#   Raw binary data — like bytes from a file or network.
#   \x20 is the byte code for a SPACE character.
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What does [::-1] do to a string?
# ✅ ANSWER  : It reverses the string! 
#              [start:end:step] → step=-1 means go BACKWARDS

# ❓ QUESTION: Why do we encode strings?
# ✅ ANSWER  : To send text over networks or save to files, Python
#              needs to convert text into bytes. UTF-8 is the most
#              common encoding standard used worldwide.

# 🔹 Basic string variables
chai_type = "Masala Chai"
customer_name = "Shivam"


print(f"Customer {customer_name} ordered {chai_type}")    # f-string formatting


# 🔹 String SLICING — cutting parts of a string
chai_description = "Aromatic and bold"
print(f"firstword : {chai_description[:5]}")   # "Aroma" (first 5 chars)
print(f"lastword:  {chai_description[12:]}")   # "bold" (from index 12 to end)
print(f"lastword: {chai_description[::-1]}")   # "dlob dna citamorA" (reversed!)


# 🔹 Encoding — converting text to bytes (UTF-8)
label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")     # Text → Bytes

print(f"Label type: {label_text}")             # Original text
print(f"Encoded Label: {encoded_label}")       # b'Chai Special' (bytes format)


# 🔹 Decoding — converting bytes BACK to text
decoded_label = encoded_label.decode("utf-8") # Bytes → Text
print(f"Decoded Label: {decoded_label}")       # "Chai Special" (back to normal)


# 🔹 Raw bytes literal — b"..." (directly writing bytes)
raw_data = b"Tea\x20Leaves"                   # \x20 = space character in hex
print(f"Raw data: {raw_data}")                 # b'Tea Leaves'
print(f"Decoded: {raw_data.decode('utf-8')}") # "Tea Leaves"

# 💡 KEY TAKEAWAY:
#    Strings → encode() → Bytes (for storage/network)
#    Bytes   → decode() → String (for reading/display)

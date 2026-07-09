# =============================================================
# 📘 LOOPS 9 — Project: Parcel Scanning System
# 📚 Section  : 4 — Loops
# 📚 Course   : The Ultimate Python Bootcamp (Hitesh Choudhary)
# 👨‍💻 Author   : Shivam Makwana
# =============================================================

# ─────────────────────────────────────────────────────────────
# 🧠 CONCEPT EXPLANATION (Simple Language)
# ─────────────────────────────────────────────────────────────
# COMBINING: for loop + continue + break + for/else + list building
#
# This is a REAL WORLD mini-project — a warehouse parcel scanner!
#
# Think of Amazon/Flipkart warehouse:
#   → Conveyor belt moves parcels one by one
#   → Scanner reads barcodes
#   → "DAMAGED" barcode → skip it, note it, scan next
#   → "STOP" barcode → emergency halt, stop everything
#   → Normal barcode → scan and log it
#   → If ALL parcels scanned without stopping → "All done!"
#
# CONCEPTS USED:
#   1. Function with type hints: list[str] -> list[str]
#   2. Empty list to collect messages: scan_logs = []
#   3. for loop to process each barcode
#   4. continue → skip DAMAGED parcels
#   5. break → stop on STOP signal
#   6. for/else → "All parcels scanned" only if NO break
#   7. .append() → add messages to the log
#   8. return → give back all messages to caller
#
# TYPE HINT: list[str]
#   → A list where every item is a string
#   → parcel_codes: list[str] → each barcode is a string
#   → -> list[str] → function returns a list of strings
# ─────────────────────────────────────────────────────────────

# ❓ QUESTION: What does scan_logs.append(message) do?
# ✅ ANSWER  : It adds `message` to the END of the scan_logs list.
#              Like writing a new line in a logbook.

# ❓ QUESTION: Why does the else block have "All parcels scanned" message?
# ✅ ANSWER  : Because the else only runs when the for loop COMPLETES 
#              without hitting a break. If "STOP" is in the list,
#              break fires and else is skipped → no "All done" message.

'''

Parcel Scanning System
You are automating a parcel scanning system in a warehouse. Each parcel has a barcode. The system must validate all parcels and report issues:



Tasks:

There is list named parcel_code which consist of barcods.

The system will go through each barcode in the list using a for loop:

If a barcode is "DAMAGED", skip it using continue and log: "Skipped damaged parcel".

If a barcode is "STOP", use break and log: "Critical error: Stopping scan".

For valid barcodes, log: "Scanned parcel: <barcode>".

If the loop completes without hitting a break, log: "All parcels scanned successfully" using for-else.

Return a list of all scan messages.

'''


def scan_parcels(parcel_codes: list[str]) -> list[str]:
    scan_logs = []                                     # 📋 Empty logbook to collect messages

    for barcode in parcel_codes:                       # 🔄 Go through each barcode

        # 🔹 DAMAGED → skip it, log a note, continue to next
        if barcode == "DAMAGED":
            scan_logs.append("Skipped damaged parcel") # Log the skip
            continue                                    # ← skip rest, go to next barcode

        # 🔹 STOP → emergency halt! Log it and exit loop
        elif barcode == "STOP":
            scan_logs.append("Critical error: Stopping scan")  # Log the error
            break                                       # ← EXIT loop immediately

        # 🔹 Normal barcode → scan it successfully
        else:
            scan_logs.append(f"Scanned parcel: {barcode}")     # Log success

    # 🔹 FOR/ELSE — runs ONLY if loop completed without break
    else:
        scan_logs.append("All parcels scanned successfully")    # 🎉 All done!

    return scan_logs                                    # Return the full log list


# 🔹 Test with a mixed list (has DAMAGED and STOP barcodes)
parcel_codes = ["1234", "5678", "DAMAGED", "9101", "1112", "STOP", "1314"]
print(scan_parcels(parcel_codes))

# 💡 EXPECTED OUTPUT:
# ['Scanned parcel: 1234',
#  'Scanned parcel: 5678',
#  'Skipped damaged parcel',
#  'Scanned parcel: 9101',
#  'Scanned parcel: 1112',
#  'Critical error: Stopping scan']
# (No "All parcels scanned" because STOP triggered break!)

# 💡 KEY TAKEAWAY:
#    This project combines ALL loop concepts learned so far.
#    Real-world code rarely uses just one concept — they work TOGETHER!

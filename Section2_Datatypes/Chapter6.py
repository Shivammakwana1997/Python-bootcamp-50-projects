chai_type = "Masala Chai"
customer_name = "Shivam"


print(f"Customer {customer_name} ordered {chai_type}")


chai_description = "Aromatic and bold"
print(f"firstword : {chai_description[:5]}")
print(f"lastword:  {chai_description[12:]}")
print(f"lastword: {chai_description[::-1]}")


label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")

print(f"Label type: {label_text}")
print(f"Encoded Label: {encoded_label}")


decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label: {decoded_label}")


raw_data = b"Tea\x20Leaves"
print(f"Raw data: {raw_data}")
print(f"Decoded: {raw_data.decode('utf-8')}")
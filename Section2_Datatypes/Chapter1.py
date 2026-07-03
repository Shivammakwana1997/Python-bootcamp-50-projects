### MMutable is always working with identity not value 
sugar_amount = 10
print(f"Initial sugar amount: {sugar_amount}")
print(type(sugar_amount))
print(id(sugar_amount))
sugar_amount = 20
print(f"Updated sugar amount: {sugar_amount}")
print(type(sugar_amount))
print(id(sugar_amount))


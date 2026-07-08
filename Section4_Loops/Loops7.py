def check_flavors(flavors: list):
    for flavor in flavors:
        if flavor == "out of stock":
            continue
        if flavor == "Discontinued":
            print(f"Discontinued item found: {flavor}")
            break
        print(f"Serving flavor: {flavor}")




# Example list to test the loop control
flavors_list = ["Masala", "Ginger", "out of stock", "Mint", "Discontinued", "Lemon"]
check_flavors(flavors_list)
print("out of the loops")
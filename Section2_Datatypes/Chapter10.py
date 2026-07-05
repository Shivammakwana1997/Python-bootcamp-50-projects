'''
Dictionary :- 
are mutable and are always written in {} brackets
'''
Chai_order = dict(type="Masala Chai",sugar="2 spoons",addons=["ginger","cardamom"])

print(f"type of chai order {Chai_order}")
print(f"type of chai order {type(Chai_order)}")


chai_recipe = {}
chai_recipe["base"]="blacktea"
chai_recipe["liquid"]="milk"


print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe liquid: {chai_recipe['liquid']}")
print(f"Recipe : {chai_recipe}")

del chai_recipe["liquid"]
print(f"Recipe : {chai_recipe}")


Chai_order = {"type":"Gingerchai","payment":"UPI","time":"11.34AM"}

print(f"order type {Chai_order.keys()}")
print(f"order payment {Chai_order.values()}")
print(f"order details {Chai_order.items()}")



last_item = Chai_order.popitem()
print(f"last item is {last_item}")

extra_spices ={"flavor":"Elaichi","color":"green"}
chai_recipe.update(extra_spices)
print(f"Update_Recipe : {chai_recipe}")


customer_note = Chai_order.get("Note","No notes")
print(f"Notes: {customer_note}")


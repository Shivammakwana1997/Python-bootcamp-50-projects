'''
Dictionary :- 
are mutable and are always written in {} brackets
'''
Chai_order = dict(type="Masala Chai",sugar="2 spoons",addons=["ginger","cardamom"])

print(f"type of chai order {Chai_order}")
print(f"type of chai order {type(Chai_order)}")


chai_recipe = {}
chai_recipe["base"]="blacktea"
chai_recipe["base"]="water"
print(f"type of chai order {chai_recipe}")
print(f"type of chai order {type(chai_recipe)}")
print(chai_recipe.keys())
print(chai_recipe.values())
print(chai_recipe.items())  
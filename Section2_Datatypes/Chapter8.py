''' 
List:- 
is a mutable data structure that is used to store multiple values in a single variable
Lists are ordered and allow duplicate values
They are defined using square brackets []
'''

import typing_extensions
import typing_extensions
import typing_extensions
import typing_extensions
import typing_extensions
ingredients = ["water", "milk", "tea leaves", "sugar"]
ingredients.append("Sugar")

print(f"The ingredients are:{ingredients}")


ingredients.remove("milk")
print(f"The ingredients are:{ingredients}")


spice_options = ["ginger","cardamom","clove"]
ingredients.extend(spice_options)
print(f"the new list is:{ingredients}")

#print(dir(list))


ingredients.insert(1,"green tea")
print(f"the new list is:{ingredients}")

last_Added = ingredients.pop()
print(f"{last_Added}")

print(f"chai : {ingredients}")
print(f"chai: {ingredients.reverse()}")

ingredients.reverse()
print(f"chai: {ingredients}")

ingredients.sort()
print(f"soreted_chai: {ingredients}")

sugar_level = [1,2,3,4,5]   
print(f"max sugar level {max(sugar_level)}")
print(f"min sugar level {min(sugar_level)}")


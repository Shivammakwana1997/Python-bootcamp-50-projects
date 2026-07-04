'''
Set :- 
is a mutable data structure that is used to store multiple values in a single variable
Sets are unordered and do not allow duplicate values
They are defined using curly braces {}
'''

essential_spices = {"cardamom", "Ginger", "clove"}
print(f"Essential spices: {essential_spices}")

print(f"Type of essential spices: {type(essential_spices)}")


optional_spices = {"black papper","fennel","Ginger"}                                    


all_spices =  optional_spices.union(essential_spices)
print(f"all spices: {all_spices}")


common_spices = optional_spices.intersection(essential_spices)
print(f"common spices: {common_spices}")

only_reserach = essential_spices - optional_spices

print(f"only reserach spices: {only_reserach}")


print(f"is ginger present in essential spices? {"Ginger" in essential_spices}")



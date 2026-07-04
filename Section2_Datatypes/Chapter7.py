'''
Tuple Datatypes
Tuple are immutable and are always written in () brackets
and is used when we want to store data that we don't want to change so tuple is immutable
'''

import typing_extensions
import typing_extensions
masala_blend = ("Cardamom", "Cinnamon", "Ginger", "Clove")
print(f"Masala Blend: {masala_blend}")

(spice1, spice2, spice3, spice4) = masala_blend
print(f"Spice 1: {spice1}")
print(f"Spice 2: {spice2}")
print(f"Spice 3: {spice3}")
print(f"Spice 4: {spice4}")

ginger_ratio , cadramom_ratio = 2,1
print(f"Ginger Ratio: {ginger_ratio} and cadramom_ratio : {cadramom_ratio}")

ginger_ratio , cadramom_ratio  = cadramom_ratio, ginger_ratio
print(f"Ginger Ratio: {ginger_ratio} and cadramom_ratio : {cadramom_ratio}")

###membership 

print(f"Is ginger present in masala spices ? {"masala" in masala_blend}")


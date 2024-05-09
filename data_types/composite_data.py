# LIST
list = ["Urabrask", "red", 4, 4.4, True]
print(list[1])

# TUPLE
tuple = ("Vorinclex", "green", 5, 6.6, True)  # Cannot be changed
print(tuple[1])

# SET
# Can be iterated but not accessed via indexes
# Disordered values
# No duplicate values
set = {"Sheoldred", "black", 4, 4.5, True}
print(set)

# DICT
dict = {
    "name": "Urabrask",
    "color": "Red",
    "cost": [2, "R", "R"],
    "power_toughness": 4.4,
    "legendary": True,
}
print(dict["name"])

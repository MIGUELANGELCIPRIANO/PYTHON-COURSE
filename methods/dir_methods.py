dictionary = {
    "name": "Urabrask",
    "color": "Red",
    "cost": [2, "R", "R"],
    "power_toughness": 4.4,
    "legendary": True,
}

# KEYS (Return the keys)
print(dictionary.keys())

# GET (Returns a key value. If it does not exist, the program continues)
print(dictionary.get("cost"))

# CLEAR (Removes all items)
# dictionary.clear()
# print(dictionary)

# POP (Removes an item from a list by requesting the index)
dictionary.pop("legendary")
print(dictionary)

# ITEMS (Iterates the dictionary)
print(dictionary.items())

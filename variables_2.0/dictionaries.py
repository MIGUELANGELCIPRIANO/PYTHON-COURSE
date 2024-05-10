# CREATE DICTIONARIES

# In dictionaries, tuples and sets (only as frozensets!) can be keys

red_praetor = dict(
    name="Urabrask",
    color="red",
    cost=[2, "R", "R"],
    power_toughness=4.4,
    legendary=True,
)
print(type(red_praetor))
print(red_praetor)

# CREATE DICTIONARIES WITH FROMKEYS()

# If the fromkeys() function only receives two parameters,
# the first one will be the iterable and each iterated element will correspond to a key
# and all of them will receive as value the second parameter

empty_praetor = dict.fromkeys(["name", "color", "cost", "power_toughness", "legendary"])
print(empty_praetor)

# FOR IN

praetors = ["Elesh-Norn", "Jin-Gitaxias", "Sheoldred", "Urabrask", "Vorinclex"]
numbers = [3.5, 5.5, 4.5, 4.4, 6.6]

# for praetor in praetors:
#     print(praetor)

# for number in numbers:
#     product = number * 10
#     print(product)

# # ZIP()

# for praetor, number in zip(praetors, numbers):
#     print(f"Phyrexian Praetor: {praetor}")
#     print(f"Power/Toughness: {number}")

# # RANGE()

# for number in range(10, 20):
#     print(number)

# for number in range(len(numbers)):  # Non-optimal way to iterate lists!
#     print(numbers[number])

# # ENUMERATE()

# for number in enumerate(numbers):
#     index = number[0]
#     value = number[1]
#     print(f"index = {index}, value = {value}")

# # FOR ELSE

# for praetor, number in zip(praetors, numbers):
#     print(f"Phyrexian Praetor: {praetor}")
#     print(f"Power/Toughness: {number}")
# else:
#     print("End of list")

# # FOR IN DICTIONARIES

# red_praetor = dict(
#     name="Urabrask",
#     color="red",
#     cost=[2, "R", "R"],
#     power_toughness=4.4,
#     legendary=True,
# )

# for key in red_praetor:
#     print(key)

# # ITEMS()

# for data in red_praetor.items():
#     key = data[0]
#     value = data[1]
#     print(f"{key} = {value}")

# CONTINUE & BREAK

for praetor in praetors:
    if praetor == "Sheoldred":
        continue
    print(praetor)

for praetor in praetors:
    print(praetor)
    if praetor == "Urabrask":
        break

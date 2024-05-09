# CREATE TUPLES

# Tuples are more optimal for storing fixed data because they are immutable,
# i.e., each piece of data represents a single memory space,
# unlike lists, where each piece of data has two memory spaces, one modifiable and one temporary.

first_way = tuple(["Elesh-Norn", "Jin-Gitaxias", "Sheoldred", "Urabrask", "Vorinclex"])
print(first_way)

second_way = "Elesh-Norn", "Jin-Gitaxias", "Sheoldred", "Urabrask", "Vorinclex"
print(second_way)

single_data_tuple = ("Urabrask",)
print(single_data_tuple)
print(type(single_data_tuple))

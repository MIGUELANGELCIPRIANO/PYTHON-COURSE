# SETS

praetors1 = frozenset({"Elesh-Norn", "Jin-Gitaxias", "Sheoldred"})
praetors2 = {praetors1, "Urabrask", "Vorinclex"}
print(type(praetors1))
print(praetors2)

# SET THEORY

praetors1 = {"Elesh-Norn", "Jin-Gitaxias", "Sheoldred", "Urabrask", "Vorinclex"}
praetors2 = {"Urabrask", "Vorinclex"}

# SUBSET CHECK

check_mode_1 = praetors1.issubset(praetors2)
print(check_mode_1)

check_mode_2 = praetors2 <= praetors1
print(check_mode_2)

# SUPERSET CHECK

check_mode_3 = praetors1.issuperset(praetors2)
print(check_mode_3)

check_mode_4 = praetors2 > praetors1
print(check_mode_4)

# COMMON DATA CHECK

check_mode_5 = praetors2.isdisjoint(praetors1)
print(check_mode_5)

list1 = ["white", "blue", "black"]
list2 = [1, 6, 89, -5, False, 54, 103, 45, 62, True]

# LIST (Create a list)
print(list())

# LEN (Counts the number of items in a list)
print(len(list1))

# APPEND (Add an item to the list)
list1.append("red")
print(list1)

# INSERT (Adds an item to the list at the specified index)
list1.insert(1, "green")
print(list1)

# EXTEND (Adds several items to the list)
list1.extend([True, 2024])
print(list1)

# POP (Removes an item from a list by requesting the index)
list1.pop(-2)  # == newlist.pop(5)
print(list1)

# REMOVE (Removes an item from a list by requesting the value)
list1.remove("blue")
print(list1)

# CLEAR (Removes all items from a list)
# list1.clear()
# print(list1)

# SORT (Sorts a list in ascending to descending order)
list2.sort()
print(list2)

# REVERSE (Inverts the elements of a list)
list2.reverse()
print(list2)

# NOTE: In the case of tuples and sets we can verify through the dir() function that the methods to apply are more limited since they are immutable

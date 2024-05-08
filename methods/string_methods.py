string1 = "Hi, I'm Tom"
string2 = "Hi Tom, nice to meet you!"
string3 = "Ismyfirstcommit"

# UPPER (Uppercase)
print(string1.upper())

# LOWER (Lowercase)
print(string1.lower())

# CAPITALIZE (First capital letter)
print(string1.capitalize())

# FIND (Returns the index of the value. If it does not exist, returns -1)
print(string1.find("T"))

# INDEX (Returns the index of the value. If it does not exist, returns an error)
# print(string1.index("t"))

# ISNUMERIC (If the value is numeric returns true)
print(string1.isnumeric())

# ISALPHA (If the value is alpha numeric returns true)
print(string3.isalpha())

# COUNT (Return the number of matches of the substring in the given string)
print(string2.count("t"))

# LEN (Counts the characters in a string)
print(len(string2))

# STARTSWITH (Checks if a string starts with the given value)
print(string2.startswith("hi"))

# ENDSWITH (Checks if a string ends with the given value)
print(string2.endswith("u!"))

# REPLACE (Substitutes the first parameter, if it matches the search, for the second parameter given)
print(string1.replace("Tom", "Zack"))

# SPLIT (Split by the given parameter)
print(string2.split(" "))

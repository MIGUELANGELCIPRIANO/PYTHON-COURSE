import re

text = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum."""

# SEARCH
# print(re.search("dolor", text))

# FIND ALL
# print(re.findall("dolor", text))

# \d : Search numeric values [0-9]
# print(re.findall(r"\d", text))

# \D : Search all values except numeric [0-9]
# print(re.findall(r"\D", text))

# \w : Search alphanumeric values [a-z A-Z 0-9 _]
# print(re.findall(r"\w", text))

# \W : Search all values except alphanumeric [a-z A-Z 0-9 _]
# print(re.findall(r"\W", text))

# \s : Search whitespace, tabs and line breaks [' ','\n']
# print(re.findall(r"\s", text))

# \S : Search all values except whitespace, tabs and line breaks [' ','\n']
# print(re.findall(r"\S", text))

# \n : Search line breaks ['\n']
# print(re.findall(r"\n", text))

# . : Search all values except line breaks ['\n']
# print(re.findall(r".", text))

# \ : Cancel special characters [a-z A-Z 0-9 _]
# print(re.findall(r"\.", text)) # Return all points of the text

# ^ : Search line start
# flags=re.M : Active multiline
# print(re.findall(r"^Lorem", text, flags=re.M))

# $ : Search line end
# print(re.findall(r"laborum.$", text, flags=re.M))

# {n} : Search "n" times left value
# print(re.findall(r"l{2}", text))

# {n,m} : Search "n" times minimum and "m" times maximum
# print(re.findall(r"l{1,2}", text))

# | : OR
# print(re.findall(r"l{1,2}|mollit", text))

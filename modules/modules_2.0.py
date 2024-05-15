# IMPORT MODULE IN THE SAME PATH

# import module_routing.greet_function

# print(module_routing.greet_function.greet("Jason"))

# IMPORT SYS

import sys

# print(sys.path)

sys.path.append("c:\\Users\\cipri_9p901s4\\Desktop\\PYTHON-COURSE\\module_routing")

import greet_function  # type: ignore

print(greet_function.greet("Jason"))

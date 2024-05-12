# ARGS PARAMETER (*)


def add_1(*numbers):
    return sum(numbers)


result = add_1(3.5, 5.5, 4.5, 4.4, 6.6)
print(result)


def add_2(numbers):
    return sum([*numbers])


result = add_2([3.5, 5.5, 4.5, 4.4, 6.6])
print(result)

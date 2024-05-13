# LAMBDA FUNCTION EXAMPLE

multiply = lambda x: x * 2

# EVEN NUMBERS FILTER FUNCTION

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_even(number):
    if number % 2 == 0:
        return True


even_numbers = filter(is_even, numbers)

# EVEN NUMBERS LAMBDA FUNCTIONS

even_numbers = filter(lambda number: number % 2 == 0, numbers)

print(list(even_numbers))

# PRIME NUMBER


def prime_number(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_numbers_upto(number):
    prime_numbers = []
    for i in range(number + 1):
        result = prime_number(i)
        if result == True:
            prime_numbers.append(i)
    return prime_numbers


prime_numbers = prime_numbers_upto(19)
print(prime_numbers)

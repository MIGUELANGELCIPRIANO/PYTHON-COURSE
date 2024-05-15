# FIBONACCI SERIES


def fibonacci(number):
    a, b = 0, 1
    fibonacci_series = [0]
    for i in range(number):
        if b > number:
            return fibonacci_series
        else:
            fibonacci_series.append(b)
            a, b = b, a + b


fibonacci_series = fibonacci(21)
print(fibonacci_series)

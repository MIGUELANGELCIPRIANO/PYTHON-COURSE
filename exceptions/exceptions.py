# EXCEPTION MANAGEMENT


def add():
    while True:
        a = input("Number 1: ")
        b = input("Number 2: ")
        try:
            result = int(a) + int(b)
        except Exception as e:
            print(f"ERROR: {e}")
        else:
            break
    return result


print(add())

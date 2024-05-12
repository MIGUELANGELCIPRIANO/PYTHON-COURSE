# RETURN FUNCTION


def random_password(number):
    characters = "abcdefghijklmnopqrstuvwxyz"
    string = str(number)
    interger = int(string[0])
    character_1 = interger - 2
    character_2 = interger
    character_3 = interger - 6
    character_4 = interger - 12
    password = f"{characters[character_1]}{characters[character_2]}{characters[character_3]}{characters[character_4]}{interger*2}{interger*3}"
    return password


new_password = random_password(98)
print(new_password)

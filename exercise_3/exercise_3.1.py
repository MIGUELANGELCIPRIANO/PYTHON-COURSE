# WORKING WITH TXT FILES

names = [
    "Leanne",
    "Ervin",
    "Clementine",
    "Patricia",
    "Chelsey",
    "Dennis",
    "Kurtis",
    "Nicholas",
    "Glenna",
    "Clementina",
]

lastnames = [
    "Graham",
    "Howell",
    "Bauch",
    "Lebsack",
    "Dietrich",
    "Schulist",
    "Weissnat",
    "Runolfsdottir",
    "Reichert",
    "DuBuque",
]

with open("exercise_3\\users.txt", "w") as file:
    file.writelines("Users:\n\n")
    [file.writelines(f"Name: {n}\nLastname: {l}\n\n") for n, l in zip(names, lastnames)]

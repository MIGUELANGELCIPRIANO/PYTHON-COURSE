# OVERWRITE FILE

# with open("files\\text_file.txt", "w", encoding="UTF-8") as file:
# file.write(
#     "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"
# )

# OVERWRITE FILE BY LINES

# with open("files\\text_file.txt", "w", encoding="UTF-8") as file:
#     file.writelines("Lorem ipsum dolor sit amet,\n", "consectetur adipiscing elit,")

# ADD TEXT LINE WITH FUNCTION


def new_line(linea):
    with open("files\\text_file.txt", "a", encoding="UTF-8") as file:
        file.write(f"{linea}\n")


new_line("Ut enim ad minim veniam,")

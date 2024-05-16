# OPEN AND CLOSE THE FILE AUTOMATICALLY

with open("files\\text_file.txt", encoding="UTF-8") as file:
    print(file.read())

# NOTE: It is not necessary to use "close()" to close the file. Open and close automatically using "with open()".

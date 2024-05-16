import csv

with open("csv_files\\csv_file_1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

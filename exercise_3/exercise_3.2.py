# WORKING WITH CSV FILES

import pandas as pd

dataframe = pd.read_csv("exercise_3\\csv_file.csv")

# DELETE DUPLICATES
dataframe = dataframe.drop_duplicates()

print(dataframe)

# CREATING A CLEAN DATAFRAME

dataframe.to_csv("exercise_3\\csv_clean_file.csv")

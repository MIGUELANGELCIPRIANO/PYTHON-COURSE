import pandas as pd

dataframe = pd.read_csv(
    "csv_files\\csv_file_1.csv",
    names=["name", "color", "cost", "power_toughness", "legendary"],
)
# print(dataframe)
# print(dataframe["name"])

# SORT
dataframe_order = dataframe.sort_values("power_toughness", ascending=False)
# print(dataframe_order)

# HEAD
first_lines = dataframe.head(2)
# print(first_lines)

# TAIL
last_lines = dataframe.tail(2)
# print(last_lines)

# SHAPE
rows_columns = dataframe.shape
# print(rows_columns)

# DESCRIBE
data = dataframe.describe()
# print(data)

# CONCAT
# dataframe_2 = pd.read_csv(
#     "csv_files\\csv_file_2.csv",
#     names=["name", "color", "cost", "power_toughness", "legendary"],
# )
# concatenated_dataframe = pd.concat([dataframe, dataframe_2])
# print(concatenated_dataframe)

# LOC
loc_cost = dataframe.loc[2, "cost"]
# print(loc_cost)

# ILOC
iloc_cost = dataframe.iloc[2, 2]
# print(iloc_cost)

names = dataframe.iloc[:, 0]
# print(names)

row_3 = dataframe.iloc[2, :]
# print(row_3)

more_power = dataframe.loc[dataframe["power_toughness"] > 5, :]
# print(more_power)

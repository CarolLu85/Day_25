# with open("./weather_data.csv", "r") as data_file:
#     data = data_file.readlines()

# import csv
# temperature = []
# with open("./weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             # new_temperature = int(row[1])
#             temperature.append(int(row[1]))
#
# print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
# below line has achieved the same goal that i did from line 4 to line 14 (via import csv)."temp" here is the name of that column.
# below is a panda's series object. if print the type of data["temp"]. a series is kinda like a list or single column of your table.
print(data["temp"])
# type checks, below is a dataframe (eg. the whole table)
print(type(data))

data_dict = data.to_dict()
temp_list = data["temp"].to_list()
print(temp_list)

# length = len(temp_list)
# total = sum(temp_list)
# average_temp = total / length
# below is an alternative of line "29 - 31"
average_temp = data["temp"].mean()
print(average_temp)

top_temp = data["temp"].max()
print(top_temp)

# get data in columns
print(data["condition"])
# below shows panda has already taken the strings in the first row as attributes.
print(data.condition)

# get data in row
print(data[data.day == "Monday"])
# data[data["day"]

# pull out the row with max temperature, via running below two codes, you get the same result.
print(data[data.temp == data["temp"].max()])
print(data[data["temp"] == data["temp"].max()])

# get a specific data from the table
monday = data[data.day == "Monday"]
print(monday.condition)

# get "monday's temperature"
monday = data[data.day == "Monday"]
# monday_C = monday.tem[0]
monday_F = (monday.temp)* 1.8 + 32
print(monday_F)

# create a dataframe from scratch
data_dict_a = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
b_data = pandas.DataFrame(data_dict_a)
data.to_csv("new_data_b.csv")
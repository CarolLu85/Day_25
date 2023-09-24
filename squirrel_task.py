import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# dictionary = {
#     "Fur Color": 2473,
#     "red": 392,
#     "black": 103,
# }

color_list = ["Gray", "Cinnamon", "Black"]
colors = data["Primary Fur Color"].to_list()
count_list = []
print(colors)
dictionary = {}
gray_num = 0
cinnamon_num = 0
black_num = 0
for color in colors:
    if color == "Gray":
        gray_num += 1
    if color == "Cinnamon":
        cinnamon_num += 1
    if color == "Black":
        black_num += 1

count_list.append(gray_num)
count_list.append(cinnamon_num)
count_list.append(black_num)

dictionary["Fur Color"] = color_list
dictionary["Count"] = count_list


# for a in dictionary:
#     print(dictionary[a])

squirrel_number = pandas.DataFrame(dictionary)
print(squirrel_number)
data.to_csv("squirrel_number.csv")




# Angela's
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dictionary)
# df.to_csv(squirrel_number.csv)
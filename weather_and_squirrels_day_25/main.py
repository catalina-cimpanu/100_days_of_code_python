# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# avg = sum(temp_list)/len(temp_list)
# print(avg)

# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in column
# print(data.temp)
# print(data["temp"])

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# # or
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)

# Create a data frame from scratch
# data_dict = {
#     "students": ["Ana", "Benny", "Cook"],
#     "scores": [78, 98, 85]
# }
#
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# new_data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("squirrel_count.csv")
fur_color = squirrel_data["Primary Fur Color"]
# print(fur_color)

# classical
all_gray = 0
all_cinnamon = 0
all_black = 0
for item in fur_color:
    if item == "Gray":
        all_gray += 1
    elif item == "Cinnamon":
        all_cinnamon += 1
    elif item == "Black":
        all_black += 1
print(all_gray, all_cinnamon, all_black)

# pandas - my way (probably complicated
all_gray = sum(fur_color.str.fullmatch("Gray")==True)
all_cinnamon = sum(fur_color.str.fullmatch("Cinnamon")==True)
all_black = sum(fur_color.str.fullmatch("Black".capitalize())==True)
print(all_gray, all_cinnamon, all_black)

# her way
grey_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count, red_squirrel_count,black_squirrel_count)

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [all_gray, all_cinnamon, all_black]
}

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_fur_count.csv")

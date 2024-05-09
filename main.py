# with open("weather_data.csv", "r") as f:
#     data = f.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(row[1])
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"]

# monday = data[data.day == "Monday"]
# monday_temperature_f = (monday.temp * 9/5) + 32
# print(monday.temp)
# print(monday_temperature_f)
# print(data.day[data.temp == data.temp.max()])

# Create a Dataframe from scratch.

data = pandas.read_csv("squirrel_data.csv")

cinnamon_squirrel_count = len(data["Primary Fur Color"][data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data["Primary Fur Color"][data["Primary Fur Color"] == "Black"])
grey_squirrel_count = len(data["Primary Fur Color"][data["Primary Fur Color"] == "Grey"])

data_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

pandas.DataFrame(data_dict).to_csv("data.csv")

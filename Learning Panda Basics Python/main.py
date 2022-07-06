# with open("weather_data.csv") as weather_data:
#     weather_data_list = weather_data.readlines()
#     for day in weather_data_list:
#         day.strip()
#     print(weather_data_list)

# import csv
#  opening and dealing with CSV files through built-in csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         else:
#             temperature.append(int(row[1]))
#     #     temperature.append(temp)
#     print(temperature)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# temp_list = data["temp"].to_list()
# data_dict = data.to_dict()
# # print(data_dict)
# # print(temp_list)
#
# average = sum(temp_list) / (len(temp_list))
# print(int(average))
##panda method for mean calculation is pre-made already, as you can see the code above and below give the same output
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data.temp.mean())
# print(data.condition)
## dot notation can be used because panda creates attributes named after the column headings

# #Getting a row
# monday = data[data.day == "Monday"]
# #Assigning a row to a variable and getting information from the row
# print(monday.condition)
# #Getting day with the max temperature
# print(data[data.temp == data.temp.max()])
#
# #Celsius to Fahrenheit: multiply by 1.8 (or 9/5) and add 32
# mon_temp_fahrenheit = (int(monday.temp)*1.8) + 32
# print(mon_temp_fahrenheit)
# print(monday.temp)

#Creating a data frame from scratch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores": [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

########################################################################################################################

                    #   Great Squirrel Census Data Analysis Project Day 25 #

########################################################################################################################

#TODO 1: Find the number of squirrels with each fur colour, there are only three of them

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])

squirrel_colour_dict = {
    "Gray": [0],
    "Cinnamon": [0],
    "Black": [0]
}

# Instructor Solution:

# gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# data_dict = {
#   "Fur Color": ["Gray", "Cinnamon", "Red"],
#   "Count": [gray_squirrel_count,red_squirrels_count,black_squirrels_count]
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")


for element in data["Primary Fur Color"]:
    if element == "Gray":
        squirrel_colour_dict["Gray"][0] += 1
    elif element == "Cinnamon":
        squirrel_colour_dict["Cinnamon"][0] += 1
    else:
        squirrel_colour_dict["Black"][0] += 1


#TODO 2: Take that data and build a new data frame from it

new_framework = pandas.DataFrame(squirrel_colour_dict)
print(new_framework)
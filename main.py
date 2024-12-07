# Reading a file/csv file
# Work with CSV
# Pandas
# Pandas data type 1 Frame(2 dimensional) 2 Series(1 dimensional)
# DataFrame methods - https://pandas.pydata.org/docs/reference/frame.html
# DataSeries - https://pandas.pydata.org/docs/reference/series.html
# Creat a mapping game

import csv
import pandas

CSV_FILE = "D:/Python/100 days Python Challenge/Intermediate/day 25/weather_data.csv"
# with open(CSV_FILE, mode="r") as file:
#     data_list = file.readlines()

# reading a file with CSV
# with open(CSV_FILE, mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
    
#     print(temperatures)

data = pandas.read_csv(CSV_FILE)
data_dic = data.to_dict()
#print(data_dic)
data_list = data["temp"].to_list()
#print(round(sum(data_list)/len(data_list), 2))
#print(data["temp"].max())

# Get data by colomuns | You can get data by accessing them via colomun name
#print(data["condition"])
#print(data.condition)


# Get data Row from the paper with method
#print(data[data.day == "Monday"])
#print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
print(monday.temp[0])
print((monday_temp * 9/5)+32)




data_dic = {
    "students" : ["Tom", "Rayly", "John"],
    "score" : [75, 46, 95]
}

my_data = pandas.DataFrame(data_dic)
print(my_data)

my_data.to_csv("New_data.csv")


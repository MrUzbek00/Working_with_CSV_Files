import pandas
squirrelt_data_set = "D:/Python/100 days Python Challenge/Intermediate/day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241107.csv"
with open(squirrelt_data_set) as file:
    file_data_set = pandas.read_csv(file)
count_dic =dict()
#print(file_data_set[file_data_set["Primary Fur Color"]=="Gray"])

#Get CSV file runs througgh colours and counts them pure ptyhon
def create_new_data_set(file):
    count = 0
    colour_list = ["Gray", "Cinnamon", "Black"]
    for colour in range(len(colour_list)):
        for n in range(len(file_data_set[file_data_set["Primary Fur Color"]== colour_list[colour]])):
            count += 1
            count_dic[colour_list[colour]] = count

    k_list =[]
    v_list =[]
    new_count_dic=dict()
    for v, k in count_dic.items():
        k_list.append(k)
        v_list.append(v)
        new_count_dic["colour"]= v_list
        new_count_dic["count"] = k_list
    my_data_set = pandas.DataFrame(new_count_dic)
    my_data_set.to_csv("My_Squirrel_data_set.csv")
    
    return my_data_set

#print(create_new_data_set(file=squirrelt_data_set))

gray_squirrel = len(file_data_set[file_data_set["Primary Fur Color"]== "Gray"])
cinnamon_squirrel = len(file_data_set[file_data_set["Primary Fur Color"]== "Cinnamon"])
black_squirrel = len(file_data_set[file_data_set["Primary Fur Color"]== "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "color": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Pandas_Squirrel.csv")












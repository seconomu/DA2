import math

def read_data(filename):
    # opens filename for reading and loads the column names into a 
    # 1D list called headers and loads the data into a 2D list called data
    infile = open(filename, "r")
    data = []
    headers = []
    lines = infile.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    labels = lines.pop(0)
    headers = labels.split(",")
    for line in lines:
        values = line.split(",") # 1D list
        data.append(values)
    infile.close()
    return headers, data


def display_table(headers, data): 
    # Displays the header row and the data in a grid-like table format   
    for value in headers:
        offset = 20 - len(value) # create an offset to account for element length differences
        print(value, end=(offset * ' ')) # add offset spaces to line up columns
    print("")
    
    for row in data:
        for value in row:
            offset = 20 - len(value)
            print(value, end=(offset * ' '))
        print("")


def get_column(column_name, headers, data):
    # find the column name index
    column_index = 0 
    match = False
    for name in range(len(headers)):
        if headers[name] == column_name:
            column_index = name
            match = True
    if match == False:     
        print("I'm sorry, that column does not exist.")
    column_data = []
    for i in range(len(data)):
            column_data.append(data[i][column_index])  
    return column_data      

def change_to_numeric(data):
    num_list = []
    for value in data:
        num_list.append(float(value))
    return num_list

def statistics_sum(data):
    # get the sum of the list elements 
    list_sum = 0
    for element in data:
        list_sum = list_sum + element
    return list_sum

def statistics_average(data):
    # calculate the average value of the elements (the mean)
    list_sum = statistics_sum(data)
    list_average = list_sum / len(data)
    return list_average

def statistics_stddev(data):
    # get the standard deviation
    list_average = statistics_average(data)
    list_of_means = []
    for x in data: # subtract mean from element
        list_of_means.append((x - list_average) ** 2)
    means_average = 0
    for x in list_of_means: # get the sum of the means
        means_average = means_average + x
    means_average = means_average / len(list_of_means) # get the average of the means
    std_dev = math.sqrt(means_average)
    return std_dev

def statistics_median(data):
    #sort the list to get the median, largest, and smallest numbers
    my_list_sorted = data[:] 
    my_list_sorted.sort() 
    median_number = my_list_sorted[int(round((len(my_list_sorted)/2),0))]
    return median_number

def statistics_high_num(data):
    # get the date for the smallest and largest value
    high_num = 0
    high_num_index = 0
    for i in range(len(data)):
        if data[i] > high_num:
            high_num = data[i]
            high_num_index = i
    return high_num, high_num_index

def statistics_low_num(data):
    high_num = statistics_high_num(data)[0]
    low_num = high_num  
    low_num_index = 0
    for i in range(len(data)):
        if data[i] < low_num:
            low_num = data[i]
            low_num_index = i
    return low_num, low_num_index
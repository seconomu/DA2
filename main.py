import utils

# ------- LOAD THE FILES AND CHOOSE DATA -----------------
test_file = utils.read_data("fitbit_data_3-8_9-16.csv")
#test_file2 = utils.read_data("Lake Arthur Data.csv")
print("")
utils.display_table(test_file[0], test_file[1])
#utils.display_table(test_file2[0], test_file2[1])
print("What data would you like to look at?")
data_name = input()
#data_name = 'Steps'

#--------------------- FUNCTION CALLS --------------------------
column = utils.get_column(data_name, test_file[0], test_file[1])
#column = utils.get_column(data_name, test_file2[0], test_file2[1])
column_data = utils.change_to_numeric(column)
data_sum = int(utils.statistics_sum(column_data))
data_average = utils.statistics_average(column_data)
data_std_dev = utils.statistics_stddev(column_data)
data_median = int(utils.statistics_median(column_data))
data_low_num = utils.statistics_low_num(column_data)
data_high_num = utils.statistics_high_num(column_data)
low_num_date = test_file[1][data_low_num[1]][0]
high_num_date = test_file[1][data_high_num[1]][0]


# --------------------- RESULTS ---------------------------------------
print("")
print("There are ", len(column_data), " records for ", data_name, ".", sep='')
print("The total number of ", data_name, " is ", data_sum, '.', sep='')
print("The average number of ", data_name, " is ", int(data_average), ".", sep='')
print("The standard deviation for ", data_name, " is ", int(data_std_dev), ".", sep='')
print("The median number for ", data_name, " is ", data_median, ".", sep='')
print("The smallest number for ", data_name, " is ", data_low_num[0], " on ", low_num_date,".", sep='')
print("The largest number for ", data_name, " is ", data_high_num[0], " on ", high_num_date,".", sep='')



# ------------- BONUS QUESTION ANALYSIS --------------------------------
# Did the exercise patterns change after the marathon?   No significant change
# Did the exercise patterns change once fall semester started (8/31)?  No significant change
# Assumption: The marathon is the day with the highest steps/distance.

# print("What is the name of the column with the dates? ")
# date_column = input()
date_column = 'Date'
# print("What data column would you like to use? ")
# data_col = input()
data_col = 'Distance'
# print("Enter a beginning date for analysis: ")
# beginning_date = input()
beginning_date = '7/1/21'
# print("Enter an ending date")
# ending_date = input()
ending_date = '9/1/21'
data_slice = utils.slice_column(utils.get_column(date_column, test_file[0], test_file[1]), utils.get_column(data_col,test_file[0], test_file[1]), beginning_date, ending_date)
date_slice = utils.slice_column(utils.get_column(date_column, test_file[0], test_file[1]), utils.get_column(date_column,test_file[0], test_file[1]), beginning_date, ending_date)
data_slice_header = [date_column, data_col]
print("")
print("")
nested_list = utils.create_nested_list(date_slice, data_slice) #create a table for display
utils.display_table(data_slice_header, nested_list)

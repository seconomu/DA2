import utils

# ------- LOAD THE FILES AND CHOOSE DATA -----------------
test_file = utils.read_data("fitbit_data_3-8_9-16.csv")
test_file2 = utils.read_data("Lake Arthur Data.csv")
print("")
#utils.display_table(test_file[0], test_file[1])
utils.display_table(test_file2[0], test_file2[1])
print("What data would you like to look at?")
data_name = input()
#data_name = 'Steps'

#--------------------- FUNCTION CALLS --------------------------
#column = utils.get_column(data_name, test_file[0], test_file[1])
column = utils.get_column(data_name, test_file2[0], test_file2[1])
column_data = utils.change_to_numeric(column)
data_sum = int(utils.statistics_sum(column_data))
data_average = utils.statistics_average(column_data)
data_std_dev = utils.statistics_stddev(column_data)
data_median = int(utils.statistics_median(column_data))
data_low_num = utils.statistics_low_num(column_data)
data_high_num = utils.statistics_high_num(column_data)
low_num_date = test_file2[1][data_low_num[1]][0]
high_num_date = test_file2[1][data_high_num[1]][0]

# --------------------- RESULTS ---------------------------------------
print("")
print("There are ", len(column_data), " records for ", data_name, ".", sep='')
print("The total number of ", data_name, " is ", data_sum, '.', sep='')
print("The average number of ", data_name, " is ", int(data_average), ".", sep='')
print("The standard deviation for ", data_name, " is ", int(data_std_dev), ".", sep='')
print("The median number for ", data_name, " is ", data_median, ".", sep='')
print("The smallest number for ", data_name, " is ", data_low_num[0], " on ", low_num_date,".", sep='')
print("The largest number for ", data_name, " is ", data_high_num[0], " on ", high_num_date,".", sep='')

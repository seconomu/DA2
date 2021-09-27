import utils

test_file = utils.read_data("fitbit_data_3-8_9-16.csv")
test_file2 = utils.read_data("lake_arthur_monitoring.csv")
print("")
#print(len(test_file[0][6]))
#utils.display_table(test_file[0], test_file[1])
print("What data would you like to look at?")
data_name = input()
#utils.statistics(data_name, test_file[0], test_file[1])
utils.statistics(data_name, test_file[0], test_file[1])
#utils.statistics(data_name, test_file2[0], test_file2[1])

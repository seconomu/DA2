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
        offset = 22 - len(value) # create an offset to account for element length differences
        print(value, end=(offset * ' ')) # add offset spaces to line up columns
    print("")
    
    for row in data:
        for value in row:
            offset = 22 - len(value)
            print(value, end=(offset * ' '))
        print("")
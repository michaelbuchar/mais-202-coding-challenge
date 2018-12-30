import csv
import numpy as np
import matplotlib.pyplot as plt

class interest_rate_calc:

    ### IMPORTS DATA FROM THE CSV FILE
    f = open('data.csv') # opens the file
    csv = csv.reader(f) # csv reader
    values = [] # a list with (purpose, interest_rate)
    possible_purposes = set() # a set with no duplicates that stores all purposes

    # Getting the values
    for row in csv:
        purpose = row[16] # extracts the purpose
        interest_rate = row[5] # extracts the interest rate
        values.append((purpose, interest_rate))
        if purpose != 'purpose': # doesnt store the value purpose in the possible_purposes set
            possible_purposes.add(row[16])

    ### CREATES THE OUTPUT
    output = [] # a list with (purpose, avg_interest_rate)

    for set in possible_purposes: # for every set in possible purposes
       total_value = 0 # the total value of added interest rates with a given purpose
       num_of_values = 0 # the total number of values with a given purpose

       for value in values: # loop through every value in values
           if set == value[0]: # if set is the same as the purpose in value
               correct_val = round(float(value[1]), 2) # to ensure correct parsing to float type (double)
               # round to 2 decimal numbers
               total_value += correct_val # adds to the total value
               num_of_values += 1 # adds one to the total number of values

       avg_value = round(total_value/num_of_values, 6) # computes average value rounded to six decimal figures
       output.append((set, avg_value)) # adds into the output list

class bar_graph:
    output = interest_rate_calc.output # imports output

    objects = [] # a list with purposes
    y_pos = [] # a list with average values
    for data in output: # adds data to the lists
        objects.append(data[0])
        y_pos.append(data[1])
    x_pos = np.arange(len(objects)) # creates a list with numbers 0 to len(objects)

    plt.figure(figsize= (16,8)) # resize the figure so that the labels on the x-axis are visible
    plt.bar(x_pos, y_pos, align='center', alpha=0.5, color = ['teal', 'red', 'navy', 'magenta', 'cyan', 'purple',
                                                              'green', 'yellow', 'gray'])
    # alpha sets transparency, aligns bars to the center of the labels and sets colors
    plt.xticks(x_pos, objects) # assigns the objects list to the bars (renames the xticks)
    plt.ylabel('mean(int_rate)') # sets the ylabel
    plt.xlabel('purpose') # sets the xlabel
    plt.title('Bar graph') # sets the title
    plt.savefig('bar_graph.png') # saves the bar_graph into the same folder

class table:
    def second(element): # method to help in sorting the output
        return element[1]

    output = interest_rate_calc.output # imports the output
    output.sort(key=second, reverse=True) # sorts the output by the second argument (avg_value)

    colLabels = ['purpose', 'avg_rate'] # labels of the graph columns
    purpose = [] # list with the purposes, to determine the number of cols of the table
    for data in output: # stores data in the lists
        purpose.append(data[0])

    rowLabels = np.arange(len(purpose)) # creates a list with numbers 0 to len(purpose)
    cellText = [] # a list with the outputs (purpose, avg_rate)
    for value in output:
        cellText.append(value)

    fig, ax = plt.subplots()  # ax = axis, fig = figure
    ax.axis('off') # hides axes
    ax.table(cellText=cellText, rowLabels=rowLabels, cellLoc='left',
             colWidths=[.5, .2], colLabels=colLabels, loc='center') # sets parameters of the table
    plt.savefig('table.png') # saves the table into the same folder

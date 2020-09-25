import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# must define out of loops
total_months = 0
total_money = 0
# need b2 and b3 cause couldn't have iterating list with 2 values iterating (aka row[1] and first_row[1])
# made 2 new lists to then minus (eventually) from one another
row_b2_values = []
row_b3_values = []
# net_change date cause asked to print out date for greatest increase/decrease
net_change_date = []
net_change_values = []

with open(budget_csv) as csv_file:
    csv_budget = csv.reader(csv_file, delimiter=",")
    # skip 1 for for b2
    header = next(csv_budget)

    for row in csv_budget:

        # sum row count
        total_months += 1       

        # sum for total money
        total_money += int(row[1])

        # make list for b2 rows onward
        row_b2 = int(row[1])
        row_b2_values += [row_b2]


with open(budget_csv) as csv_file:
    csv_budget = csv.reader(csv_file, delimiter=",")
    header = next(csv_budget)
    # skip 2 rows to start at b3 (so you can get list to subtract)
    first_row = next(csv_budget)

    for row in csv_budget:

        # make list of b3 onwards
        row_b3 = int(row[1])
        row_b3_values += [row_b3]

        # get date net change from row 0 (so you can use it to find date of net_change)
        net_change_date += [row[0]]

# remove last value from b2 list so you can do zip/the lists line up
row_b2_values.remove(671099)

# SPAGHETTI BASED OFF OF:
# https://stackoverflow.com/questions/11677860/subtract-values-in-one-list-from-corresponding-values-in-another-list
# SPAGHETTI = net_change_values = [row_b3_values - row_b2_values for row_b3_values, row_b2_values in zip(row_b3_values, row_b2_values)]
# see below for figuring out what it means/unraveling it
# zip = Adding two lists of equal lengths element-wise resulting in 1 list
for row_b3_values, row_b2_values in zip(row_b3_values, row_b2_values):
        net_change_values.append(row_b3_values - row_b2_values)
    
# define increase based on net_change_values YAY FINALLY GOT NET CHANGE
increase = max(net_change_values)
decrease = min(net_change_values)

# find indes of the increase/decrease soo....
index_increase = net_change_values.index(increase)
index_decrease = net_change_values.index(decrease)

# ...you can make an f statement that will print out the date based of index & the increase/decrease value
greatest_increase = f"{net_change_date[index_increase]} (${increase})"
greatest_decrease = f"{net_change_date[index_decrease]} (${decrease})"

# NOW you get average change based off of sum/len
average_change = sum(net_change_values) / len(net_change_values)

# PRINT ALL THE THINGS
print("Finacial Analysis")
print("-----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_money}")
# reduce decimals down to 2 = .2f
print(f"Average Change: ${average_change:.2f}") 
print(f"Greatest Increase in Profits: {greatest_increase}")    
print(f"Greatest Decrease in Profits: {greatest_decrease}")

# now text print out to Anyalysis
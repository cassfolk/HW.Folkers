import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_money = 0
# make empty lists to shove the values into
net_change_values = []
net_change_date = []

with open(budget_csv) as csv_file:
    csv_budget = csv.reader(csv_file, delimiter=",")
    header = next(csv_budget)
    # skips down 2 rows 
    first_row = next(csv_budget)

    # because of first row (for net change) sets values as row 1 before 
    total_months += 1
    total_money += int(first_row[1])

    # makes variable for 2nd row to use
    previous_next = int(first_row[1])

    for row in csv_budget:

        #sum row count
        total_months += 1       

        # sum for total money
        total_money += int(row[1])

        # get net change (aka diff between b2 & b3 etc)
        net_change = int(row[1]) - previous_next
        # makes it so previous_next is not a static value of 2nd row
        previous_next = int(row[1])
        # adds net_change to net_change_values list
        net_change_values += [net_change]
    
        #get DATE net change from row 0 (so you can use it to find date of net_change)
        net_change_date += [row[0]]

# define increase based on net_change_values YAY FINALLY GOT NET CHANGE
increase = max(net_change_values)
decrease = min(net_change_values)

# find indexs of the increase/decrease soo....
index_increase = net_change_values.index(increase)
index_decrease = net_change_values.index(decrease)

# ...you can make an f statement that will print out the date based of index & the increase/decrease valuee
greatest_increase = f"{net_change_date[index_increase]} (${increase})"
greatest_decrease = f"{net_change_date[index_decrease]} (${decrease})"

# NOW you get average change based off of sum/len
average_change = sum(net_change_values) / len(net_change_values)

# print all the things
print("Finacial Analysis")
print("-----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_money}")

# reduce decimals down to 2 = .2f
print(f"Average Change: ${average_change:.2f}") 
print(f"Greatest Increase in Profits: {greatest_increase}")    
print(f"Greatest Decrease in Profits: {greatest_decrease}")  
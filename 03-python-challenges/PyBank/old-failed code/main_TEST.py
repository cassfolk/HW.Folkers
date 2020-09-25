import os
import csv

budegt_csv = os.path.join("Resources", "budget_data.csv")

# total_months = 0
# total_money = 0
net_change_values = []
net_change_date = []

with open(budegt_csv) as csv_file:
    csv_budget = csv.reader(csv_file, delimiter=',')
    header = next(csv_budget)
    first_row = next(csv_budget)

    previous_next = int(first_row[1])

    for row in csv_budget:
        net_change = int(row[1]) - previous_next
        net_change_values += [net_change]

        print(previous_next)
        #still does first row value for all
import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_money = 0
net_change_values = []
net_change_date = []

with open(budget_csv) as csv_file:
    csv_budget = csv.reader(csv_file, delimiter=",")
    header = next(csv_budget)
    first_row = next(csv_budget)

    #because of first row (for net change) sets values as row 1 before 
    total_months += 1
    total_money += int(first_row[1])

    #*******THERE RIGHT THERE********
    previous_next = int(first_row[1])

    #count rows MINUS HEADER (above) for file
    for row in csv_budget:

        #sum row count
        total_months += 1       

        #sum for total money
        total_money += int(row[1])

        #get net change (aka diff between b2 & b3 etc)
        #*******THERE RIGHT THERE********
        net_change = int(row[1]) - previous_next
        net_change_values += [net_change]
    
        #get date net change from row 0 (so you can use it to find date of net_change)
        net_change_date += [row[0]]
       
        print(previous_next)
        # print(int(row[1]))
        # print(int(first_row[1]))

increase = max(net_change_values)
decrease = min(net_change_values)

index_increase = net_change_values.index(increase)
index_decrease = net_change_values.index(decrease)

greatest_increase = f"{net_change_date[index_increase]} (${increase})"
greatest_decrease = f"{net_change_date[index_decrease]} (${decrease})"

average_change = sum(net_change_values) / len(net_change_values)

# print(net_change_values)
# print(sum(net_change_values))
# print(len(net_change_values))

print("Finacial Analysis")
print("-----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_money}")

#reduce decimals down to 2 = .2f
print(f"Average Change: ${average_change:.2f}") 

print(f"Greatest Increase in Profits: {greatest_increase}")    
print(f"Greatest Decrease in Profits: {greatest_decrease}")  
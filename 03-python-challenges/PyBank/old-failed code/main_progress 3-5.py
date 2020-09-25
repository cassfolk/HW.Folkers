import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")


# def get_change(budget_data):
#     current = (row[1])
#     previous = (row[1] + 1)

#     if current == previous:
#         return ((current - previous) / previous)

total_months = 0
total_money = 0
net_change_values = []

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    first_row = next(csv_reader)

    previous_next = int(first_row[1])

    print("Finacial Analysis")
    print("-----------------------")
    
    #define outside of loop
    # total_months = 0
    # total_money = 0
    # net_change_values = []
    # # sum_net = []
    # # len_net = []

    #count rows MINUS HEADER (above) for file
    for row in csv_reader:
        profit_loss = (row[1])
        #sum row count
        total_months += 1

        #sum for total money
        total_money = total_money + int(row[1])

        #get net change (aka diff between b2 & b3 etc)
        net_change = int(row[1]) - int(previous_next)
        net_change_values += [net_change]

        #average of the changes
        # average_change.append(net_change)

        # sum_net.append(sum(net_change))
        # len_net.append(len(range(net_change)))



        # if net_change == 0:
        #     average_change.append(0)
        # else:
        #     average_change.append((sum(range(net_change)) / len(range(net_change))))
        # print(average)
        
        
        # if net_change == 0:
        #     net_change = net_change

        # if (sum(range(net_change)) / len(range(net_change))) == 0:
        #     average_change.append(0)
        # else:
        #     average_change.append((sum(range(net_change)) / len(range(net_change))))




        #GREATEST INCREASE

        #can't use max, not interable
        #greatest_increase in if so not availabe outside
        #greatest_increase = max(profit_loss)


        # #greatest decrease
        # #can't use min, not intreable
        # decrease = min(-2196167)
        # great_decrease = f"{row}" 



        #(f"{row[0]} ({row[1]})")
            
    # print(sum_net)

average_change = (sum(net_change_values) / len(net_change_values))

print(f"Total Months: {total_months}")
print(f"Total: ${total_money}")
print(f"Average Change: ${average_change}") 
#print(f"Greatest Increase in Profits: {greatest_increase}")    
# print(f"Greatest Decrease in Profits: {great_decrease}")  
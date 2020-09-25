import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)

    print("Finacial Analysis")
    print("-----------------------")

    #define outside of loop
    total_months = 0
    total_money = 0

    #count rows MINUS HEADER (above) for file
    for row in csv_reader:
        
        #sum row count
        total_months += 1

        #sum for total money
        total_money = total_money + int(row[1])

        #average of the changes???? 
        # WRONG BELOW - average only
        #average_change = float(total_money / total_months)



    print(f"Total Months: {total_months}")
    print(f"Total: ${total_money}")
    #print(f"Average Change: ${average_change}") 
    #print(f"Greatest Increase in Profits: {great_increase}")  
    #print(f"Greatest Decrease in Profits: {great_decrease}")  
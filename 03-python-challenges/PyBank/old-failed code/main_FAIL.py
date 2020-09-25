import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

def print_budget(budget_data):
    #date = str(budget_data[0])
    #money = int(budget_data[1])

    #total_months = sumd(date)
    
    print("Finacial Analysis")
    print("-----------------------")
    #print(f"Total Months: {total_months}")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:
        print(print_budget(row))
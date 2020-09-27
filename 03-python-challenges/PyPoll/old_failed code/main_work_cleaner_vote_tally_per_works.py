# " - correct" = this part is working yay (checked with printing)


import os 
import csv

election_csv = os.path.join("Resources", "election_data_MINI.csv")

total_votes = 0
#list of candidates (to be used for loop & for dict calling on names)
candidates = ["Khan", "Correy", "Li", "O'Tooley"]

#dictionaries to hold % and vote values
candidates_percent = {"Khan": 0, "Correy": 0, "Li": 0, "O'Tooley": 0}
candidates_votes = {"Khan": 0, "Correy": 0, "Li": 0, "O'Tooley": 0}


def vote_print(name, candidates_votes, candidates_percent):

    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------")
    

    for name in candidates:
        print(f"{name}: {candidates_percent[name]:.2f}% ({candidates_votes[name]})")


with open(election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        # sum all votes - correct
        total_votes += 1

        candidates_votes[row[2]] += 1
    
    for name in candidates:
        candidates_percent[name] = round(((candidates_votes[name] / total_votes) * 100))
   

    vote_print(candidates, candidates_votes, candidates_percent)


winnner = max(candidates_votes[candidates])

print("-----------------------")
print(f"Winner: {winnner}")
print("-----------------------")



    

# # NEED TO PRINT TO TEXT
# out_put = os.path.join("Analysis", "New_Poll_Analysis.txt")
# with open(out_put, 'w') as csv_output:

#     csvwriter = csv.writer(csv_output, delimiter=',')
    
#     csvwriter.writerow(["TEXT HERE"])
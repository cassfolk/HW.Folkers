# " - correct" = this part is working yay (checked with printing)


import os 
import csv

election_csv = os.path.join("Resources", "election_data_MINI.csv")

total_votes = 0
# candidate_votes = 0
# candidate_percent = 0
# candidates = ["Khan", "Correy", "Li", "O'Tooley"]
# candidate_vote_totals = [0, 0, 0, 0]

candidates = ["Khan", "Correy", "Li", "O'Tooley"]

candidates_info = {"Khan": 0, "Correy": 0, "Li": 0, "O'Tooley": 0}

def vote_print(name, candidates_info):
    
    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------")
    
    for name in candidates:
        print(f"{name} {candidates_info[name]}")

    # candidate_percent = (candidate_votes / total_votes) * 100

    # print(f"{name}: {candidate_percent}% ({candidate_votes})")


with open(election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        # sum all votes - correct
        total_votes += 1

        candidates_info[row[2]] += 1



    vote_print(candidates, candidates_info)
    
    # print("-----------------------")
    # # print(f"Winner: {}")
    # print("-----------------------")

    

# # NEED TO PRINT TO TEXT
# out_put = os.path.join("Analysis", "New_Poll_Analysis.txt")
# with open(out_put, 'w') as csv_output:

#     csvwriter = csv.writer(csv_output, delimiter=',')
    
#     csvwriter.writerow(["TEXT HERE"])
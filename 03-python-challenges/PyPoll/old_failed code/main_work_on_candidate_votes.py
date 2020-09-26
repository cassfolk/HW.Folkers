# " - correct" = this part is working yay (checked with printing)

#Cannot get function to impact candidate_votes/candidate_vote_totals


import os 
import csv

election_csv = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_votes = 0
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
candidate_vote_totals = []

def vote_divide(vote_calc):
    candidate_votes = 1
    candidate_percent = 2
    candidate_vote_totals = []

    # # Kept giving error of string out of range
    # candidates_cast = str(vote_data[2])
    # if (name == candidates_cast):
    #     for row in csvreader:
    #         candidate_votes += 1

    for row in csvreader:
        
        if (name == row[2]):
            
            candidate_votes += 1
            candidate_vote_totals = [candidate_votes]




    #total_votes works/reads as 3521001 when print here
    # this works---ish
    # print(f"{name} {candidate_votes}")

    # candidate_percent = (candidate_votes / total_votes) * 100

    print(f"{name}: {candidate_percent}% ({candidate_votes})")




with open(election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        # sum all votes - correct
        total_votes += 1

    # print("Election Results")
    # print("-----------------------")
    # print(f"Total Votes: {total_votes}")
    # print("-----------------------")
    for name in candidates:
        vote_divide(name)
    
    # print("-----------------------")
    # # print(f"Winner: {}")
    # print("-----------------------")

# functions--> with --> for loops --> calculations using functions



# candidates listed out

# votes per candidate

# maybe do function for % / number? 
# where name = Khan, do %
# where name = Khan, do number


# display winner
    

# # NEED TO PRINT TO TEXT
# out_put = os.path.join("Analysis", "New_Poll_Analysis.txt")
# with open(out_put, 'w') as csv_output:

#     csvwriter = csv.writer(csv_output, delimiter=',')
    
#     csvwriter.writerow(["TEXT HERE"])
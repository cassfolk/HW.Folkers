# " - correct" = this part is working yay (checked with printing)


import os 
import csv

election_csv = os.path.join("Resources", "election_data_MINI.csv")

total_votes = 0
#empty list to toss winner in
winner = []
#list of candidates (to be used for loop & for dict calling on names)
candidates = ["Khan", "Correy", "Li", "O'Tooley"]

#dictionaries to hold % and vote values
candidates_percent = {"Khan": 0, "Correy": 0, "Li": 0, "O'Tooley": 0}
candidates_votes = {"Khan": 0, "Correy": 0, "Li": 0, "O'Tooley": 0}

#function of happy to print the candidates + % + #
def vote_print(name, candidates_votes, candidates_percent):

    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------")
    
    # loop through candidates and print _____
    for name in candidates:
        print(f"{name}: {candidates_percent[name]:.2f}% ({candidates_votes[name]})")


with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        # sum all votes - correct
        total_votes += 1

        # add votes to candidate vote total based on if name is in row 2, add 1
        candidates_votes[row[2]] += 1
    
    for name in candidates:
        # round % of candidates vote (by name) / total votes * 100 to be percent #
        candidates_percent[name] = round(((candidates_votes[name] / total_votes) * 100))

    # use function with multiple arguments (yay understanding)    
    vote_print(candidates, candidates_votes, candidates_percent)

    # max code in a dictionary
    # yay google https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
    winnner = max(candidates_votes, key=candidates_votes.get)
    print("-----------------------")
    print(f"Winner: {winnner}")
    print("-----------------------")   



# PRINT TO TEXT
out_put = os.path.join("Analysis", "New_Poll_Analysis.txt")

with open(out_put, 'w', newline='') as csv_output:
    outputfile = csv.writer(csv_output, delimiter=',')
    

    # print(["Election Results"])
    # print(["-----------------------"])
    # print([f"Total Votes: {total_votes}"])
    # print(["-----------------------"])

    outputfile.writerow([f"{vote_print(candidates, candidates_votes, candidates_percent)})"])
    outputfile.writerow(["-----------------------"])
    outputfile.writerow([f"Winner: {winnner}"])
    outputfile.writerow(["-----------------------"])

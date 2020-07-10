import os
import csv

#set the election_data file path
datapath = os.path.join("", "Resources", "election_data.csv")

#open the election_data file
with open(datapath, 'r') as datafile:

    #skip the header row
    data_header = next(datafile)
    
    #specify the datafile delimiter and stores the file content
    election_results = csv.reader(datafile, delimiter=",")

    #create a list of the candidates that received votes and their results
    candidates = []
    results = []
    #set the global veriables
    total_votes = 0
    most_votes = 0
    percent = 0

    for row in election_results:
        #tally the total votes
        total_votes = total_votes + 1
        #create candidates list
        name = row[2]
        if name not in candidates:
            candidates.append(name)
            #the first time we find a new candidate they get 1 vote
            results.append({"name" : name, "votes" : 1, "percent": percent})
        else:
            #each time we find an existing candidate we add 1 to their votes in the results list
            for item in results:
                if name == item["name"]:
                    item["votes"] += 1

# calculate the percentage of votes each candidate received
for item in results:
    percent =f'{(item["votes"]/total_votes) * 100: .3f}'
    item["percent"] = percent

#check for the winner
for item in results:
    if most_votes < item["votes"]:
        most_votes = item["votes"]
        winner = item["name"]

#display the election results
print(f"\nElection Results")
print(f"--------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------")
for item in results:
    print(f"{item['name']}: {item['percent']}% ({item['votes']})")
print(f"--------------------------")
print(f"Winner: {winner}")
print(f"--------------------------\n")

# write the analysis results to fin_analysis.txt file.
analysispath = os.path.join("", "Analysis", "election_results.txt")
with open(analysispath, 'w') as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f"--------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write(f"--------------------------\n")
    for item in results:
        textfile.write(f"{item['name']}: {item['percent']}% ({item['votes']}) \n")
    textfile.write(f"--------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write(f"--------------------------\n")
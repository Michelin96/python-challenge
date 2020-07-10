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

    #create a list of the candidates that received votes
    candidates = []
    results = []
    total_votes = 0
    votes = 0
    percent = 0

    for row in election_results:
        #tally the total votes
        total_votes = total_votes + 1
        #create candidates list
        if row[2] not in candidates:
            candidates.append(row[2])
            name = row[2]
            results.append({"name" : name, "votes" : 0, "percent": 0})
            

    # with open(datapath, 'r') as datafile:
    # #skip the header row
    # data_header = next(datafile)
    
    # #specify the datafile delimiter and stores the file content
    # election_results = csv.reader(datafile, delimiter=",")
print(f"\nElection Results")
print(f"--------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------")
for item in results:
    print(f"{item['name']}: {item['percent']}% ({item['votes']})")
print(f"--------------------------\n")
#print(f"Winner: {winner}\n")
print(f"--------------------------\n")
#print(f"Results Dictionary: {results}")
# #open the election_data file to tally the votes
# cndt_votes = 0
# results = []
# for name in candidates:
#     results.append({'votes': cndt_votes + 1})
# print(f"The results list: {results}")


#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
# check for the winner
# #for name in candidates:
#     if most_votes < candidates["votes"]:
#         most_votes = candidates["votes"]
#         winner = candidates["name"]


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
    #textfile.write(f"Winner: {winner}\n")
    textfile.write(f"--------------------------\n")
import os
import csv

#set the election_data file path
datapath = os.path.join("", "Resources", "election_data.csv")
# creates list of dictionaries referenced by name and votes
#each row of election data is evaluated and stored or appended to this list

#open the election_data file to get the total votes
with open(datapath, 'r') as datafile:
  
    #skip the header row
    data_header = next(datafile)
    
    #datareader specifies the delimiter and stores the file content
    datareader = csv.reader(datafile, delimiter=",")
    
    print(f"\nElection Results")
    print(f"--------------------------")

    votes = datafile.readlines()
    #get the number of votes in the election_results file
    total_votes = len(votes)
    print(f"Total Votes: {total_votes}")
    print(f"--------------------------")
#put all the file stuff outside the with
#watch heather's pre office hrs explaination  and implenent it
#open the election_data file for analysis
with open(datapath, 'r') as datafile:
  
    #skip the header row
    data_header = next(datafile)
    
    #specify the datafile delimiter and stores the file content
    election_results = csv.reader(datafile, delimiter=",")

    #create a list of the candidates that received votes
    candidates = []
    votes = []
    for row in election_results:
        if row[2] not in candidates:
            candidates.append(row[2])



    print(f"List of candidates: {candidates}")

#   * The total number of votes cast

#   * A complete list of candidates who received votes

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



# write the analysis results to fin_analysis.txt file.


analysispath = os.path.join("", "Analysis", "election_results.txt")
with open(analysispath, 'w') as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f"--------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write(f"--------------------------\n")
        
    # for item in candidates
    #     textfile.write(f"{candidate}: {percent}% ({votes}) \n")
        
    textfile.write(f"--------------------------\n")
    textfile.write(f"Winner: \n")

    textfile.write(f"--------------------------\n")


    
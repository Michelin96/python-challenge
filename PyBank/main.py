import os
import csv
#import any additional libraries for odd functions

#set the budget_data file path
datapath = os.path.join("", "Resources", "budget_data.csv")

def total_revenue(revenue_amt):
    #accumulate the revenue total
    revenue = revenue + int(revenue_amt[1])
    print(f"Total: ${revenue}")

#def revenue(P_and_L)
    # profit_loss = int(budget_data[1])

#open the budget_data file for reading getting the total months
with open(datapath, 'r') as datafile:
  
    #skip the header row
    data_header = next(datafile)
    
    #datareader specifies the delimiter and stores the file content
    datareader = csv.reader(datafile, delimiter=",")
    
    print(f"Financial Analysis")
    print(f"--------------------------")

    #get the numnber of months in the budget_data file
    months = datafile.readlines()
    total_months = len(months)
    print(f"Total Months: {total_months}")

#open the budget_data file for reading the profit and loss
with open(datapath, 'r') as datafile:
  
    #skip the header row
    data_header = next(datafile)
    
    #datareader specifies the delimiter and stores the file content
    datareader = csv.reader(datafile, delimiter=",")
    
    #calculate the total revene from budget_data
    rev_total = 0
    for row in datareader:
        revenue = int(row[1])
        rev_total += revenue
    
    print(f"Total: ${rev_total}")
    
#  use the  "Profit/Losses"  column to caluculate the total over the entire period

#  use the "Profit/Losses" column to find the average of the changes over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```
# printing the financial analysis to the terminal
   

# print the analysis to the terminal and export a fin_results.txt file with the results.

anaysispath = os.path.join("", "Analysis", "fin_analysis.txt")
with open(anaysispath, 'w') as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"--------------------------\n")
    textfile.write(f"Total months: {total_months}\n")
    textfile.write(f"Total: ${rev_total}\n")
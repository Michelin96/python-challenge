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

#open the budget_data file for reading
with open(datapath) as datafile:

    #skip the header row
    data_header = next(datafile)
    
    #datareader specifies the delimiter and stores the file content
    datareader = csv.reader(datafile, delimiter=",")
    
    print(f"Financial Analysis")
    print(f"--------------------------")

    #get the numnber of months in the budget_data file
    months = datafile.readlines()
    print(f"Total Months: {len(months)}")

    for row in datareader:
       print(f"Budget Data: {row[1]}")


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

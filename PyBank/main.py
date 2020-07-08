import os
import csv

#set the budget_data file path
datapath = os.path.join("", "Resources", "budget_data.csv")

#open the budget_data file for getting the total months
with open(datapath, 'r') as datafile:
  
    #skip the header row
    data_header = next(datafile)
    
    #datareader specifies the delimiter and stores the file content
    datareader = csv.reader(datafile, delimiter=",")
    
    print(f"\nFinancial Analysis")
    print(f"--------------------------")

    #get the numnber of months in the budget_data file
    months = datafile.readlines()
    total_months = len(months)
    print(f"Total Months: {total_months}")

#open the budget_data file for calculating the profit and loss
with open(datapath, 'r') as datafile:
  
    #skip the header row
    data_header = next(datafile)
    
    #datareader specifies the delimiter and stores the file content
    datareader = csv.reader(datafile, delimiter=",")

    #set the vairbales for the calculation totals
    rev_total = 0
    most_increase = 0
    most_decrease = 0

    for row in datareader:
        #calculate the total revene from budget_data
        revenue = int(row[1])
        rev_total += revenue

        profits = int(row[1])
        losses = int(row[1])
        
        if profits > most_increase:
            most_increase = profits
            month_inc = str(row[0])
        elif losses < most_decrease:
            most_decrease = losses
            month_dec = str(row[0])

    #avg_change = most_increase - most_decrease
    
    print(f"Total: ${rev_total}")
    #print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {month_inc} (${most_increase})")
    print(f"Greatest Decrease in Profits: {month_dec} (${most_decrease})")


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
   
# write the analysis results to fin_analysis.txt file.
anaysispath = os.path.join("", "Analysis", "fin_analysis.txt")
with open(anaysispath, 'w') as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"--------------------------\n")
    textfile.write(f"Total months: {total_months}\n")
    textfile.write(f"Total: ${rev_total}\n")
    #textfile.write(f"Average Change: ${avg_change}\n")
    textfile.write(f"Greatest Increase in Profits: {month_inc} (${most_increase})\n")   
    textfile.write(f"Greatest Decrease in Profits: {month_dec} (${most_decrease})")
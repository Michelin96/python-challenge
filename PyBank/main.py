import os
import csv

#set the budget_data file path
datapath = os.path.join("", "Resources", "budget_data.csv")

#open the budget_data file
with open(datapath, 'r') as datafile:

    #skip the header row
    data_header = next(datafile)
        
    #datareader specifies the delimiter and stores the file content
    datareader = csv.reader(datafile, delimiter=",")

    #set the vairbales for the calculation totals
    total_months = 0
    rev_total = 0
    most_increase = 0
    most_decrease = 0
    change = 0
    change_total = 0
    prev_row = 0

    for row in datareader:

        #get the number of months from budget_data
        total_months = total_months + 1
        #calculate the total revene from budget_data
        revenue = int(row[1])
        rev_total += revenue
        
        # find the difference between the current month's profit and the previous month's profit
        if prev_row != 0:
            change = int(row[1]) - prev_row
        change_total += change

        profits = int(row[1])
        losses = int(row[1])
        
        #calculate greatest profit and loss for the period
        if profits > most_increase:
            most_increase = profits
            month_inc = str(row[0])
        elif losses < most_decrease:
            most_decrease = losses
            month_dec = str(row[0])
        
        #store the profit for this row to use on the next row
        prev_row = int(row[1])

    #Averge change in profits over the period. First month has no change.
    avg_change = change_total / (total_months - 1)
    
    print(f"\nFinancial Analysis")
    print(f"--------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${rev_total}")
    print(f"Average Change: ${round(avg_change,2)}")
    print(f"Greatest Increase in Profits: {month_inc} (${most_increase})")
    print(f"Greatest Decrease in Profits: {month_dec} (${most_decrease})\n")
    
# write the analysis results to fin_analysis.txt file.
analysispath = os.path.join("", "Analysis", "fin_analysis.txt")
with open(analysispath, 'w') as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"--------------------------\n")
    textfile.write(f"Total months: {total_months}\n")
    textfile.write(f"Total: ${rev_total}\n")
    textfile.write(f"Average Change: ${round(avg_change,2)}\n")
    textfile.write(f"Greatest Increase in Profits: {month_inc} (${most_increase})\n")   
    textfile.write(f"Greatest Decrease in Profits: {month_dec} (${most_decrease})")
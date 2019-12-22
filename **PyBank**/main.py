#Import Modules 
import os
import csv 
#Set Variables 
#Set Path for CSV file
csvpath = os.path.join ("**PyBank**","budget_data.csv")

#Determine Variables 
totalMonth = 0
netAmount =0
changes =[]
monthlyChange = []
gInc = 0
gIncMonth = 0
gDec = 0
gDecMonth = 0

#Open and Read the CSV file
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
#Calcuate the total number of months and total revenue
    previousProfit = int(row[1])
    totalMonth = totalMonth + 1
    netAmount = netAmount + int(row[1])
    gInc = int(row[1])
    gIncMonth = row[0]

    for row in csvreader:
 
        totalMonth = totalMonth + 1
        netAmount = netAmount + int(row[1])

        # Calculate change from this month to previous months
        change = int(row[1]) - previousProfit
        changes.append(change)
        previousProfit = int(row[1])
        monthlyChange.append(row[0])
        
        #Calculate Greatest Increase 
        if int(row[1]) > gInc:
            gInc = int(row[1])
            gIncMonth = row[0]
            
        #Calculate Greatest Decrese
        if int(row[1]) < gDec:
            gDec = int(row[1])
            gDecMonth = row[0]  
      
    #Calculate Average and the date 
    averageChange = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    #Print Values 
    print(f"Financial Analysis")
    print(f"-----------------------------------")
    print(f"Total Months: {totalMonth}")
    print(f"Total Amount: ${netAmount}")
    print(f"Average Change: ${averageChange: .2f}")
    print(f"Greatest Increse in Profit:, {gIncMonth}, (${max(changes)})")
    print(f"Greatest Decrease in Profit:, {gDecMonth}, (${min(changes)})")

    # Specify File To Write To
    output_file = os.path.join("**PyBank**","FINALPyBank.text")

    # Open File Using "Write" Mode. Specify The Variable To Hold The Contents
    with open(output_file, 'w',) as txt:

# Write New Data
        txt.write(f"Financial Analysis\n")
        txt.write(f"---------------------------\n")
        txt.write(f"Total Months: {totalMonth}\n")
        txt.write(f"Total: ${netAmount}\n")
        txt.write(f"Average Change: ${averageChange: .2f}\n")
        txt.write(f"Greatest Increase in Profits: {gIncMonth} (${max(changes)})\n")
        txt.write(f"Greatest Decrease in Profits: {gDecMonth} (${min(changes)})\n")
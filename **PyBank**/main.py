#Import Modules 
import os
import csv 
#Set Variables 
#Set Path for CSV file
csvpath = os.path.join ("**PyBank**","budget_data.csv")

#initializing the variables 
totalMonth = 0
netAmount =0
changes =[]
monthlyChange = []
gInc = 0
gIncMonth = 0
gDec = 0
gDecMonth = 0

# Open the CSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
# calculating the total number of months and total revenue
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
        
        #calculating the greatest increase
        if int(row[1]) > gInc:
            gInc = int(row[1])
            gIncMonth = row[0]
            
        #calculating the greatest decrease
        if int(row[1]) < gDec:
            gDec = int(row[1])
            gDecMonth = row[0]  
      
    # calculating the average and date
    averageChange = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    # printing all values
    print(f"Financial Analysis")
    print(f"-----------------------------------")
    print(f"Total Months: {totalMonth}")
    print(f"Total Amount: ${netAmount}")
    print(f"Average Change: ${averageChange: .2f}")
    print(f"Greatest Increse in Profit:, {gIncMonth}, (${max(changes)})")
    print(f"Greatest Decrease in Profit:, {gDecMonth}, (${min(changes)})")
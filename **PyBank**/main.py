#Import Modules 
import os
import csv 
#Set Path for CSV file
file = os.path.join('Resources','budget_data.csv')
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
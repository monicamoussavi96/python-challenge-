#Import Modules 
import os
import csv 

#Set Path for CSV file
csvpath = os.path.join ("**PyPoll**","election_data.csv")

# Set Variables 
totalVotes = 0
khanVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row 
    csv_header = next(csvfile)

    # Read Each Row Of Data After The Header
    for row in csvreader:
        
        # Calculate Total Number Of Votes Cast
        totalVotes += 1
        
        # Calculate Total Number Of Votes Each Candidate Won
        if (row[2] == "Khan"):
            khanVotes += 1
        elif (row[2] == "Correy"):
            correyVotes += 1
        elif (row[2] == "Li"):
            liVotes += 1
        else:
            otooleyVotes += 1
            
    # Calculate Percentage Of Votes Each Candidate Won
    kahnPercent = khanVotes / totalVotes
    correyPercent = correyVotes / totalVotes
    liPercent = liVotes / totalVotes
    otooleyPercent = otooleyVotes / totalVotes
    
    # Calculate Winner Of The Election Based On Popular Vote
    winner = max(khanVotes, correyVotes, liVotes, otooleyVotes)

    if winner == khanVotes:
        winner_name = "Khan"
    elif winner == correyVotes:
        winner_name = "Correy"
    elif winner == liVotes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print 
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {totalVotes}")
print(f"---------------------------")
print(f"Kahn: {kahnPercent:.3%}({khanVotes})")
print(f"Correy: {correyPercent:.3%}({correyVotes})")
print(f"Li: {liPercent:.3%}({liVotes})")
print(f"O'Tooley: {otooleyPercent:.3%}({otooleyVotes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Specify File To Write To
output_file = os.path.join("**PyPoll**","FINALPyPoll.text")

# Open File Using "Write" Mode. Specify The Variable 
with open(output_file, 'w',) as txt:

# Write data into text file 
    txt.write(f"Election Results\n")
    txt.write(f"---------------------------\n")
    txt.write(f"Total Votes: {totalVotes}\n")
    txt.write(f"---------------------------\n")
    txt.write(f"Kahn: {kahnPercent:.3%}({khanVotes})\n")
    txt.write(f"Correy: {correyPercent:.3%}({correyVotes})\n")
    txt.write(f"Li: {liPercent:.3%}({liVotes})\n")
    txt.write(f"O'Tooley: {otooleyPercent:.3%}({otooleyVotes})\n")
    txt.write(f"---------------------------\n")
    txt.write(f"Winner: {winner_name}\n")
    txt.write(f"---------------------------\n")
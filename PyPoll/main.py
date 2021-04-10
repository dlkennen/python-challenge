#Python03 Homework Part 2
#Import the os module
import os

#Import the csv module
import csv

#Path for the input csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#Path for th output text file
output_path = os.path.join('Analysis', "polloutput.txt")

#Opening budget data csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skipping header row
    csv_header = next(csvreader)

#Initializing variables
    totalvotes = 0
    candidates = []
    votelist = []
    percentlist = []
    winningvotes = 0
    combinedvotetotal = 0
    index = 0
    winnerindex = 0

#Looping through each row in the spreadsheet to generate list of candidates
    for row in csvreader:
        fullname = row[2]
        if fullname not in candidates:
            candidates.append(fullname)

    #Totalling votes for each candidate 
    for name in candidates:
        #Resetting the CSV iterator
        with open(csvpath) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                fullname = row[2]
                if name == fullname:
                    totalvotes += 1
            votelist.append(totalvotes)
        totalvotes=0

#Determining the winner and combined vote total for the election.
for votes in votelist:
    combinedvotetotal += votes
    if votes > winningvotes:
        winningvotes = votes
        winnerindex = index
    index += 1

#Determining the percentage of votes for each candidate.
for votes in votelist: 
    percent = round((100*float(votes)/float(combinedvotetotal)), 4)  
    percentlist.append(percent)

#Printing output to terminal
print("")
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {combinedvotetotal}")
print("-------------------------------------")

indexN = 0
for name in candidates:
    print(f"{name} : {percentlist[indexN]}% ({votelist[indexN]})")
    indexN += 1

winner = candidates[winnerindex]
print(f"Winner: {winner}")

#Printing output to polloutput.txt
import sys

indexN=0

with open(output_path, 'w') as f:
    print("Election Results", file=f)
    print("-------------------------------------", file=f)
    print(f"Total Votes: {combinedvotetotal}", file=f)
    print("-------------------------------------", file=f)
    for name in candidates:
        print(f"{name} : {percentlist[indexN]}% ({votelist[indexN]})", file=f)
        indexN += 1
    print(f"Winner: {winner}", file=f)
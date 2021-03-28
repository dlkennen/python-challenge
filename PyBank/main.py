#Python03 Homework
#Import the os module
import os

#Import the csv module
import csv

#Path for the input csv file
csvpath = os.path.join('Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

#Path for th output text file
output_path = os.path.join('Analysis', "financialoutput.txt")

#Opening budget data csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skipping header row
    csv_header = next(csvreader)

#Initializing variables
    totalmonths = 0
    totalprofit = 0
    maxdate = "Jan-2010"
    maxprofit = 0
    mindate = "Jan-2010"
    minprofit = 0

#Looping through each row in the spreadsheet
    for row in csvreader:

#Summing up the total months and profit for each row in the csv.
        totalmonths += 1
        totalprofit += int(row[1])

#Replacing the stored minimum or maximum values.
        if int(row[1]) > maxprofit:
            maxprofit = int(row[1])
            maxdate = row[0]
        
        if int(row[1]) < minprofit:
            minprofit = int(row[1])
            mindate = row[0]
 
 #Computing the average change over the data set. 
    averagechange = round((totalprofit/totalmonths), 2)

#Printing output to terminal
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalprofit}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {maxdate} ${maxprofit}")
print(f"Greatest Decrease in Profits: {mindate} ${minprofit}")

#Printing output to financialoutput.txt
import sys

with open(output_path, 'w') as f:
    print("Financial Analysis", file=f)
    print("-------------------------------------", file=f)
    print(f"Total Months: {totalmonths}", file=f)
    print(f"Total: ${totalprofit}", file=f)
    print(f"Average Change: ${averagechange}", file=f)
    print(f"Greatest Increase in Profits: {maxdate} ${maxprofit}", file=f)
    print(f"Greatest Decrease in Profits: {mindate} ${minprofit}", file=f)
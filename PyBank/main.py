#Python03 Homework
#Import the os module
import os

#Import the csv module
import csv
csvpath = os.path.join('Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)

    totalmonths = 0
    totalprofit = 0
    maxdate = "Jan-2010"
    maxprofit = 0
    mindate = "Jan-2010"
    minprofit = 0

    for row in csvreader:
        totalmonths += 1
        totalprofit += int(row[1])

        if int(row[1]) > maxprofit:
            maxprofit = int(row[1])
            maxdate = row[0]
        
        if int(row[1]) < minprofit:
            minprofit = int(row[1])
            mindate = row[0]
    
    averagechange = totalprofit/totalmonths

print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalprofit}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {maxdate} ${maxprofit}")
print(f"Greatest Decrease in Profits: {mindate} ${minprofit}")
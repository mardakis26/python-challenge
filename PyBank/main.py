#import stuff
import os
import csv

#define path
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv' )

#create lists total months and total profit/loss
months = []
profitloss = []

#counter for total number of months in column 1
total_months = 0


#read file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #adds each value in the rows to the list months
        months.append(row[0])
        #adds the integer value in the rows of 2nd column to list profitloss
        profitloss.append(int(row[1]))

#calculate total number of months
total_months = len(months)

#calculates total sum of profit/loss column
PL_sum = sum(profitloss)

#get average of the changes each period
profitchange = []
for x in profitloss:    
    x = 1
    profitchange  = ((profitloss[x] - profitloss[x-1]))/total_months
    
    

print(profitchange)


        







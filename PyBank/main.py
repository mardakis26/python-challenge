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
for x in range(1,(len(months))):    
    profitchange.append((profitloss[x] - profitloss[x-1]))
    #gives average change in profit/loss
    avg_chg = sum(profitchange) / len(profitchange)

#shows max profit
maxprofit = max(profitchange)
#gives index of max profit so I can match it to the date in column 0
max_index = profitchange.index(maxprofit) + 1
#shows date that corresponds to max profit
maxprofit_date = months[max_index]

#shows min profit
minprofit = min(profitchange)
#gives index of min profit so I can match it to the date in column 0
min_index = profitchange.index(minprofit) + 1
#shows date that corresponds to min profit
minprofit_date = months[min_index]

#final results
print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(PL_sum))
print("Average Change: $" + str(avg_chg))
print("Greatest Increase in Profits: " + str(maxprofit_date) + " ($" + str(maxprofit) + ")")
print("Greatest Decrease in Profits: " + str(minprofit_date) + " ($" + str(minprofit) + ")")

#export results to text file
with open("PyBank_Summary.txt","w") as text_file:
    text_file.write("Financial Analysis")
    text_file.write("\n")
    text_file.write("-----------------------")
    text_file.write("\n")
    text_file.write("Total Months: " + str(total_months))
    text_file.write("\n")
    text_file.write("Total: $" + str(PL_sum))
    text_file.write("\n")
    text_file.write("Average Change: $" + str(avg_chg))
    text_file.write("\n")
    text_file.write("Greatest Increase in Profits: " + str(maxprofit_date) + "($" + str(maxprofit) + ")")
    text_file.write("\n")
    text_file.write("Greatest Decrease in Profits: " + str(minprofit_date) + " ($" + str(minprofit) + ")")

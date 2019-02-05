#PYPOLL

#import stuff
import os
import csv

#define path
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv' )

#lists to store data
votes = []
candidates = []
#number of votes counter
total_votes = 0


#read file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #counts total number of votes cast
        total_votes += 1
        #lists ALL candidates (repeating) for entire data set (don't run it because it will take a while!)
        candidates.append(row[2])

#narrows down to unique values for candidates, so lists only 4 ones
uniquecands = set(candidates)
uniquecandslist = list(uniquecands)

x = 0
for x in range(x,2):
    total1 = candidates.count(uniquecandslist[0])
percent1 = str(int(total1/total_votes*100))+"%"

for x in range(x,2):
    total2 = candidates.count(uniquecandslist[1])
percent2 = str(int(total2/total_votes*100))+"%"

for x in range(x,2):
    total3 = candidates.count(uniquecandslist[2])
percent3 = str(int(total3/total_votes*100))+"%"

for x in range(x,2):
    total4 = candidates.count(uniquecandslist[3])
percent4 = str(int(total4/total_votes*100))+"%"


if total1 > total2 and total1 > total3 and total1 > total4:
   winner = (uniquecandslist[0])
elif total2 > total1 and total2 > total3 and total2 > total4:
   winner = (uniquecandslist[1])
elif total3 > total1 and total3 > total2 and total3 > total4:
   winner = (uniquecandslist[2])
elif total4 > total1 and total4 > total2 and total4 > total3:
   winner = (uniquecandslist[3])


#for row in range(len(candidates),2):
 #   candvotes = int(uniquecands[0].count)

#for row in range(len(candidates),2):
 #   x = 0
  #  candvotes = candvotes(uniquecands[x].counts)
   # x += 1

print("Election Results")
print("--------------------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------------------")
print(str(uniquecandslist[0]) + ": " + str(percent1) + " (" + str(total1) + ")")
print(str(uniquecandslist[1]) + ": " + str(percent2) + " (" + str(total2) + ")")
print(str(uniquecandslist[2]) + ": " + str(percent3) + " (" + str(total3) + ")")
print(str(uniquecandslist[3]) + ": " + str(percent4) + " (" + str(total4) + ")")
print("--------------------------------------")
print("Winner: " + str(winner))
print("--------------------------------------")


#export results to text file
with open("PyPoll_Summary.txt","w") as text_file:
   text_file.write("Election Results")
   text_file.write("\n")
   text_file.write("--------------------------------------")
   text_file.write("\n")
   text_file.write("Total Votes: " + str(total_votes))
   text_file.write("\n")
   text_file.write("--------------------------------------")
   text_file.write("\n")
   text_file.write(str(uniquecandslist[0]) + ": " + str(percent1) + " (" + str(total1) + ")")
   text_file.write("\n")
   text_file.write(str(uniquecandslist[1]) + ": " + str(percent2) + " (" + str(total2) + ")")
   text_file.write("\n")
   text_file.write(str(uniquecandslist[2]) + ": " + str(percent3) + " (" + str(total3) + ")")
   text_file.write("\n")
   text_file.write(str(uniquecandslist[3]) + ": " + str(percent4) + " (" + str(total4) + ")")
   text_file.write("\n")
   text_file.write("--------------------------------------")
   text_file.write("\n")
   text_file.write("Winner: " + str(winner))

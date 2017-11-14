import csv
file = open("election_data_1.csv",newline='')
reader = csv.reader(file)
count =0
for line in reader:
    count = count +1
print("Election Results")
print("-------------------------------")
print("Total Votes:  " + str(count-1))
print("-------------------------------")

file = open("election_data_1.csv",newline='')
reader = csv.reader(file)
import collections
from collections import Counter
for row in reader:
    c = Counter(row[2] for row in reader)
for name, num_vote in c.items():
    percentage = num_vote/(count-1)
    print(name + ": " + format(percentage,'0.0%')+ "(" + str(num_vote)+")")
Winner = c.most_common(1)

for name, num in Winner:
    print("-------------------------------")
    print("Winner: " + name)
    print("-------------------------------")    

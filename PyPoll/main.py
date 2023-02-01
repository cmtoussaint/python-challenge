#import the os & csv modules
import os
import csv

#add path to reference later
CSVPATH = os.path.join('Resources', 'election_data.csv')
os.chdir(os.path.dirname(os.path.realpath(__file__)))
#add column number to reference later
CANDIDATE_COL = 2

#declare variables starting at 0 to begin
total = 0 
stockham = 0
degette = 0
doane = 0
#create a dictionary for candidates
votes = {}

#locate csv file needed
with open(CSVPATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header row
    header = next(csvreader)

    #loop through csv file
    for row in csvreader:
        #add 1 to "total" above for each value
        total += 1
        #test if each row in the candidate column has the candidate's name then add
        #to the candidate variable respectively
        if row[CANDIDATE_COL] == "Diana DeGette":
            degette += 1
        elif row[CANDIDATE_COL] == "Raymon Anthony Doane":
            doane += 1
        elif row[CANDIDATE_COL] == "Charles Casper Stockham":
            stockham += 1

        #create dictionary with the candidate column and vote count
        current_candidate = row[CANDIDATE_COL]
        if current_candidate in votes:
            votes[current_candidate] += 1
        else:
            votes[current_candidate] = 1         


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")
#print from declared variables above the candidate's vote count/total, round to the 
#1000th and then print the candidate's total
print(f"Charles Casper Stockham: {round(stockham / total * 100, 3)}% ({stockham})")
print(f"Diana DeGette: {round(degette / total * 100, 3)}% ({degette})")
print(f"Raymon Anthony Doane: {round(doane / total * 100, 3)}% ({doane})")
print("-------------------------")
#use dictionary to find the max value, sort by the second element (the value)
max_value = max(votes, key=lambda x: votes[x]) 
print(f"Winner: {max_value}")
print("-------------------------")
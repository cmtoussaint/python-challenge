#import the os & csv modules
import os
import csv

#add path to reference later
csvpath = os.path.join("Resources", "budget_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))


#create a place to store lists
date = []
total = [] 
change = []

#locate csv file needed
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        #skip header row
        csvheader = next(csvreader)

        #loop through csv file
        for row in csvreader:
            #print (row[0])
            #add each month to the list above
            date.append(row[0])
            #add each profit value to the list above, 
            #convert from string to integer for the values in the second column in the csv file
            total.append(int(row[1]))
        # assign an index number "x" to values in the total list that we appended to in previous step, 
        # count values in the range with "len" or length omitting the header
        for x in range(len(total)-1):
            #calculate the change in profits
            change.append(total[x+1]-total[x])

#find the min and max profit values
increase = max(change)
decrease = min(change)

#locate the row with the min and max and then go one to the right
increase_month = change.index(max(change)) + 1
decrease_month = change.index(min(change)) + 1
        
print("Financial Analysis")
print("----------------------------")
#calculate the number of variables in the date list
print(f"Total Months: {len(date)}")
#sum the total list
print(f"Total: ${sum(total)}")
#calculate the average from the change list
print(f"Average Change: ${round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {date[increase_month]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {date[decrease_month]} (${(str(decrease))})")

import os
import csv

budget = os.path.join("Resources", "budget_data.csv")


# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

total_months = 0
total_pl = 0
month_change = 0
previous_month = 0
total_month_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""
average_month_change = 0

with open(budget) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_months += 1
        total_pl +=int(row[1])

        if total_months > 1:
            month_change = int(row[1]) - previous_month
        total_month_change += month_change
        previous_month = int(row[1])

        if month_change > greatest_increase:
            greatest_increase = month_change
            greatest_increase_month = row[0]
        

average_month_change = total_month_change / (total_months-1)

print(total_month_change)
print(month_change)
print(average_month_change)
print(total_months)
print(total_pl)
#print(greatest_increase_month)
#print(greatest_increase)   
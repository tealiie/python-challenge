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

        if month_change < greatest_decrease:
            greatest_decrease = month_change
            greatest_decrease_month = row[0]
            
average_month_change = total_month_change / (total_months-1)



print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_pl))
print("Average Change: $" + str(round(average_month_change,2)))
print("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")")

file_to_output = os.path.join("analysis", "budget_analysis.txt")
with open(file_to_output, "w") as txt_file:

    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write("Total Months: " + str(total_months) + "\n")
    txt_file.write("Total: $" + str(total_pl) + "\n")
    txt_file.write("Average Change: $" + str(average_month_change) + "\n")
    txt_file.write("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")\n")
    txt_file.write("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")\n")


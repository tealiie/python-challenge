import os
import csv

poll_data = os.path.join("Resources", "election_data.csv")

total_votes = []
correy_count = 0
khan_count = 0
li_count = 0
otooley_count = 0


with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes.append(row[0])
        if row[2] == "Correy":
            correy_count += 1
        elif row[2] == "Khan":
            khan_count += 1
        elif row[2] == "Li":
            li_count += 1
        else: 
            otooley_count += 1

correy_percent = (correy_count / len(total_votes)) * 100
khan_percent = (khan_count / len(total_votes)) * 100
li_percent = (li_count / len(total_votes)) * 100
otooley_percent = (otooley_count / len(total_votes)) * 100

percentages = [correy_percent, khan_percent, li_percent, otooley_percent]
if max(percentages) == correy_percent:
    winner = "Correy Wins!"
elif max(percentages) == khan_percent:
    winner = "Khan Wins!"
elif max(percentages) == li_percent:
    winner = "Li Wins!"
else:
    winner = "O'Tooley Wins!"    


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(total_votes)))
print("-------------------------")
print("Khan: " + str(round(khan_percent,4)) + "%" + " (" + str(khan_count) + ")")
print("Correy: " + str(round(correy_percent,4)) + "%" + " (" + str(correy_count) + ")")
print("Li: " + str(round(li_percent,4)) + "%" + " (" + str(li_count) + ")")
print("O'Tooley: " + str(round(otooley_percent,4)) + "%" + " (" + str(otooley_count) + ")")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")


file_to_output = os.path.join("analysis", "poll_analysis.txt")
with open(file_to_output, "w") as txt_file:

    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Total Votes: " + str(len(total_votes)))
    txt_file.write("\n-------------------------\n")
    txt_file.write("Khan: " + str(round(khan_percent,4)) + "%" + " (" + str(khan_count) + ")\n")
    txt_file.write("Correy: " + str(round(correy_percent,4)) + "%" + " (" + str(correy_count) + ")\n")
    txt_file.write("Li: " + str(round(li_percent,4)) + "%" + " (" + str(li_count) + ")\n")
    txt_file.write("O'Tooley: " + str(round(otooley_percent,4)) + "%" + " (" + str(otooley_count) + ")\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Winner: " + str(winner))
    txt_file.write("\n-------------------------")



  
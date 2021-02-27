import os
import csv

# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: 
#Voter ID, County, and Candidate. Your task is to create a Python script that analyzes 
#the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

poll_data = os.path.join("Resources", "election_data.csv")

total_votes = []

with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)



def poll_results(poll_data):
    voter_id = int(poll_data[0])
    country = str(poll_data[1])
    candidate = str(poll_data[2])

    total_votes = sum(voter_id)

print(total_votes)

  